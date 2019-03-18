from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models

User = get_user_model()


@receiver(post_save, sender=models.ExamSheet)
def create_exam_sheet_for_student(sender, instance, **kwargs):
    """Signal to create multiple exam sheets"""
    if instance.is_completed:
        print('hej')
    else:
        pass
