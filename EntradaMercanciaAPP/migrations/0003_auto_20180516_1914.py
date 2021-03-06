# Generated by Django 2.0.5 on 2018-05-16 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EntradaMercanciaAPP', '0002_auto_20180516_0432'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntradaMercanciaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costoTotal', models.FloatField()),
                ('cantidadTotal', models.IntegerField()),
                ('comentarios', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='entradamercancia',
            name='cantidadTotal',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='entradamercanciaproducto',
            name='idEMFk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EntradaMercanciaAPP.EntradaMercancia'),
        ),
        migrations.AddField(
            model_name='entradamercanciaproducto',
            name='idProductoFk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EntradaMercanciaAPP.Producto'),
        ),
    ]
