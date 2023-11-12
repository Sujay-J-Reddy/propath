from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete


class Franchisee(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Admin(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

@receiver(post_save, sender=Admin)
def create_user_for_admin(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create(username=instance.username)
        user.set_password(instance.password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        instance.user = user
        instance.save()

@receiver(post_save, sender=Franchisee)
def create_user_for_franchisee(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create(username=instance.username)
        user.set_password(instance.password)
        user.save()

        instance.user = user
        instance.save()

# @receiver(post_delete, sender=Franchisee)
# @receiver(post_delete, sender=Admin)
# def delete_user(sender, instance, **kwargs):
#     if instance.user:
#         instance.user.delete()