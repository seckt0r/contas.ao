# Generated by Django 3.0.4 on 2020-03-07 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transacoes', '0008_auto_20200307_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transacao',
            old_name='id_tipo',
            new_name='tipo',
        ),
    ]
