from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    site_header = '安格订舱管理系统'
    site_title = '安格订舱管理系统'


admin_site = MyAdminSite(name='myadmin')
