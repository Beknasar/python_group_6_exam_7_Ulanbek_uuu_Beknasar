from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.TextField(max_length=500, verbose_name='Опрос')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания опроса')

    def __str__(self):
        return f'{self.pk}. {self.question}'

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

class Choice(models.Model):
    text = models.TextField(max_length=500, verbose_name='Текст варианта')
    poll = models.ForeignKey('webapp.Poll', related_name='choices', on_delete=models.CASCADE, verbose_name='Опрос' )

    def __str__(self):
        return '{} {}'.format(self.pk, self.text)


    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'