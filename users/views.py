from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import User
from .forms import UserForm
import json
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    """Render the index page."""
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def user_list(request):
    """List users with pagination."""
    user_queryset = User.objects.all()

    # Set up pagination, 10 items per page
    paginator = Paginator(user_queryset, 10)
    
    # Get the current page number from the request
    page_number = request.GET.get('page', 1)
    
    # Get the corresponding page of users
    users_page = paginator.get_page(page_number)

    return render(request, "user_list.html", {"users": users_page})

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])  
            user.save()
            return redirect("users")
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})
    
        

def update_user(request, user_id):
    """Update an existing user."""
    try:
        user = User.objects.get(pk=user_id)
        
        if request.method == "POST":
            # Handle POST request for updating a user
            data = json.loads(request.body)
            form = UserForm(data, instance=user)
            
            if form.is_valid():
                user = form.save(commit=False)
                if 'password' in data:
                    user.password = make_password(data['password'])  # Hash the password
                user.save()
                return JsonResponse({'success': True, 'message': 'User updated successfully'})

            return JsonResponse({'success': False, 'message': 'Invalid form data'}, status=400)
    
    except User.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'User not found'}, status=404)

    # Render the update form for GET requests
    form = UserForm(instance=user)
    return render(request, "update_user.html", {"form": form})

def delete_user(request, user_id):
    """Delete an existing user."""
    try:
        user = User.objects.get(pk=user_id)
        
        if request.method == "POST":
            # Handle POST request for deleting a user
            user.delete()
            return JsonResponse({'success': True, 'message': 'User deleted successfully'})
    
    except User.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'User not found'}, status=404)

    return render(request, "delete_user.html", {"user": user})
