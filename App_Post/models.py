from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    post_image = models.ImageField(upload_to = 'post_image')
    caption = models.CharField(max_length= 264, blank=True,)
    upload_date = models.DateTimeField(auto_now_add=True) 
    update_date = models.DateTimeField(auto_now=True)
    

class Like(models.Model):
    post = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker')
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{} : {}'.format(self.user, self.post)
    