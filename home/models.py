from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import Signal
from django.utils import timezone

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    tel_nomer = models.IntegerField(default=998)
    data = models.DateTimeField(auto_now_add=True)
    profil_image = models.ImageField(upload_to='images/', default='defult_avatar_png', null=True ,blank=True)
    last_activity = models.DateTimeField(default=timezone.now)
    is_online = models.BooleanField(default=False)
    def __str__(self) -> str:
        return str(self.user)

class ProjectModel(models.Model):
    kurs=(
        ('frontend','frontend'),
        ('backend','backend'),
    )
    name = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    gitHub_link = models.CharField(max_length=100,default='defult link')
    project_image = models.ImageField(upload_to='profileimg/',default='defult_img')
    profil = models.ForeignKey(ProfileModel, on_delete=models.SET_NULL, null=True)
    yonalish = models.CharField(max_length=20, choices=kurs, default=None)


    def __str__(self) -> str:
        return str(self.name)
    
class Comment(models.Model):
    ism = models.CharField(max_length=15)
    comment = models.TextField(max_length=150)
    data = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, null=True)
    user_profile = models.ForeignKey(ProfileModel,on_delete=models.CASCADE,blank=True,null=True)
    user_profile_image = models.ImageField(upload_to='comment_user_images/', null=True,blank=True)
    
    def __str__(self) -> str:
        return str(self.ism)



def  create_profil(sender,instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(
            user=instance
        )
    else:
        profilemodel = ProfileModel.objects.get(user=instance)
        profilemodel.email = instance.email
        profilemodel.name = f"{instance.first_name} {instance.last_name}"
        profilemodel.save()
        
Signal.connect(post_save,create_profil,sender=User)

# class SignupForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['first_name','last_name','username','email','password1','password2']


