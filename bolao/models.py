from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):
    usuario = models.OneToOneField(User)
    descricao = models.CharField(max_length=100, default='')
    cidade = models.CharField(max_length=100, default='')
    celular = models.IntegerField(default=0)

    def __str__(self):
        return "%s" %(self.usuario)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(usuario=kwargs['instance'])
post_save.connect(create_profile, sender=User)

class selecao(models.Model):
    class Meta:
        verbose_name_plural = "Selecoes"

    def __str__(self):
        return "%s" % (self.nome)
    sigla = models.CharField(max_length=3)
    nome = models.CharField(max_length=30)


class Partida(models.Model):
    local = models.CharField(max_length=50, default='')
    time1 = models.ForeignKey(selecao, related_name='time1')
    time2 = models.ForeignKey(selecao, related_name='time2')
    placar_time1 = models.IntegerField(blank=True, null=True)
    placar_time2 = models.IntegerField(blank=True, null=True)

    def __str__(self):
#       return self.time1.sigla + ' VS ' + self.time2.sigla
        return "%s %s VS  %s %s " %(self.time1.sigla, self.time1, self.time2.sigla, self.time2)


class aposta(models.Model):
    usuario = models.CharField(max_length=100);
    valor = models.IntegerField()
    aposta_partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    gols_time1 = models.IntegerField()
    gols_time2 = models.IntegerField()

    def __str__(self):
        return "%s - %i x %i " %(self.aposta_partida, self.gols_time1, self.gols_time2)
