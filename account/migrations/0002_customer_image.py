# Generated by Django 4.0.1 on 2022-06-28 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(default='defaultprofilepic.jpg', upload_to='profiles_pics'),
        ),
    ]
