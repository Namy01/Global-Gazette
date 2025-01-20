from datetime import timedelta
from django.utils import timezone
from .models import Post, Tag, Category, Comment

def navigations(request):
   trending = Post.objects.filter(published_at__isnull= False, status = "active").order_by("-views_count")[:5]
   tags = Tag.objects.all()[:10]
   categories = Category.objects.all()[:5]
   populars = Post.objects.filter(published_at__isnull= False, status = "active"
   ).order_by("-views_count")[:3]
   latest = Post.objects.filter(published_at__isnull= False, status = "active"
   ).order_by("-published_at", "-views_count")[5:9]
   latest_small1 = Post.objects.filter(published_at__isnull= False, status = "active"
   ).order_by("-published_at", "-views_count")[1:3]
   latest_small2 = Post.objects.filter(published_at__isnull= False, status = "active"
   ).order_by("-published_at", "-views_count")[4:6]

   one_week_ago = timezone.now() - timedelta(days=15)
   weekly = Post.objects.filter(published_at__isnull= False, status = "active", published_at__gte = one_week_ago
   ).order_by("-published_at", "-views_count").first()

   weekly1 = Post.objects.filter(published_at__isnull= False, status = "active", published_at__gte = one_week_ago
   ).order_by("-published_at", "-views_count")[5:7]

   weekly2 = Post.objects.filter(published_at__isnull= False, status = "active", published_at__gte = one_week_ago
   ).order_by("-published_at", "-views_count")[7:9]

   return {
      "trending":trending,
      "tags" : tags,
      "categories":categories,
      "populars": populars,
      "latest": latest,
      "latest_small1": latest_small1,
      "latest_small2": latest_small2,
      "weekly": weekly,
      "weekly1": weekly1,
      "weekly2": weekly2,


      }
   
