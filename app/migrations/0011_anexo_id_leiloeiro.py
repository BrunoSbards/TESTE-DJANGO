# Generated by Django 5.1.6 on 2025-02-20 21:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_anexo_id_leiloeiro'),
    ]

    operations = [
        migrations.AddField(
            model_name='anexo',
            name='id_leiloeiro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.leiloeiro'),
            preserve_default=False,
        ),
    ]
