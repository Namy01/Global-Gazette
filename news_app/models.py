from django.db import models

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
class Tag(TimeStamp):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category(TimeStamp):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Post(TimeStamp):
    STATUS =[
        ("active", "Active"),
        ("in_active", "Inactive"),
    ]

    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/%Y/%m/%d", blank=False)
    status = models.CharField(max_length=20,choices=STATUS,default="active")
    published_at = models.DateTimeField(null=True, blank=True)
    views_count = models.PositiveBigIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Comment(TimeStamp):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    comment = models.TextField()
    profile = models.ImageField(upload_to="images/%Y/%m/%d", default="")
    name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.email} | {self.comment[:7]}"


class Contact(TimeStamp):
    message = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.name

