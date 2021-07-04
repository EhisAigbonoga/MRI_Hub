from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from courses.views import Course, Category as Course_Category






def home(request):
    big_post_latest = Post.objects.all()[:1]
    small_post_latests1 = Post.objects.all()[1:4]
    small_post_latests2 = Post.objects.all()[4:7]
    categories = Category.objects.all()
    big_course_latest1 = Course.objects.all()[:1]
    big_course_latest2 = Course.objects.all()[1:2]
    big_course_latest3 = Course.objects.all()[2:3]
    course_categories = Course_Category.objects.all()




    context = {
    "big_post_latest" : big_post_latest,
    "small_post_latests1": small_post_latests1,
    "small_post_latests2" : small_post_latests2,
    "categories" : categories,
    "big_course_latest1": big_course_latest1,
    "big_course_latest2": big_course_latest2,
    "big_course_latest3": big_course_latest3,
    "course_categories" : course_categories
    }
    return render(request, 'crihhome/homepage.html', context)


def post_detail(request, slug, pk):
    post = get_object_or_404(Post, slug=slug, pk=pk)
    context = {
        "post": post,
    }
    return render(request, "crihhome/post_detail.html", context)