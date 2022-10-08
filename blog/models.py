from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField(blank=True,null = True)
    date = models.DateTimeField(auto_now_add=True)
    code = models.TextField(max_length = 5000,null = True,blank = True)
    output = models.TextField(max_length = 1000,null=True,blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self) -> str:
        return self.title

class comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=20)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self) -> str:
        return 'Comment {} by {}'.format(self.body,self.name)
