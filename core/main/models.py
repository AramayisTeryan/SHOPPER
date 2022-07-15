from django.db import models

# Create your models here.

class HomeSite(models.Model):
    name = models.CharField('HomeSite name', max_length=100, null=True)
    about = models.TextField('HomeSite about', null=True)
    contact = models.CharField('HomeSite contact', max_length=30, null=True)
    video = models.TextField('Homesite video link', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeSite'
        verbose_name_plural = 'HomeSites'


class AboutWeb1(models.Model):
    name = models.CharField('AboutWeb1 name', max_length=100, null=True)
    about = models.TextField('AboutWeb1', null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'AboutWeb1'
        verbose_name_plural = 'AboutWebs1'


class FashionBlog(models.Model):
    name1 = models.CharField('FashionBlog name1', max_length=100)
    name2 = models.CharField('FashionBlog name2', max_length=100)
    img = models.ImageField('FashionBlog image', upload_to='media')
    about1 = models.TextField('FashionBlog')
    about2 = models.TextField('FashionBlog')

    def __str_(self):
        return self.name1

    class Meta:
        verbose_name = 'FashionBlog'
        verbose_name_plural = 'FashionBlogs' 


class WorkBlog(models.Model):
    name1 = models.CharField('WorkBlog name1', max_length=100)
    name2 = models.CharField('WorkBlog name2', max_length=100)
    img = models.ImageField('WorkBlog image', upload_to='media')
    about = models.TextField('WorkBlog')   

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'WorkBlog'
        verbose_name_plural = 'WorkBlogs'


