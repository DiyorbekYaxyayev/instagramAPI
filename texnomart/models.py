from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(max_length=129, unique=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.SmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    discount = models.SmallIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images')


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


# class Comment(models.Model):
#     post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     rating = models.IntegerField(choices=((1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')), default=1)
#     likes = models.ManyToManyField(User, related_name='liked_comments')
#     dislikes = models.ManyToManyField(User, related_name='disliked_comments')

#     def __str__(self):
#         return f"{self.text} by {self.post}





class Comment(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=((1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')), default=1)

    def __str__(self):
        return f"{self.text} by {self.post}"
    