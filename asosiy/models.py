from django.db import models

class Club(models.Model):
    nom = models.CharField(max_length=30)
    logo = models.FileField()
    davlat = models.CharField(max_length=60)
    prezident = models.CharField(max_length=30,null=True,blank=True)
    murabbiy = models.CharField(max_length=30,null=True,blank=30)
    yil = models.PositiveIntegerField(null=True,blank=True)
    qimmat_tr = models.PositiveIntegerField(null=True,blank=True)
    qimmat_sotuv = models.PositiveIntegerField(null=True,blank=True)

    def __str__(self):
        return self.nom

p = (
    ("Darvozabon","Darvozabon"),
    ("Himoyachi","Himoyachi"),
    ("Hujumchi","Hujumchi"),
    ("Yarim Himoyachi","Yarim Himoyachi"),
)
class Player(models.Model):
    ism = models.CharField(max_length=30)
    pozitsiya = models.CharField(max_length=230,choices=p)
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    narx = models.PositiveIntegerField()
    davlat = models.CharField(max_length=30)
    t_yil = models.DateField()

    def __str__(self):
        return self.ism

class Transfer(models.Model):
    player = models.ForeignKey(Player,on_delete=models.CASCADE)
    eski_club = models.ForeignKey(Club,on_delete=models.CASCADE,related_name="sotuvlari")
    yangi_club = models.ForeignKey(Club,on_delete=models.CASCADE)
    narx = models.PositiveIntegerField()
    tax_narx = models.PositiveIntegerField(null=True,blank=True)
    mavsum = models.CharField(max_length=30)



class Hozirgi_mavsum(models.Model):
    h_mavsum = models.CharField(max_length=30)

