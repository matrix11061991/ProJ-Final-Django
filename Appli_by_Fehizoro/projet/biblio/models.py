from audioop import reverse
from PyPDF2 import PdfFileReader
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()
    
    class Meta:
        verbose_name = "Catégorie"
        
    def __str__(self):
        return self.name
    
class Livre (models.Model):
    titre = models.CharField(max_length=100,verbose_name='Titre')
    nbPages = models.IntegerField(verbose_name='Nombre de Page')
    image = models.ImageField(upload_to='livres/')
    slug = models.SlugField(blank=True,verbose_name='Slug',default=slugify(f"{titre}"))
    file = models.FileField(upload_to='livres/')
    
    
    def extraire_texte(self):
        with self.file.open(mode='rb') as pdf_file:
            pdf_reader = PdfFileReader(pdf_file)
            texte = ''
            for page in range(pdf_reader.getNumPages()):
                texte += pdf_reader.getPage(page).extractText()
            return texte
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
            
        super().save(*args,**kwargs)
    
    class Meta:
        verbose_name = "Livre"
        
    def __str__(self):
        return self.titre
        
    #def get_absolute_url(self):
        #return reverse('', kwargs={'pk': self.pk})