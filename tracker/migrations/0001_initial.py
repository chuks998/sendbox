# Generated by Django 4.0.2 on 2022-03-18 00:06

from django.db import migrations, models
import django.utils.timezone
import tracker.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Package_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, default=tracker.models.id_genarator, max_length=11, null=True, unique=True)),
                ('order_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('order_image', models.ImageField(default='image/homepage.svg', upload_to='image')),
                ('reciver_name', models.CharField(max_length=50)),
                ('content', models.CharField(default='iphone12(black), louis vuttion designer bag, sealed 700 x 700 envelop', max_length=100)),
                ('quantity', models.CharField(default='1', max_length=20)),
                ('weight', models.CharField(default='30g', max_length=20)),
                ('status', models.CharField(choices=[('delayed', 'delayed'), ('active', 'active'), ('waiting comfirmation', 'waiting comfirmation'), ('pending', 'pending')], default=3, max_length=21)),
                ('message', models.CharField(default='This Parcel Is On Transit To Manilla, Phillipines.', max_length=500)),
            ],
        ),
    ]
