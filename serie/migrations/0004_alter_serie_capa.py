# Generated by Django 3.2.17 on 2023-02-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serie', '0003_alter_serie_capa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='capa',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
