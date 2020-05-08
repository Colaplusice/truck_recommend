from django.db import models
from django.db.models import Avg


class User(models.Model):
    username = models.CharField(max_length=32, unique=True, verbose_name="账号")
    password = models.CharField(max_length=32, verbose_name="密码")
    phone = models.CharField(max_length=32, verbose_name="手机号码")
    name = models.CharField(max_length=32, verbose_name="名字", unique=True)
    address = models.CharField(max_length=32, verbose_name="地址")
    email = models.EmailField(verbose_name="邮箱")

    class Meta:
        verbose_name_plural = "用户"
        verbose_name = "用户"

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=32, verbose_name="标签", unique=True)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"

    def __str__(self):
        return self.name


class Truck(models.Model):
    title = models.CharField(max_length=64, verbose_name='名称')
    tags = models.ManyToManyField(Tags, verbose_name='货车长度', blank=True)
    collect = models.ManyToManyField(User, verbose_name="收藏者", blank=True)
    weight = models.FloatField(verbose_name='载重')
    sump = models.IntegerField(verbose_name="收藏人数", default=0)
    num = models.IntegerField(verbose_name="浏览量", default=0)
    pic = models.FileField(verbose_name="封面图片", max_length=64, upload_to='truck_cover')

    class Meta:
        verbose_name = "货车"
        verbose_name_plural = "货车"

    def __str__(self):
        return self.title


class Rate(models.Model):
    truck = models.ForeignKey(
        Truck, on_delete=models.CASCADE, blank=True, null=True, verbose_name="货车id"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="用户id",
    )
    mark = models.FloatField(verbose_name="评分")
    create_time = models.DateTimeField(verbose_name="发布时间", auto_now_add=True)

    @property
    def avg_mark(self):
        average = Rate.objects.all().aggregate(Avg('mark'))['mark__avg']
        return average

    class Meta:
        verbose_name = "评分信息"
        verbose_name_plural = verbose_name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    content = models.CharField(max_length=64, verbose_name="内容")
    create_time = models.DateTimeField(auto_now_add=True)
    good = models.IntegerField(verbose_name="点赞", default=0)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, verbose_name="货车")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name


# class Num(models.Model):
#     users = models.IntegerField(verbose_name="用户数量", default=0)
#     trucks = models.IntegerField(verbose_name="货车数量", default=0)
#     comments = models.IntegerField(verbose_name="评论数量", default=0)
#     rates = models.IntegerField(verbose_name="评分汇总", default=0)
#     actions = models.IntegerField(verbose_name="活动汇总", default=0)
#     message_boards = models.IntegerField(verbose_name="留言汇总", default=0)
#
#     class Meta:
#         verbose_name = "数据统计"
#         verbose_name_plural = verbose_name
