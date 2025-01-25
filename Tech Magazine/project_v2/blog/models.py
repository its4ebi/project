from django.db import models
from django.utils.text import slugify
from django.conf import settings  # برای استفاده از AUTH_USER_MODEL

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # اشاره به مدل کاربری سفارشی
        on_delete=models.CASCADE,  # حذف مقالات هنگام حذف کاربر
        related_name='articles',  # دسترسی به مقالات از طریق کاربر
    )
    publish_date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)  # شمارنده بازدید
    sources = models.TextField(blank=True, null=True)  # منابع
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)  # تصویر
    slug = models.SlugField(unique=True, blank=True)  # امکان خالی بودن در فرم

    def save(self, *args, **kwargs):
        if not self.slug:  # اگر slug خالی بود
            base_slug = slugify(self.title)  # slug اولیه بر اساس عنوان
            slug = base_slug  # مقدار پایه
            counter = 1  # شمارنده برای مقادیر تکراری
            # چک می‌کنیم که slug تکراری نباشه
            while Article.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"  # عدد به انتها اضافه می‌شه
                counter += 1  # شمارنده افزایش پیدا می‌کنه
            self.slug = slug  # مقدار نهایی به slug اختصاص داده می‌شه

        # تبدیل \n به <br> برای حفظ فاصله‌ها
        self.body = self.body.replace('\n', '<br>')

        super().save(*args, **kwargs)  # ذخیره در دیتابیس

    def __str__(self):
        return self.title  # همچنان عنوان مقاله به صورت ساده نمایش داده می‌شود


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)  # وضعیت تایید کامنت (برای ادمین)

    def __str__(self):
        return f"Comment by {self.name} on {self.article.title}"


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)