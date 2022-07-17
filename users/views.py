from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, UserUpdateForm
from transliterate import translit

@login_required
def profile(request):

    user_class = translit(request.user.profile.user_class_number+request.user.profile.user_class_letter, "ru", reversed=True)

    if request.method == "POST":
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()

            profile = profile_form.save()
            profile.user_class_letter = profile.user_class_letter.upper()
            profile.save()

            messages.success(request, 'Ваш аккаунт был успешно обновлен!')
            return redirect('profile')
    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        user_form = UserUpdateForm(instance=request.user)

    context = {'user_class': user_class, 'profile_form': profile_form, 'user_form': user_form, 'title': 'Профиль'}
    return render(request, 'users/profile.html', context)