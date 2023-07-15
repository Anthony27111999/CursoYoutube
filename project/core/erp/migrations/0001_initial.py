# Generated by Django 4.2.3 on 2023-07-15 08:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Nombres')),
                ('surnames', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('ci', models.CharField(max_length=8, verbose_name='C.I')),
                ('birthday', models.DateField(default=datetime.datetime.now, verbose_name='Decha de nacimiento')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='Direccion')),
                ('sexo', models.CharField(choices=[('man', 'male'), ('woman', 'famele')], default='male', max_length=10, verbose_name='Sexo')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'CLientes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime(2023, 7, 15, 5, 5, 34, 428353))),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.client')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d')),
                ('pvp', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.category')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DetSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cant', models.IntegerField(default=0)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.sale')),
            ],
            options={
                'verbose_name': 'DetalleVenta',
                'verbose_name_plural': 'DetalleVentas',
                'ordering': ['id'],
            },
        ),
    ]
