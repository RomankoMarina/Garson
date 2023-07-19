from django.db import models

class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True, null=True,blank=True)
    update_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        abstract = True
    def __str__(self):
        return "%s.%s" % (self.pk, self.name) if hasattr(self,'name') else super().__str__()
