from django.db import models

class User(models.Model):
    name = models.CharField('Nazwa Użytkownika', max_length=150)
    email = models.EmailField('Email')
    password = models.CharField('Hasł', upload_to='icons',
                              blank=True)

    class Meta:
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownicy"

    def __unicode__(self):
        return self.name