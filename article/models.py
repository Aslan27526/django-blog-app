from django.db import models 
from ckeditor.fields import RichTextField
# Create your models here.
class Article(models.Model):
    author=models.ForeignKey("auth.user",on_delete=models.CASCADE,verbose_name='Yazıçı')
    title=models.CharField(max_length=50,verbose_name='Başlıq')
    content=RichTextField()
    created_data=models.DateTimeField(auto_now_add=True,verbose_name="Yaradılma tarixi")
    article_image = models.FileField(blank=True,null=True,verbose_name='Fayl yukleyin')
    #title ni gosterir
    def __str__(self):
        return self.title
    class Meta:
        #Django ordering
        ordering=['-created_data']
class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Məqalə",related_name="comments")
    comment_author=models.CharField(max_length=50,verbose_name="Ad")    
    comment_content=models.CharField(max_length=200,verbose_name="Rəy")
    comment_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        #Django ordering
        ordering=['-comment_date']