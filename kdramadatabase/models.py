from django.db import models

# Create your models here.

class BroadcastChannel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class KDrama(models.Model):
    name_eng = models.CharField(max_length=200)
    name_kor = models.CharField(max_length=200)
    broadcast_ch = models.ForeignKey(BroadcastChannel, on_delete=models.CASCADE)
    release_date = models.DateTimeField("First Episode Release Date")
    rating = models.DecimalField(decimal_places=1, max_digits=3)
    pub_date = models.DateTimeField("Date Published")

    def __str__(self):
        return self.name_eng

