from django.shortcuts import render
from django.views import View
from landing_page.forms import LogIn, UserRegistrationForm, SuperUpload
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from landing_page.models import BlogStuff, Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

#this is our home page that has links to log in, sign up,  and the gallery.
def landing_page(request):
    user  = request.user
    return render(request, 'landing_page/home.html',{'user':user})

#this is just a sample class view usage.It really does nothing but display text.
class page_sample(View):
    template_name = 'landing_page/sample.html'
    
    def get(self, request):
            return render(request, self.template_name)

# Still to implement : Forgot your password
def log_in(request):
    if request.method == 'POST':
        form = LogIn(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'],
                password=cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'landing_page/home.html', {
                        'user': user
                    })
            else:
                # this part needs fixing.
                return HttpResponse('Error user does not exist')
        else:
            return HttpResponse('Invalid login ')
    else:
        form = LogIn()
        return render(request, 'landing_page/login.html', {
            'form': form
        })

# this logouts the user and should redirect them to a page where hthey can log in again.
def logout_view(request):
    logout(request)
    return render(request, 'landing_page/home.html')

# Working perfectly fine 
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
        return render(request,
                      'landing_page/login.html',
                      {
                          'new_user': new_user
                      })
    else:
        user_form = UserRegistrationForm()
        return render(request,
                      'landing_page/sign_up.html',
                      {
                          'user_form': user_form
                      })

# It is working but the design still needs some work. It still is kinda useless tho.
def display_image(request, id):
    image = get_object_or_404(BlogStuff, pk=id)
    context = {
        'image':image
    }
    return render(request, 'landing_page/display_image.html', context)

# Working great! displaying images pretty well but needs more bootstrap design.
def gallery(request):
    images = BlogStuff.objects.all()
    user = request.user
    context = {
        'images': images,
        'user':user,
    }
    return render(request, 'landing_page/gallery.html', context)

#Working well. Uploading pictures as expected.
def super_user(request):
    if request.method == 'POST':
        upload_form = SuperUpload(request.POST, request.FILES)
        if upload_form.is_valid():
            # save the documents to database.
            form = upload_form.save()
            return render(request, 'landing_page/super_user.html', {'form':form})
    else:
        upload_form = SuperUpload()
        return render(request, 'landing_page/super_user.html')

#shows your profile details and should allow you to make changes.
# Not working well.
def profile(request, id):
    my_profile = get_object_or_404(Profile, pk=id)
    return render(request, 'landing_page/users/profile.html', {'my_profile':my_profile})