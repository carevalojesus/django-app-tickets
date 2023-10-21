# Generated by Django 4.2.6 on 2023-10-21 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_pago_cancelado_alter_evento_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='estado',
            new_name='activo',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='eventp',
            new_name='evento',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='estado',
        ),
        migrations.AddField(
            model_name='ticket',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]