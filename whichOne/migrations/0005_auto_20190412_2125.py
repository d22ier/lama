# Generated by Django 2.2 on 2019-04-12 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whichOne', '0004_auto_20190412_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='alpagaIMG',
            field=models.ImageField(null=True, upload_to='alpaga', verbose_name='Alpaga image :'),
        ),
        migrations.AlterField(
            model_name='question',
            name='lamaIMG',
            field=models.ImageField(null=True, upload_to='lama', verbose_name='Lama image :'),
        ),
    ]
