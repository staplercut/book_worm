# Generated by Django 2.0.2 on 2018-02-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20180226_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, to='books.Author'),
        ),
    ]
