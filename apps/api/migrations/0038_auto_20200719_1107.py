# Generated by Django 2.2.4 on 2020-07-19 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_runapiresultinfo_belong_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='runapiplaninfo',
            name='case_num',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='用例总数'),
        ),
        migrations.AddField(
            model_name='runapiplaninfo',
            name='success_mum',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='成功数'),
        ),
        migrations.AddField(
            model_name='runapiplaninfo',
            name='success_ratio',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='成功率'),
        ),
    ]
