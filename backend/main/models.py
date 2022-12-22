from django.core.files import File
from PIL import Image
from io import BytesIO
from django.db import models
from . import utils


class Team(models.Model):
    name = models.CharField('Team Name', max_length=255)
    location = models.CharField('Team Location', max_length=255)
    description = models.TextField('Team Description')
    slug = models.SlugField('Team Slug', max_length=255)

    image = models.ImageField('Team Image', upload_to='Team Images/%Y/%m/%d', blank=True, null=True)
    thumbnail = models.ImageField('Team Thumbnail', upload_to='Team Thumbnails/%Y/%m/%d', blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def get_team_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_team_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url

        if self.image:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()

            return 'http://127.0.0.1:8000' + self.thumbnail.url
        return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=100)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class Player(models.Model):
    team = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE)

    first_name = models.CharField('Player Name', max_length=255)
    last_name = models.CharField('Player Last Name', max_length=255)
    patronymic = models.CharField('Player Patronymic', max_length=255)

    birthday = models.CharField(max_length=10, default='DD.MM.YYYY')

    position = models.CharField('Player Position', max_length=255)

    matches = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()
    status = models.CharField('Player Status', max_length=255, default='Available')

    image = models.ImageField('Player Image', upload_to='Players Images/%Y/%m/%d', null=True, blank=True)
    thumbnail = models.ImageField('Player Thumbnail', upload_to='Players Thumbnails/%Y/%m/%d', null=True, blank=True)

    slug = models.SlugField(max_length=255)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.get_player_full_name()

    def get_player_full_name(self):
        return f'{self.first_name} {self.patronymic} {self.last_name}'

    def get_player_age(self):
        return utils.count_player_age(self.birthday)

    def get_absolute_url(self):
        return f'/{self.team.slug}/{self.slug}/'

    def get_player_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_player_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url

        if self.image:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()

            return 'http://127.0.0.1:8000' + self.thumbnail.url
        return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=100)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
