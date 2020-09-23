# Generated by Django 2.2 on 2020-04-22 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('setting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField()),
                ('content', models.CharField(max_length=512)),
                ('task_type', models.CharField(default='html', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(verbose_name='任务ID')),
                ('task_name', models.CharField(max_length=100, verbose_name='任务名称')),
                ('last_run', models.DateTimeField(auto_now=True, verbose_name='上次运行时间')),
                ('last_status', models.CharField(default='创建任务成功', max_length=100, verbose_name='上次运行结果')),
                ('task_status', models.IntegerField(choices=[(0, 'run'), (1, 'stop')], default=0, verbose_name='任务状态')),
                ('task_type', models.CharField(default='html', max_length=100, verbose_name='任务类型')),
            ],
            options={
                'verbose_name': '任务状态',
                'verbose_name_plural': '任务状态',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='任务名称')),
                ('url', models.CharField(max_length=500, verbose_name='监控网址')),
                ('selector_type', models.IntegerField(choices=[(0, 'Xpath'), (1, 'Css selector'), (2, 'JsonPath')], default='Xpath', verbose_name='元素选择器类型')),
                ('selector', models.CharField(max_length=128, verbose_name='元素选择器')),
                ('is_chrome', models.IntegerField(choices=[(0, 'no'), (1, 'yes'), (2, 'firefox')], default='no', verbose_name='是否使用无头浏览器')),
                ('frequency', models.IntegerField(default=5, verbose_name='频率(分钟)  ')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('regular_expression', models.CharField(blank=True, help_text='使用正则表达式进一步提取信息，可以留空', max_length=128, verbose_name='正则表达式')),
                ('rule', models.CharField(blank=True, help_text='规则写法参考文档，留空则只简单监控内容变化', max_length=128, verbose_name='监控规则')),
                ('headers', models.CharField(blank=True, help_text='自定义请求头，如可以设置cookie获取登录后才能查看的页面', max_length=1024, verbose_name='自定义请求头')),
                ('notification', models.ManyToManyField(to='setting.Notification', verbose_name='通知方式')),
            ],
            options={
                'verbose_name': '网页监控',
                'verbose_name_plural': '网页监控管理',
            },
        ),
        migrations.CreateModel(
            name='RSSTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='任务名称')),
                ('url', models.CharField(max_length=500, verbose_name='RSS地址')),
                ('frequency', models.IntegerField(default=5, verbose_name='频率(分钟)')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('notification', models.ManyToManyField(to='setting.Notification', verbose_name='通知方式')),
            ],
            options={
                'verbose_name': 'RSS监控',
                'verbose_name_plural': 'RSS监控管理',
            },
        ),
    ]
