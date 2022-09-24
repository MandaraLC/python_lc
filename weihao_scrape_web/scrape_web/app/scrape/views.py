import time

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from django_filters.rest_framework import DjangoFilterBackend

from .filters import ResultFilters
from .models import ScrapeTask, ScrapeConfigAccount, ScrapeResult
from .serializers import ScrapeTaskSerializer, ScrapeAccountSerializer, ScrapeResultSerializer

# Create your views here.


class ScrapeTaskViewSets(ModelViewSet):
    """
    爬虫任务接口

    list:
    爬虫任务列表

    retrieve:
    爬虫任务详细信息

    create:
    新建爬虫信息

    update:
    修改爬虫信息

    delete:
    删除爬虫信息
    """
    queryset = ScrapeTask.objects.all()
    serializer_class = ScrapeTaskSerializer


class ScrapeAccountViewSets(ModelViewSet):
    """
    任务账户接口

    list:
    任务账户列表

    retrieve:
    任务账户详细信息

    create:
    新建任务账户

    update:
    修改任务账户

    delete:
    删除任务账户
    """
    queryset = ScrapeConfigAccount.objects.all()
    serializer_class = ScrapeAccountSerializer


class ScrapeResultViewSets(GenericViewSet,
                           ListModelMixin,
                           RetrieveModelMixin):
    """
    任务账户接口

    list:
    任务账户列表

    retrieve:
    任务账户详细信息
    """
    queryset = ScrapeResult.objects.filter(status=0).order_by('-batch')
    serializer_class = ScrapeResultSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ResultFilters

    def filter_queryset(self, queryset):
        queryset = super(ScrapeResultViewSets, self).filter_queryset(queryset)
        pass_time = int(time.time()) - 3600
        return queryset.filter(batch__gte=pass_time)



