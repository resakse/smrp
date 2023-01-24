from django.db import models

modaliti_choices = (
    ('CT','CT-Scan'),
    ('MR','MRI'),
    ('XR','General X-Ray'),
    ('MG','Mammography'),
    ('US','Ultrasound'),
    ('FL','Fluoroscopy'),
    ('XA','Angiography'),
    ('MF','Mobile Fluoro/OT/ERCP'),
    ('HC','Hardcopy'),
    ('DI','Digitize'),
    ('RE','Rad Resources'),
    ('RC','Ref Consult'),
)
# Create your models here.



class Smrp(models.Model):

    name = models.CharField(max_length=50)
    modaliti = models.CharField(choices=modaliti_choices,default='XR', max_length=50)



    class Meta:
        verbose_name_plural = "SMRP"

    def __str__(self):
        return self.name




class Ris(models.Model):

    code = models.CharField(max_length=50,unique=True)
    name = models.CharField(verbose_name='Exam', max_length=150)
    modaliti = models.CharField(choices=modaliti_choices,default='XR', max_length=50)
    smrp = models.ForeignKey(Smrp, on_delete=models.SET_NULL, null=True)
    jxr = models.CharField(max_length=150)
    modified = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural = "RIS"
        ordering = ['modaliti','name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ris_detail", kwargs={"pk": self.pk})
    
    @property
    def mesin(self):
        return str(self.get_modaliti_display())