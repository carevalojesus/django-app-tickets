# Generated by Django 4.2.6 on 2023-10-20 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(blank=True, max_length=50, null=True)),
                ('celular', models.CharField(max_length=9)),
                ('creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_evento', models.CharField(max_length=255)),
                ('fecha_hora', models.DateTimeField()),
                ('lugar', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='eventos')),
                ('estado', models.CharField(max_length=50, null=True)),
                ('capacidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('codigo_unico', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.cliente')),
                ('eventp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.evento')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('metodo_pago', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('completado', 'Completado'), ('cancelado', 'Cancelado'), ('reembolsado', 'Reembolsado')], max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.cliente')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.ticket')),
            ],
        ),
    ]