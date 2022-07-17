from django.shortcuts import redirect, render
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from users.models import Profile
from .bot.notify import send_notify


def getAllPosts(user):
    class_num = user.profile.user_class_number
    class_let = user.profile.user_class_letter

    all_visibles = Post.objects.filter(visible_all=True)
    all_private_posts = Post.objects.filter(visible_all=False)

    class_visibles = []

    for el in all_private_posts:

        if el.visible_class.isnumeric():
            if el.visible_class == class_num:
                class_visibles.append(el)
        else:
            if el.visible_class == class_num+class_let:
                class_visibles.append(el)
    
    all_posts = list(all_visibles) + class_visibles

    return all_posts

def sort_posts(posts):
    return sorted(posts, key=lambda x: x.updated_at, reverse=True)

def checkPostVisible(el, user):
    class_num = user.profile.user_class_number
    class_let = user.profile.user_class_letter
    if el.visible_all == True:
        return True
    if el.visible_class.isnumeric():
        if el.visible_class == class_num:
            return True
    else:
        if el.visible_class == class_num+class_let:
            return True
    return False

def index(request):
    latest_posts = []
    if request.user:
        latest_posts = getAllPosts(request.user)[:3]

    context = {'title': 'Главная страница', 'posts': sort_posts(latest_posts)}
    return render(request, 'mainapp/index.html', context=context)

@login_required
def posts_all(request):
    if request.user.is_superuser:
        posts = Post.objects.all()
        context = {'posts': posts, 'title': 'Все посты'}
        return render(request, 'mainapp/posts_all.html', context)
    else:
        messages.error(request, 'У вас нет разрешений на промотр данной страницы!')
        return redirect('index')

@login_required
def post_detail(request, postid):
    post = Post.objects.get(id=postid)
    if checkPostVisible(post, request.user) == True or request.user.is_superuser:
        context = {'post': post, 'title': f'Пост {post.title}'}
        return render(request, 'mainapp/post_detail.html', context)
    else:
        messages.error(request, 'У вас нет разрешений на промотр данной страницы!')
        return redirect('posts')

@login_required
def posts(request):

    all_posts = getAllPosts(request.user)

    context = {"posts": sort_posts(all_posts), 'title': 'Посты'}
    return render(request, 'mainapp/posts.html', context=context)

@login_required
def create_post(request):
    if request.user.is_superuser:

        if request.method == "POST":

            post_form = PostCreateForm(request.POST, request.FILES)

            users = []

            if post_form.is_valid():

                post = post_form.save()
                post.visible_class = post.visible_class.upper()
                post.save()

                if post.visible_all == False:
                    if post.visible_class.isnumeric():
                        for i in Profile.objects.filter(user_class_number=post.visible_class):
                            users.append(i.user.id)
                    else:
                        for i in Profile.objects.all():
                            if(i.user_class_number+i.user_class_letter == post.visible_class):
                                users.append(i.user.id)
                else:
                    for i in Profile.objects.all():
                        users.append(i.user.id)

                send_notify(users, f"Новая новость!\nСсылка на неё: http://127.0.0.1:8000/post_detail/{post.id}/")

                messages.success(request, 'Ваш пост был успешно создан!')
                return redirect('index')

        else:

            post_form = PostCreateForm()
            context = {'post_form': post_form, 'title': 'Создать пост'}
            return render(request, 'mainapp/create_post.html', context)
    else:
        messages.error(request, 'У вас нет разрешений на публикацию новостей!')
        return redirect('index')