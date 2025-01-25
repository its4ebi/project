from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from .forms import CommentForm

# صفحه اصلی (نمایش مقالات اخیر و پر بازدید)
def home(request):
    recent_articles = Article.objects.order_by('-publish_date')[:3]
    popular_articles = Article.objects.order_by('-views')[:3]

    context = {
        'recent_articles': recent_articles,
        'popular_articles': popular_articles,
    }
    return render(request, 'blog/article_list.html', context)

# صفحه لیست مقالات (برای صفحه جدید با مرتب سازی)
def article_list(request):
    sort_by = request.GET.get('sort_by', 'publish_date')  # مقدار پیش‌فرض تاریخ انتشار است
    articles = Article.objects.all().order_by(f"-{sort_by}")  # ترتیب نزولی

    return render(request, 'blog/articles.html', {'articles': articles})

# جزئیات مقاله
def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    
    # افزایش تعداد بازدید مقاله
    article.views += 1
    article.save()

    # بررسی درخواست POST برای ارسال نظر
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article  # اتصال کامنت به مقاله مربوطه
            comment.save()  # ذخیره کامنت در پایگاه داده
            return redirect('article_detail', id=article.id)
    else:
        form = CommentForm()

    # گرفتن کامنت‌های تایید شده
    comments = article.comments.filter(approved=True)

    return render(request, 'blog/article_detail.html', {
        'article': article,
        'form': form,
        'comments': comments,
    })

def article_list(request):
    # دریافت پارامتر مرتب‌سازی از URL
    sort_by = request.GET.get('sort_by', 'publish_date')  # مقدار پیش‌فرض 'publish_date' است

    # بازیابی مقالات و مرتب‌سازی بر اساس پارامتر sort_by
    articles = Article.objects.all().order_by(f"-{sort_by}")

    return render(request, 'blog/articles.html', {'articles': articles})

from django.shortcuts import render

def about(request):
    return render(request, 'blog/about.html')  # اگر فایل در templates/blog/ قرار دارد

def contact(request):
    admins = [
    {
        'name': 'ebi',
        'email': 'ebi.firoozy@gmail.com',
        'profile_pic': 'images/photo_2024-12-15_13-45-16.jpg'
    },
    {
        'name': 'fatemeh',
        'email': 'fatm.sad2001@gmail.com',
        'profile_pic': 'images/photo_2025-01-25_00-19-27.jpg'
    },
    {
        'name': 'majede',
        'email': 'Majedeh.motraghi18@gmail.com',
        'profile_pic': 'images/photo_2025-01-24_22-50-51.jpg'
    },
    {
        'name': 'idin',
        'email': 'idinkhosravian@gmail.com',
        'profile_pic': 'images/idin.jpg'
    },
]
    return render(request, 'blog/contact.html', {'admins': admins})