from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
RATING_CHOICES = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)

def get_member_image_uploadpath(instance, filename):
    ext = filename.split('.')[-1]
    full_name = [
        character for character in instance.full_name if character.isalnum()]
    full_name = "".join(full_name)

    return f'uploads/about/members/{instance.full_name}/{instance.full_name}_image.{ext}'

def get_testimonial_image_uploadpath(instance, filename):
    ext = filename.split('.')
    full_name = [
        character for character in instance.full_name if character.isalnum()]
    full_name = "".join(full_name)

    return f'uploads/about/testimonials/{instance.full_name}/{instance.full_name}.{ext}'


class Member(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Full Name')
    image = models.ImageField(upload_to=get_member_image_uploadpath, blank=True, null=True, verbose_name='Image')
    position = models.CharField(max_length=50)
    contact_number_regex = RegexValidator(regex=r'([0-9])', message="")
    contact_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Mobile Number')
    facebook = models.CharField(max_length=200, blank=True, null=True, verbose_name='Facebook Profile Link')
    twitter = models.CharField(max_length=200, blank=True, null=True, verbose_name='Twitter Profile Link')
    linkedin = models.CharField(max_length=200, blank=True, null=True, verbose_name='LinkedIn Profile Link')

    def __str__(self):
        return str(self.full_name)
        
class Testimonials(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Full Name')
    image = models.ImageField(upload_to=get_testimonial_image_uploadpath, blank=True, null=True, verbose_name='Image')
    organization = models.CharField(max_length=100, verbose_name='Reviewer Organization Name')
    testimonial = models.TextField()
    rating = models.CharField(choices=RATING_CHOICES, max_length=10)
    created_at = models.DateField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return str(self.full_name)