# Generated by Django 2.2 on 2019-04-12 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whichOne', '0007_auto_20190412_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='alpagaIMG',
            field=models.ImageField(null=True, upload_to='whichOne/alpaga_img/', verbose_name='Alpaga image :'),
        ),
        migrations.AlterField(
            model_name='question',
            name='lamaIMG',
            field=models.ImageField(null=True, upload_to='whichOne/lama_img/', verbose_name='Lama image :'),
        ),
    ]
