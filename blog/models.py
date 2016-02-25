from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify 
from django.utils import timezone
from django.contrib.auth.models import User 

# Create your models here.

class Blogger(models.Model):
	user = models.OneToOneField(User, related_name="blogger")
	page = models.SLugField(max_length=110, blank=True)

	def save(self, *args, **kwargs):
		if not self.page:
			user_details = self.user.first_name + self.user.last_name
			self.page = slugify(user_details[:100])
		super(Blogger, self).save(*args, **kwargs)


	def __unicode__(self):
		return self.user.username


class BlogSection(models.Model):
	name = models.CharField(max_length=100)
	page = models.SlugField(max_length=110, blank=True)
	desc = models.TextField(verbose_name="Description")

	def save(self, *args, **kwargs):
		if not self.page:
			self.page = slugify(self.name)
		super(BlogSection, self).save(*args, **kwargs)


class BlogPost(models.Model):
	blogger = models.ForeignKey(Blogger, related_name="blog_posts")
	title = models.CharField(max_length=120)
	body = models.TextField(max_length=1500)
	link = models.SlugField(max_length=130, blank=True)
	date_published = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if not self.link:
			self.link = slugify(self.title)
		super(BlogPost, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s : %s" % (self.blogger.page, self.title)

class Tag(models.Model):
	tag = models.CharField(max_length=50)
	posts = models.ManyToManyField(BlogPost, related_name="tags")


	def __unicode__(self):
		return self.tag 


class Comment(models.Model):
	commenter = models.ForeignKey(User, related_name="comments")
	body = models.TextField(max_length=500)
	comment_date = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(BlogPost, related_name="comments")

	def __unicode__(self):
		return "%s : %s " % (self.commenter.username, self.post.title)




