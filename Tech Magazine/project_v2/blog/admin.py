from django.contrib import admin
from .models import Article, Comment

# ثبت مدل Article و تنظیمات ادمین آن
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'views')  # نمایش فیلدها در لیست مقالات
    list_filter = ('author', 'publish_date')  # فیلترها در پنل ادمین
    search_fields = ('title', 'body')  # قابلیت جستجو در پنل ادمین

    ordering = ('-publish_date',)


    readonly_fields = ('publish_date','views')

    # افزودن فیلد image به فرم ادمین
    fields = ('title', 'author', 'body', 'publish_date', 'image')  # اضافه کردن image در اینجا

# ثبت مدل Comment و تنظیمات ادمین آن
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'article', 'publish_date', 'approved')
    list_filter = ('approved', 'publish_date')
    search_fields = ('name', 'content')

    actions = ['approve_comments', 'reject_comments']  # عملیات تایید و رد کامنت

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

    def reject_comments(self, request, queryset):
        queryset.update(approved=False)

admin.site.register(Comment, CommentAdmin)


# ثبت مدل CustomUser و تنظیمات ادمین آن
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('profile_picture',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('profile_picture',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)