from django.db import models
from stdimage.models import StdImageField
import uuid
# Create your models here.

def get_file_path (_instance, filename):
    ext= filename.split(',') [-1]
    filename= f'{uuid.uuid4()}.{ext}'
    return filename


class base(models.Model):
    criados= models.DateTimeField('criação', auto_now_add=True)
    modificado = models.DateField('atualização', auto_now=True)
    ativo = models.BooleanField('ativo?', default=True)
    class Meta:
        abstract = True

class Servico(base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Grafico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foquete'),
    )
    Servico = models.CharField("Serviços", max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone= models.CharField('Incone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Servico'
        verbose_name_plural = 'Servicos'
    def _str_(self):
        return self.Servico

class Cargo(base):
    cargo= models.CharField('cargo', max_length= 100)
    
    class meta:
        verbose_name= 'cargo'
        verbose_name_plural= 'cargos'
    
    def __str__(self) :
        return self.cargo
    
class Equipe(base):
    nome= models.CharField('nome', max_length=100)
    cargo = models.ForeignKey('core.cargo', verbose_name='cargo', on_delete=models.CASCADE)
    bio = models.TextField('bio', max_length=200)
    imagem= StdImageField('imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height':400, 'crop': True}} )
    facebook = models.CharField('facebook', max_length=100, default='#')
    twitter= models.CharField('twitter', max_length=100, default='#')
    instagram= models.CharField('instagram', max_length=100, default='#')
    class meta:
        verbose_name= 'equipe'
        verbose_name_plural= 'equipes'

    def __str__(self):
        return self.nome

class features(base):
    ESCOLHAS= (
        ("lni-rocket", "Foquete"),
        ("lni-laptop-phone", 'notebookEcelular'),
        ("lni-cog","engrenagem"),
        ("lni-leaf", "folha"),
        ("lni-layers", "multi")
    )

    nome= models.CharField('nome', max_length=100)
    bio = models.TextField('bio', max_length=200)
    icone= models.CharField('Icone', max_length=16, choices=ESCOLHAS)
    class meta:
        verbose_name= "feature"
        verbose_name_plural= "features"
    
    def __str__(self):
        return self.nome