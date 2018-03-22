# Generated by Django 2.0.2 on 2018-03-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180322_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='pics/profile_pics/None/blank.png', upload_to='pics/profile_pics/'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]