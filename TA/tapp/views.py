from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Essay
from django.contrib.auth.models import User, Group
from guardian.shortcuts import get_objects_for_group, assign_perm

def index(request):
    return render(request, 'tapp/index.html')

# Author distinct from everyone else - author's view is different
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse('tapp:essay_group'))
        else:
            # Return a 'disabled account' error message
             return HttpResponseRedirect(reverse('tapp:index'))
    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect(reverse('tapp:index'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('tapp:index'))

# def create_user(request):
def signup(request):
    return render(request, 'tapp/signup.html')

def signup_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        user = User.objects.create_user(username=username ,password=password)
        user.save()
        user = authenticate(username=username, password=password)
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('tapp:essay_group'))
        return HttpResponseRedirect(reverse('tapp:signup'))
    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect(reverse('tapp:signup'))   

@login_required
def essay_group(request):
    # add group like this:
    # grp.user_set.add(usr)

    # assign perms to group:
    # assign_perm('view_essay', grp, ess)
    users_groups = []
    all_users = []
    if request.user.is_authenticated():
        current_user = request.user
        users_groups = current_user.groups.all()
        all_users = User.objects.all()
    context = {'users_groups': users_groups,
                'all_users' : all_users}
    return render(request, 'tapp/essay_group.html', context)

@login_required
def filter_essay_group(request, filter_user_id):
    users_groups = []
    all_users = []
    filter_user = User.objects.get(id=filter_user_id)
    if request.user.is_authenticated():
        current_user = request.user
        users_groups = current_user.groups.all()
        filter_users_groups = filter_user.groups.all()
        intersection_groups = users_groups & filter_users_groups
        all_users = User.objects.all()
    context = {'users_groups': intersection_groups,
                'all_users' : all_users}
    return render(request, 'tapp/essay_group.html', context)  

@login_required
def new_essay_group(request):
    # don't create an essay group if group already exists
    name = request.POST['name']
    if request.user.is_authenticated():
        current_user = request.user
        grp = Group.objects.create(name=name)
        grp.user_set.add(current_user)
        return HttpResponseRedirect(reverse('tapp:essays', args=(grp.id,)))
    return HttpResponseRedirect(reverse('tapp:essay_group'))

@login_required
def delete_essay_group(request, group_id):
    # only allow deletion by author 
    current_user = request.user
    grp = Group.objects.get(id=group_id)
    grp.delete()
    users_groups = current_user.groups.all()
    all_users = User.objects.all()
    context = {'users_groups': users_groups,
                'all_users' : all_users}
    return render(request, 'tapp/essay_group.html', context)  

@login_required
def essays(request, group_id):
    # Check which essays to show only here. 
    # Do we need the group?
    # Do we need the user? 
    # Does anything have to be passed to essays()

    latest_essay_list = []
    if request.user.is_authenticated():
        current_user = request.user
        grp = Group.objects.get(id=group_id)
        e_group_users = grp.user_set.all()
        group_name = grp.name
        latest_essay_list = get_objects_for_group(grp, 'tapp.view_essay')
    context = {'latest_essay_list': latest_essay_list, 
                'group_id': group_id,
                'group_name': group_name,
                'e_group_users': e_group_users}
    return render(request, 'tapp/essays.html', context)

def add_user_to_essay(request, group_id):
    username = request.POST['username']
    # treat the error the same way as you did in addcomment 
    try:
        new_user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('tapp:essays', args=(group_id,)))
    grp = Group.objects.get(id=group_id)
    grp.user_set.add(new_user)
    return HttpResponseRedirect(reverse('tapp:essays', args=(grp.id,)))

def add_essay_text(request, group_id):
    author = request.user.username
    title = request.POST['title']
    text = request.POST['text']
    new_e_version = Essay(essay_title=title, essay_text=text, 
                            pub_date=timezone.now(), author=author)
    new_e_version.save()
    grp = Group.objects.get(id=group_id)
    assign_perm('view_essay', grp, new_e_version)
    return HttpResponseRedirect(reverse('tapp:essays', args=(grp.id,)))

@login_required
def detail(request, essay_id):
    essay = get_object_or_404(Essay, pk=essay_id)
    comments = essay.comment_set.all().order_by('-start_i')
    return render(request, 'tapp/detail.html', {'essay':essay,
                                                'comments':comments})

@login_required
def add_comment(request, essay_id):
    author = request.user.username
    p = get_object_or_404(Essay, pk=essay_id)
    new_text = request.POST['comment']
    start = request.POST['start']
    end = request.POST['end']
    if new_text == "":
    	return render(request, 'tapp/detail.html', {
    		'essay': p,
    		'error_message': "You didn't add text.", 
    		})
    else:
    	p.comment_set.create(comment_text=new_text, start_i=start, end_i=end, author=author,)
    	return HttpResponseRedirect(reverse('tapp:detail', args=(p.id,)))
