from django.db import models
class Question(models.Model):
    text = (('lama', 'Where is the lama ?'),('alpaga', 'Where is the alpaga ?'))
    question = models.CharField(max_length=200, choices = text, default = 1)
    alpagaIMG = models.ImageField(upload_to = 'alpaga_img/', null = True, verbose_name='Alpaga image :')
    lamaIMG = models.ImageField(upload_to = 'lama_img/', null = True, verbose_name='Lama image :')
    def __str__(self):
        return '['+str(self.id)+'] '+ self.get_question_display()
# Create your models here.
