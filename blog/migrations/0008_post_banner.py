# Generated by Django 2.2.3 on 2019-08-12 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, help_text='A banner image for the post', null=True, upload_to=''),
        ),
    ]
