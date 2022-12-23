from django.core.files import File
from PIL import Image
from io import BytesIO
from django.db import models


class BlogMainTheme(models.Model):
    main_theme = models.CharField(choices='', max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        ordering = ('main_theme',)

    def __str__(self):
        return self.main_theme

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Blog(models.Model):
    theme = models.ForeignKey(BlogMainTheme, related_name='blogs', on_delete=models.CASCADE)
    title = models.CharField('Blog Title', max_length=999)
    text = models.TextField('Blog Text')

    blog_image = models.ImageField(upload_to='Blog Images/%Y/%m/%d', blank=True, null=True)
    blog_thumbnail = models.ImageField(upload_to='Blog Thumbnails/%Y/%m/%d', blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title

    def get_blog_image(self):
        if self.blog_image:
            return 'http://127.0.0.1:8000' + self.blog_image.url
        return ''

    def get_blog_thumbnail(self):
        if self.blog_thumbnail:
            return 'http://127.0.0.1:8000' + self.blog_thumbnail.url

        if self.blog_image:
            self.blog_thumbnail = self.make_blog_thumbnail(self.blog_image)
            self.save()

            return 'http://127.0.0.1:8000' + self.blog_thumbnail.url
        return ''

    def make_blog_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=100)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail



