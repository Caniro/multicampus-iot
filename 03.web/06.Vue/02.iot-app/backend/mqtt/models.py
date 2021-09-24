from django.db import models

class Sensor(models.Model):
    username = models.CharField('사용자명', max_length=20,
                                null=True, blank=True)
    place = models.CharField('설치장소', max_length=30, null=True)
    sensor = models.CharField('센서', max_length=30, null=True)
    value = models.FloatField('센서값')
    regdate = models.DateTimeField('등록일', auto_now_add=True,
                                    null=True, blank=True)

    def __str__(self):
        return f'{self.username}/{self.place}/{self.sensor} {self.value}'
