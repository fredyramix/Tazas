# Generated by Django 2.0.5 on 2018-05-20 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EntradaMercanciaAPP', '0006_auto_20180520_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='AjusteMercancia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadAnterior', models.IntegerField()),
                ('cantidadNueva', models.IntegerField()),
                ('comentarios', models.CharField(max_length=200)),
                ('idExistenciaProductoFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EntradaMercanciaAPP.Existencia')),
                ('idUsuarioFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoOperaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CorteCaja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('entrada_salida', models.BooleanField()),
                ('saldoAnterior', models.FloatField()),
                ('saldoNuevo', models.FloatField()),
                ('idStatusFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EntradaMercanciaAPP.Status')),
                ('idUsuarioFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MantenimientoPrecios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precioVenta', models.FloatField()),
                ('idClienteFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EntradaMercanciaAPP.Cliente')),
                ('idProductoFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EntradaMercanciaAPP.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField()),
                ('comentarios', models.CharField(max_length=200)),
                ('entrada_salida', models.BooleanField()),
                ('idCorteFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EntradaMercanciaAPP.CorteCaja')),
                ('idOperacionesFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EntradaMercanciaAPP.CatalogoOperaciones')),
                ('idStatusFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EntradaMercanciaAPP.Status')),
                ('idUsuarioFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Operaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('entrada_salida', models.BooleanField()),
                ('idCatalogoFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EntradaMercanciaAPP.CatalogoOperaciones')),
            ],
        ),
        migrations.CreateModel(
            name='UnidadVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.IntegerField(default=1)),
                ('fecha', models.DateTimeField(verbose_name='Fecha de Ingreso')),
                ('comentarios', models.CharField(max_length=200)),
                ('precioTotal', models.FloatField()),
                ('cantidadTotal', models.IntegerField()),
                ('idClienteFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EntradaMercanciaAPP.Cliente')),
                ('idStatusFk', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='EntradaMercanciaAPP.Status')),
                ('idUsuarioFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VentaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precioVenta', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('comentarios', models.CharField(max_length=200)),
                ('idProductoFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EntradaMercanciaAPP.Producto')),
                ('idStatusFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EntradaMercanciaAPP.Status')),
                ('idUnidadVentaFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EntradaMercanciaAPP.UnidadVenta')),
                ('idVFk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EntradaMercanciaAPP.Venta')),
            ],
        ),
        migrations.AddField(
            model_name='mantenimientoprecios',
            name='idUnidadVentaFk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EntradaMercanciaAPP.UnidadVenta'),
        ),
    ]