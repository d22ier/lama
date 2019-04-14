# Generated by Django 2.2 on 2019-04-12 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whichOne', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='question',
            name='alpagaIMG',
            field=models.ImageField(blank=True, null=True, upload_to='alpaga'),
        ),
        migrations.AddField(
            model_name='question',
            name='lamaIMG',
            field=models.ImageField(blank=True, null=True, upload_to='lama'),
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.CharField(choices=[('Where is the lama ?', 'lama'), ('Where is the alpaga ?', 'alpaga')], default=1, max_length=200),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]