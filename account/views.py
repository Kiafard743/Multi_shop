from email.header import Header

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from account.email_sender import send_verification_code
from account.forms import LoginForm, AddressCreationForm, RegisterForm, VerifyCodeForm, UserCreationForm
from django.views import View

from account.models import EmailVerification


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
            email2 = str(Header(email, "utf-8"))
            print(email2)
            send_verification_code(email2)
            return redirect(reverse('account:verifycode') + f'?email={cd["email"]}')
        return render(request, 'account/register.html', {'form': form})

    # def post(self, request):
    #     email = request.POST.get("email")
    #     send_verification_code(email)
    #     return redirect('account:verifycode' + f'?email={cd[email]}')


# def request_verification_code(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         send_verification_code(email)
#         return JsonResponse({"message": "کد برای ایمیل ارسال شد."})


class VerifyCode(View):
    def get(self, request):
        form = VerifyCodeForm()
        return render(request, 'account/verify_code.html', {'form': form})

    def post(self, request):
        email = request.GET.get('email')
        post_data = request.POST.copy()
        post_data['email'] = email
        form = VerifyCodeForm(post_data)
        if form.is_valid():
            return redirect(reverse('home:home'))
        return render(request, 'account/verify_code.html', {'form': form})

    # def post(self, request):
    #         email = request.GET.get("email")
    #         code = request.POST.get("code")
    #         try:
    #             verification = EmailVerification.objects.get(email=email, code=code)
    #             if verification.is_expired():
    #                 return JsonResponse({"error": "کد منقضی شده."}, status=400)
    #             return JsonResponse({"message": "کد صحیح است، ادامه بده."})
    #         except EmailVerification.DoesNotExist:
    #             return JsonResponse({"error": "کد اشتباه است."}, status=400)


