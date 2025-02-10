from datetime import timedelta
from django.utils import timezone
from sqlite3.dbapi2 import Timestamp
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.core.paginator import PageNotAnInteger, Paginator
from django.db.models import Q


from news_app.forms import CommentForm, ContactForm
from .models import Post, Category , Comment, Tag

from django.views.generic import ListView, DetailView, View, TemplateView

class HomeView(ListView):
    model : Post
    template_name = "global/home/home.html"
    context_object_name = "posts"
    queryset = Post.objects.filter(published_at__isnull= False, status = "active").order_by("-published_at")[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['slider_post'] = Post.objects.filter(published_at__isnull= False, status = "active").order_by("-published_at", "-views_count")[4:7]
        context['title'] = Post.objects.filter(published_at__isnull= False, status = "active").order_by("-published_at")[4:7]
        
        context['featured'] = Post.objects.filter(published_at__isnull= False, status = "active").order_by("-published_at", "-views_count")[:7]
        return context

        
class PostListView(ListView):
    model = Post
    template_name = "global/list/post_list.html"
    context_object_name = "posts"
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(
        published_at__isnull = False , status = "active"
        ).order_by("-published_at")
    
class PostListByCategory(ListView):
    model = Post
    template_name = "global/list/post_list.html"
    context_object_name = "posts"
    paginate_by = 2

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(published_at__isnull= False, status = "active", category__id = self.kwargs["category_id"]).order_by("-published_at")
        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, id=self.kwargs["category_id"])
        context["category"] = category
        return context

    
class PostListByTag(ListView):
    model = Post
    template_name = "global/list/post_list.html"
    context_object_name = "posts"
    paginate_by = 2

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(published_at__isnull= False, status = "active", tag__id = self.kwargs["tag_id"]).order_by("-published_at")
        return query
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = get_object_or_404(Tag, id=self.kwargs["tag_id"])
        context["category"] = Post.tag

        return context
    
class PostDetail(DetailView):
    model = Post
    template_name = "global/post_detail/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(published_at__isnull = False, status= "active")
        return query
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        obj.views_count += 1
        obj.save()

        context["comments"] = Comment.objects.filter(post= obj)
        return context


class CommentView(View):
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST, request.FILES)
        post_id = request.POST["post"]
        if form.is_valid():
            form.save()
            messages.success(
                request, "Successfully commented."
            )
            return redirect("Post-detail", post_id)
        
        post = Post.objects.get(pk = post_id)
        return render(
            request,
            "global/post_detail/post_detail.html",
            {"post":post, "form": form},
        )

class ContactView(TemplateView):
    template_name = "global/contact.html"

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "successfully submitted your query. We will contact soon."
            )
            return redirect("contact")
        else:
            messages.error(
                request, "Cannot Submit your query. Please make sure all field are valid."
            )

            return render(
                request, 
                self.template_name,
                {"form": form},
            )
    

    

class AboutView(TemplateView):
    template_name = "global/about.html"



class PostSearchView(View):
    template_name = "global/list/post_list.html" 

    def get(self, request, *args, **kwargs):
        query = request.GET["query"]
        post_list = Post.objects.filter(
            (Q(title__icontains=query) | Q(content__icontains=query))
            & Q(status = "active")
            & Q(published_at__isnull = False)
        ).order_by("-published_at")

        page = request.GET.get("page", 1)
        paginate_by = 3
        paginator = Paginator(post_list, paginate_by)
        try:
            posts = paginator.page(page)

        except PageNotAnInteger:
            posts = paginator.page(1)

        return render(
            request,
            self.template_name,
            {"posts": posts, "query": query},
        )