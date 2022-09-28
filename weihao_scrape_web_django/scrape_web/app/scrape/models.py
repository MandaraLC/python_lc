from django.db import models

from utils.models import BaseModel


# Create your models here.


class ScrapeTask(BaseModel):
    """
    爬虫任务
    """
    SHIPPING_COMPANY_CHOICES = (
        (1, '马士基Maersk'),
        (2, '中远海COSOC'),
        (3, '东方海外OOCL')
    )

    CONTAINER_TYPE_CHOICES = (
        (1, '20GP/20 Dry Standard'),
        (2, '40GP/40 Dry Standard'),
        (3, '40HQ/40 Dry High')
    )

    scrape_task_id = models.BigAutoField(primary_key=True, verbose_name='爬虫任务id', help_text='爬虫任务id')
    shipping_company = models.SmallIntegerField(choices=SHIPPING_COMPANY_CHOICES, verbose_name='船运公司',
                                                help_text='船运公司: (1: 马士基Maersk, 2: 中远海COSOC, 3: 东方海外OOCL)')
    port_city = models.CharField(max_length=100, verbose_name='起运港', help_text='起运港')
    final_city = models.CharField(max_length=100, verbose_name='目的港', help_text='目的港')
    early_etd = models.DateTimeField(verbose_name='最早预计开航时间', help_text='最早预计开航时间')
    late_etd = models.DateTimeField(verbose_name='最晚预计开航时间', help_text='最晚预计开航时间')
    container_type = models.SmallIntegerField(choices=CONTAINER_TYPE_CHOICES, verbose_name='集装箱类型',
                                              help_text='集装箱类型: (1: 20GP/20 Dry Standard, 2: 40GP/40 Dry Standard, 3: 40HQ/40 Dry High)')
    commodity = models.CharField(max_length=100, null=True, blank=True, verbose_name='物品名称', help_text='物品名称')
    container_num = models.PositiveIntegerField(default=1, verbose_name='集装箱个数', help_text='集装箱个数')
    weight = models.PositiveIntegerField(null=True, blank=True, verbose_name='集装箱重量', help_text='集装箱重量')
    min_price = models.PositiveIntegerField(verbose_name='最低价格', help_text='最低价格')
    max_price = models.PositiveIntegerField(verbose_name='最高价格', help_text='最高价格')

    class Meta:
        db_table = 'scrape_task'
        verbose_name = '侦测航线'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.shipping_company}: {self.port_city} - {self.final_city}'


class ScrapeResult(BaseModel):
    SHIPPING_COMPANY_CHOICES = (
        (1, '马士基Maersk'),
        (2, '中远海COSOC'),
        (3, '东方海外OOCL')
    )

    CONTAINER_TYPE_CHOICES = (
        (1, '20GP/20 Dry Standard'),
        (2, '40GP/40 Dry Standard'),
        (3, '40HQ/40 Dry High')
    )

    RESULT_STATUS_CHOICES = (
        (-1, '下单失败'),
        (0, '未下单'),
        (1, '已下单')
    )

    scrape_result_id = models.BigAutoField(primary_key=True, verbose_name='爬虫任务结果id', help_text='爬虫任务结果id')
    status = models.SmallIntegerField(null=True, blank=True, choices=RESULT_STATUS_CHOICES, verbose_name='下单状态',
                                      help_text='下单状态')
    container_id = models.CharField(null=True, blank=True, max_length=100, verbose_name='集装箱id', help_text='集装箱id')
    shipping_company = models.SmallIntegerField(choices=SHIPPING_COMPANY_CHOICES, verbose_name='船运公司',
                                                help_text='船运公司: (1: 马士基Maersk, 2: 中远海COSOC, 3: 东方海外OOCL)')
    port_city = models.CharField(max_length=100, verbose_name='起运港', help_text='起运港')
    final_city = models.CharField(max_length=100, verbose_name='目的港', help_text='目的港')
    etd = models.DateTimeField(null=True, blank=True, verbose_name='开航时间', help_text='开航时间')
    eta = models.DateTimeField(null=True, blank=True, verbose_name='到达时间', help_text='到达时间')
    shipping_time = models.IntegerField(null=True, blank=True, verbose_name='航程时间', help_text='航程时间')
    container_type = models.SmallIntegerField(choices=CONTAINER_TYPE_CHOICES, verbose_name='集装箱类型',
                                              help_text='集装箱类型: (1: 20GP/20 Dry Standard, 2: 40GP/40 Dry Standard, 3: 40HQ/40 Dry High)')
    commodity = models.CharField(max_length=100, null=True, blank=True, verbose_name='物品名称', help_text='物品名称')
    container_num = models.PositiveIntegerField(default=1, verbose_name='集装箱个数', help_text='集装箱个数')
    weight = models.PositiveIntegerField(null=True, blank=True, verbose_name='集装箱重量', help_text='集装箱重量')
    price = models.PositiveIntegerField(null=True, blank=True, verbose_name='价格', help_text='价格')
    transport_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='航线名称', help_text='航线名称')
    finger_print = models.CharField(max_length=50, null=True, blank=True, verbose_name='去重指纹', help_text='去重指纹')
    batch = models.IntegerField(verbose_name='批次', help_text='批次')

    class Meta:
        db_table = 'scrape_result'
        verbose_name = '爬虫任务结果表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.shipping_company}: {self.port_city} - {self.final_city} - {self.scrape_result_id}'


class ScrapeConfigAccount(BaseModel):
    SHIPPING_COMPANY_CHOICES = (
        (1, '马士基Maersk'),
        (2, '中远海COSOC'),
        (3, '东方海外OOCL')
    )

    scrape_account_id = models.BigAutoField(primary_key=True, verbose_name='爬虫账号配置id', help_text='爬虫账号配置id')
    shipping_company = models.SmallIntegerField(choices=SHIPPING_COMPANY_CHOICES, verbose_name='船运公司',
                                                help_text='船运公司: (1: 马士基Maersk, 2: 中远海COSOC, 3: 东方海外OOCL)')
    account = models.CharField(max_length=50, verbose_name='账号', help_text='账号')
    password = models.CharField(max_length=50, verbose_name='密码', help_text='密码')

    class Meta:
        db_table = 'scrape_config_account'
        verbose_name = '船运账号配置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.shipping_company} - {self.account}'
