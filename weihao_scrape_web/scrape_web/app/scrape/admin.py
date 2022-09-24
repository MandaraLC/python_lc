from django.contrib import admin

from .models import ScrapeTask, ScrapeConfigAccount
from utils.admin import admin_site

# Register your models here.


class ScrapeTaskAdmin(admin.ModelAdmin):
    list_display = ('scrape_task_id', 'shipping_company', 'port_city', 'final_city', 'container_type', 'container_num')
    list_filter = ('shipping_company', 'container_type')
    search_fields = ('shipping_company', 'port_city', 'final_city', 'container_type')

    fieldsets = (
        ('船运公司', {
            'fields': ('shipping_company', )
        }),
        ('配置参数', {
            'fields': ('port_city', 'final_city', ('early_etd', 'late_etd'), 'container_type', 'commodity',
                       'container_num', 'weight', ('min_price', 'max_price'))
        })
    )
    exclude = ('create_time', 'update_time')


class ScrapeConfigAccountAdmin(admin.ModelAdmin):
    list_display = ('scrape_account_id', 'shipping_company', 'account')
    list_filter = ('shipping_company',)
    search_fields = ('shipping_company', 'account')

    fieldsets = (
        ('船运公司', {
            'fields': ('shipping_company',)
        }),
        ('账号配置', {
            'fields': ('account', 'password')
        })
    )
    exclude = ('create_time', 'update_time')


# class ScrapeResultAdmin(admin.ModelAdmin):
#     list_display = ('scrape_result_id', 'shipping_company', 'port_city', 'final_city', 'container_type', 'container_num',
#                     'status')
#     list_filter = ('shipping_company', 'status', 'container_type')
#     search_fields = ('shipping_company', 'port_city', 'final_city', 'container_type')
#
#     fieldsets = (
#         ('船运公司', {
#             'fields': ('shipping_company',)
#         }),
#         ('结果', {
#             'fields': ('port_city', 'final_city', 'status', 'container_id', 'transport_name', 'etd', 'eta', 'price',
#                        'shipping_time', 'container_type', 'commodity', 'container_num', 'weight')
#         })
#     )
#     exclude = ('create_time', 'update_time')


admin_site.register(ScrapeTask, ScrapeTaskAdmin)
admin_site.register(ScrapeConfigAccount, ScrapeConfigAccountAdmin)
# admin.site.register(ScrapeResult, ScrapeResultAdmin)


