# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name=b'Nome')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Pre\xe7o')),
                ('type', models.CharField(choices=[(b'nenhum', 'Nenhum'), (b'pilula', 'P\xedlula'), (b'gotas', 'Gotas'), (b'capsula', 'Capsula'), (b'gel', 'Gel'), (b'spray', 'Spray'), (b'creme', 'Creme')], db_index=True, default=b'nenhum', max_length=100, verbose_name=b'Tipo')),
                ('medicament_type', models.CharField(choices=[(b'nenhum', 'Nenhum'), (b'generico', 'Gen\xe9rico'), (b'similar', 'Similar'), (b'de-marca', 'De marca')], db_index=True, default=b'nenhum', max_length=100, verbose_name=b'Tipo do medicamento')),
                ('manufacturer', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Fabricante')),
                ('available', models.BooleanField(default=1, verbose_name='Dispon\xedvel')),
                ('obs', models.TextField(blank=True, null=True, verbose_name='Observa\xe7\xf5es')),
                ('image', models.CharField(blank=True, max_length=255, null=True, verbose_name='Imagem')),
                ('active', models.BooleanField(default=1, verbose_name=b'Ativo')),
                ('deleted', models.BooleanField(default=0, verbose_name=b'Deletado')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company', verbose_name='Empresa')),
                ('products_related', models.ManyToManyField(related_name='_product_products_related_+', to='product.Product')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='ProductBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principio_ativo', models.CharField(blank=True, max_length=255, null=True, verbose_name='Princ\xedpio ativo')),
                ('cnpj', models.CharField(blank=True, max_length=40, null=True, verbose_name='CNPJ')),
                ('laboratorio', models.CharField(blank=True, max_length=255, null=True, verbose_name='Laborat\xf3rio')),
                ('codigo_ggrem', models.CharField(blank=True, max_length=255, null=True, verbose_name='C\xf3digo GGREM')),
                ('registro', models.CharField(blank=True, max_length=255, null=True, verbose_name='Registro')),
                ('ean', models.CharField(blank=True, max_length=255, null=True, verbose_name='EAN')),
                ('produto', models.CharField(blank=True, max_length=255, null=True, verbose_name='Produto')),
                ('apresentacao', models.CharField(blank=True, max_length=255, null=True, verbose_name='Apresenta\xe7\xe3o')),
                ('classe_terapeutica', models.CharField(blank=True, max_length=255, null=True, verbose_name='Classe Terapeutica')),
                ('pf0', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='PF 0%')),
                ('pf12', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='PF 12%')),
                ('pf17', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='PF 17%')),
                ('pf18', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='PF 18%')),
                ('pf19', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='PF 19%')),
                ('pf17_manaus', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='PF 17 MANAUS')),
                ('pmc0', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='PMC 0%')),
                ('pmc12', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='PMC 12%')),
                ('pmc17', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='PMC 17%')),
                ('pmc18', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='PMC 18%')),
                ('pmc19', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='PMC 19%')),
                ('pmc17_manaus', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='PMC 17 MANAUS')),
                ('restricao_hospitalar', models.BooleanField(default=0, verbose_name=b'Restri\xc3\xa7\xc3\xa3o Hospitalar')),
                ('cap', models.BooleanField(default=0, verbose_name=b'CAP')),
                ('confaz_87', models.BooleanField(default=0, verbose_name=b'CONFAZ 87')),
                ('analise_recursal', models.CharField(blank=True, max_length=255, null=True, verbose_name='An\xe1lise Recursal')),
                ('ultima_alteracao', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Produto Base',
                'verbose_name_plural': 'Produtos Base',
            },
        ),
    ]