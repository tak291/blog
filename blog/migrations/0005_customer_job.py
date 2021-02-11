# Generated by Django 3.1.5 on 2021-02-10 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210210_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, '    open'), (2, 'pending'), (3, 'closed')], default=1)),
                ('customer', models.CharField(default=1, max_length=200)),
                ('Worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.worker')),
            ],
        ),
    ]