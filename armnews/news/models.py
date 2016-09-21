# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class News(models.Model):
	title = models.CharField(max_length=250)
	text = models.TextField()
	date = models.DateTimeField()

	def __str__(self):
		return '%s' % (self.title)

	class Meta:
		verbose_name = "Новость"
		verbose_name_plural = "Новости"

	def __unicode__(self):
		return u"%s" % (self.title)

class Photos(models.Model):
	title = models.CharField(max_length=250)
	link = models.CharField(max_length=250)

	def __str__(self):
		return '%s' % (self.title)

	class Meta:
		verbose_name = "Фотография"
		verbose_name_plural = "Фотографии"

	def __unicode__(self):
		return u"%s" % (self.title)

class Comment(models.Model):
    post = models.ForeignKey(News, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

	class Meta:
		verbose_name = "Комментарий"
		verbose_name_plural = "Комментарии"

    def __str__(self):
        return '%s' % (self.text)

    def __unicode__(self):
		return u"%s" % (self.text)