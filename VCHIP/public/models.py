import random

from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save

from hashids import Hashids 	#https://github.com/davidaurelio/hashids-python
hashids = Hashids(salt='VCHIP', min_length=5, alphabet='abcdefghijkmnpqrstuvwxyz23456789')

class CustomText(models.Model):
	tag = models.CharField(max_length=64, null=True, blank=True, unique=True)
	target_name = models.CharField(max_length=128)
	target_extra = models.TextField(null=True, blank=True)

	target_chipid = models.IntegerField(default=random.randint(0,2147483647))

	created_by = models.CharField(max_length=64, null=True, blank=True)

	def __str__(self):
		return self.tag

@receiver(post_save, sender=CustomText)
def tag_update(sender, instance, created, **kwargs):
	if created:
		instance.tag = hashids.encode(instance.id)
		instance.save()