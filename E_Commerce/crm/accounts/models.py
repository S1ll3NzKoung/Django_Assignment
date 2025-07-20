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
    
class TblMenuDetail(models.Model):
    MenuID = models.ForeignKey(TblSubMenu, on_delete=models.CASCADE, null=True, blank=True)
    Description = RichTextUploadingField(null=True, blank=True)
    def __str__(self):         
        return self.MenuID.MenuName
    
class TblFooter(models.Model):
    FooterName = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.FooterName

class TblSubFooter(models.Model):
    FooterID = models.ForeignKey(TblFooter, on_delete=models.CASCADE, null=True, blank=True)
    SubFooterName = models.CharField(max_length=255, null=True)
    SubFooterDescription = RichTextUploadingField(null=True, blank=True)
    def __str__(self):
        return self.SubFooterName

class TblSlide(models.Model):
    SlideName = models.CharField(max_length=255, null=True)
    SlideImage = models.ImageField(upload_to='pic\img', null=True, blank=True)   

    def __str__(self):
        return self.SlideName 
class TblSubMenu(models.Model):
    MenuID = models.ForeignKey(TblMenu, on_delete=models.CASCADE, null=True, blank=True)
    SubMenuName = models.CharField(max_length=255, null=True)
    SubMenuDescription = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.SubMenuName
    
class Billing_details(models.Model):  
    first_nume = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    companyname = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    Town = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    postcode = models.CharField(max_length=255, null=True)
    Mobile = models.CharField(max_length=255, null=True)
    Email = models.CharField(max_length=255, null=True)
    Order_note = models.CharField(max_length=255, null=True)
def __str__(self):
        return self.first_name

class Order(models.Model):
     Customer = models.CharField(max_length=255, null=True)
     TotalCost = models.DecimalField(max_digits=10, decimal_places=2)
     Reciept = models.CharField(max_length=255, null=True)
     order_date = models.DateField()
def __str__(self):
        return self.Customer

class TblOrderDetail(models.Model):
     OrderID = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
     Price = models.DecimalField(max_digits=10, decimal_places=2)
     QUantity = models.DecimalField(max_digits=10, decimal_places=2)
def __str__(self):
        return self.OrderID
class TblCustomer(models.Model):
     CustomerName = models.CharField(max_length=255, null=True)
     Phone = models.CharField(max_length=255, null=True)
     Email = models.CharField(max_length=255, null=True)
     Telegram = models.CharField(max_length=255, null=True)
     Address = models.CharField(max_length=255, null=True)
     Username = models.CharField(max_length=255, null=True)
     Password = models.CharField(max_length=255, null=True)    
def __str__(self):
        return self.Username