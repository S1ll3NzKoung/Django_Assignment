from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class TblInfo(models.Model):
    Address = models.CharField(max_length=255, null=True)
    Email = models.EmailField(max_length=255, null=True)
    Logo = models.ImageField(upload_to='staticE\img', null=True, blank=True)
    SlideInfo = models.TextField(null=True, blank=True)


class TblMenu(models.Model):
    MenuName = models.CharField(max_length=255, null=True)
    MenuDescription = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.MenuName
    
class TblSubMenu(models.Model):
    MenuID = models.ForeignKey(TblMenu, on_delete=models.CASCADE, null=True, blank=True)
    SubMenuName = models.CharField(max_length=255, null=True)
    SubMenuDescription = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.SubMenuName