
from django.shortcuts import render, redirect
from pollmembers.models import BookInstance
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login as login_user, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def index(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:

        return render(request, 'games.html')

def signout(request):
    logout(request)
    return redirect('/login')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST': 
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save() # save the user

            # login this new user
            user_name = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username = user_name, password = password)
            login_user(request, user)
            return redirect('/')

        else:
            # form not valid
            return render(request, 'auth/signup.html', {'form': form })

    else:
        # not post = GET
        form = UserCreationForm()
        return render(request, 'auth/signup.html', {'form': form })


def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST': 
        # validate credential
        user_name = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = user_name, password = password)

        if user is not None: 
            # valid creds
            login_user(request, user) # save the user as logged in
            return redirect('/')
        else:
            form = AuthenticationForm()
            return render(request, "auth/login.html", {"form": form})

    else:
        form = AuthenticationForm()
        return render(request, "auth/login.html", {"form": form})   

    form = AuthenticationForm()
    return render(request, "auth/login.html", {"form": form})

  

class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

   




class LoanedBooksByUserListView(LoginRequiredMixin,ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

from django.contrib.auth.decorators import permission_required

@permission_required('catalog.can_mark_returned')
@permission_required('catalog.can_edit')
def my_view(request):
    ...

from django.contrib.auth.mixins import PermissionRequiredMixin

class MyView(PermissionRequiredMixin, View):
    permission_required = 'catalog.can_mark_returned'
    # Or multiple permissions
    permission_required = ('catalog.can_mark_returned', 'catalog.can_edit')
    # Note that 'catalog.can_edit' is just an example
    # the catalog application doesn't have such permission!
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def my_view(request):
    ...








      
# Create your views here.
