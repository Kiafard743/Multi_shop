from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from account.forms import LoginForm, AddressCreationForm
from django.views import View


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            userr = authenticate(username=cd['phone'], password=cd['password'])
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