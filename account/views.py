from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse
from account.email_sender import send_verification_code
from account.forms import LoginForm, AddressCreationForm, VerifyCodeForm, UserCreationForm
from django.views import View



class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            userr = authenticate(username=cd['email'], password=cd['password'])
            if userr is not None:
                login(request, userr)
                return redirect('home:home')
            else:
                form.add_error(None, 'Username or password is incorrect')
        return render(request, 'account/login.html', {'form': form})


class AddAddressView(View):
    def post(self, request):
        form = AddressCreationForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)

        return render(request, 'account/add_address.html', {'form': form})

    def get(self, request):
        form = AddressCreationForm()
        return render(request, 'account/add_address.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd['email']
            password = cd['password1']
            send_verification_code(email)
            return redirect(reverse('account:verifycode') + f'?email={email}&password={password}')
        return render(request, 'account/register.html', {'form': form})


User = get_user_model()


class VerifyCode(View):
    def get(self, request):
        form = VerifyCodeForm()
        return render(request, 'account/verify_code.html', {'form': form})

    def post(self, request):
        email = request.GET.get('email')
        password = request.GET.get('password')
        post_data = request.POST.copy()
        post_data['email'] = email
        post_data['password'] = password
        form = VerifyCodeForm(post_data)
        if form.is_valid():
            user = User.objects.create_user(email=email, password=password)
            login(request, user)
            return redirect(reverse('home:home'))
        return render(request, 'account/verify_code.html', {'form': form})

