from django.db import models

# Create your models here.

# class test(models.Model):
#     Float = models.FloatField()
#     Int = models.IntegerField()
#     Char = models.CharField()
#
#
# class A(models.Model):
#     #一对一
#     onetoone = models.OneToOneField(test)
#
# class B(models.Model):
#     #一对多
#     foreign = models.ForeignKey(A)
#
# class C(models.Model):
#     manytomany = models.ManyToManyField(B)

class AddressInfo(models.Model):
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name="地址")
    pid = models.ForeignKey('self', null=True, blank=True, verbose_name="自关联")
    # pid = models.ForeignKey('AddressInfo', null=True, blank=True, verbose_name="自关联")

    def __str__(self):
        return self.address

#字段参数：
#1.所有字段都有的参数

#2.

