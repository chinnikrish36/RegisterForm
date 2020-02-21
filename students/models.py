from django.db import models

#Student also get login credentials
from django.contrib.auth.models import User
#url for reverse mapping
from django.urls import reverse

#Declares class of the student
ClASS_STANDARD=(
    ('V', 'sixth'),
    ('VII', 'seventh'),
    ('VIII', 'eight'),
    ('XI', 'ninth'),
    ('X', 'tenth')
)
#gender of the student
GENDER=(
    ('Male','MALE'),
    ('Female','FEMALE')


)

#studentregister model class
class StudentRegister(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Stu_id=models.IntegerField(primary_key=True)
    First_name=models.CharField(max_length=20)
    Middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender=models.CharField(choices=GENDER,max_length=6)
    Father_name=models.CharField(max_length=20)
    Standard=models.CharField(choices=ClASS_STANDARD,max_length=5)


    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('Stu_edit', kwargs={'pk': self.pk})