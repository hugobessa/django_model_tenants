# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 05:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import model_utils.fields
import shared_schema_tenants.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('shared_schema_tenants', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TenantSpecificFieldCharPivot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_id', models.PositiveIntegerField()),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
                'default_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='TenantSpecificFieldDatePivot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_id', models.PositiveIntegerField()),
                ('value', models.DateField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
                'default_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='TenantSpecificFieldDateTimePivot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_id', models.PositiveIntegerField()),
                ('value', models.DateTimeField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
                'default_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='TenantSpecificFieldDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('data_type', model_utils.fields.StatusField(choices=[('char', 'char'), ('text', 'text'), ('integer', 'integer'), ('float', 'float'), ('datetime', 'datetime'), ('date', 'date')], default='char', max_length=100, no_check_for_status=True)),
                ('is_required', models.BooleanField(default=False)),
                ('default_value', models.TextField()),
                ('table_id', models.PositiveIntegerField(blank=True, null=True)),
                ('table_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('tenant', models.ForeignKey(default=shared_schema_tenants.mixins.get_default_tenant, on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants.Tenant')),
            ],
        ),
        migrations.CreateModel(
            name='TenantSpecificFieldFloatPivot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_id', models.PositiveIntegerField()),
                ('value', models.FloatField()),
                ('definition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants_custom_data.TenantSpecificFieldDefinition')),
                ('row_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('tenant', models.ForeignKey(default=shared_schema_tenants.mixins.get_default_tenant, on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants.Tenant')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
                'default_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='TenantSpecificFieldIntegerPivot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_id', models.PositiveIntegerField()),
                ('value', models.IntegerField()),
                ('definition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants_custom_data.TenantSpecificFieldDefinition')),
                ('row_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('tenant', models.ForeignKey(default=shared_schema_tenants.mixins.get_default_tenant, on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants.Tenant')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
                'default_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='TenantSpecificFieldsValidator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_path', models.CharField(max_length=255)),
                ('tenants', models.ManyToManyField(related_name='validators_available', to='shared_schema_tenants.Tenant')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
                'default_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='TenantSpecificFieldTextPivot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_id', models.PositiveIntegerField()),
                ('value', models.TextField()),
                ('definition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants_custom_data.TenantSpecificFieldDefinition')),
                ('row_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('tenant', models.ForeignKey(default=shared_schema_tenants.mixins.get_default_tenant, on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants.Tenant')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
                'default_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='TenantSpecificTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('tenant', models.ForeignKey(default=shared_schema_tenants.mixins.get_default_tenant, on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants.Tenant')),
            ],
        ),
        migrations.CreateModel(
            name='TenantSpecificTableRow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='shared_schema_tenants_custom_data.TenantSpecificTable')),
                ('tenant', models.ForeignKey(default=shared_schema_tenants.mixins.get_default_tenant, on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants.Tenant')),
            ],
            options={
                'base_manager_name': 'original_manager',
                'default_manager_name': 'original_manager',
            },
            managers=[
                ('original_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='TenantSpecificTablesGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tenant_specific_tables_groups', to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='TenantSpecificTablesPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants_custom_data.TenantSpecificTable')),
                ('tenant', models.ForeignKey(default=shared_schema_tenants.mixins.get_default_tenant, on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants.Tenant')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
                'default_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='TenantSpecificTablesRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups', models.ManyToManyField(related_name='relationships', to='shared_schema_tenants_custom_data.TenantSpecificTablesGroup')),
                ('permissions', models.ManyToManyField(related_name='relationships', to='shared_schema_tenants_custom_data.TenantSpecificTablesPermission')),
                ('tenant', models.ForeignKey(default=shared_schema_tenants.mixins.get_default_tenant, on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants.Tenant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
                'default_manager_name': 'objects',
            },
        ),
        migrations.AddField(
            model_name='tenantspecifictablesgroup',
            name='permissions',
            field=models.ManyToManyField(blank=True, related_name='groups', to='shared_schema_tenants_custom_data.TenantSpecificTablesPermission'),
        ),
        migrations.AddField(
            model_name='tenantspecifictablesgroup',
            name='tenant',
            field=models.ForeignKey(default=shared_schema_tenants.mixins.get_default_tenant, on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants.Tenant'),
        ),
        migrations.AddField(
            model_name='tenantspecificfielddefinition',
            name='validators',
            field=models.ManyToManyField(blank=True, to='shared_schema_tenants_custom_data.TenantSpecificFieldsValidator'),
        ),
        migrations.AddField(
            model_name='tenantspecificfielddatetimepivot',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants_custom_data.TenantSpecificFieldDefinition'),
        ),
        migrations.AddField(
            model_name='tenantspecificfielddatetimepivot',
            name='row_content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='tenantspecificfielddatetimepivot',
            name='tenant',
            field=models.ForeignKey(default=shared_schema_tenants.mixins.get_default_tenant, on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants.Tenant'),
        ),
        migrations.AddField(
            model_name='tenantspecificfielddatepivot',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants_custom_data.TenantSpecificFieldDefinition'),
        ),
        migrations.AddField(
            model_name='tenantspecificfielddatepivot',
            name='row_content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='tenantspecificfielddatepivot',
            name='tenant',
            field=models.ForeignKey(default=shared_schema_tenants.mixins.get_default_tenant, on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants.Tenant'),
        ),
        migrations.AddField(
            model_name='tenantspecificfieldcharpivot',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants_custom_data.TenantSpecificFieldDefinition'),
        ),
        migrations.AddField(
            model_name='tenantspecificfieldcharpivot',
            name='row_content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='tenantspecificfieldcharpivot',
            name='tenant',
            field=models.ForeignKey(default=shared_schema_tenants.mixins.get_default_tenant, on_delete=django.db.models.deletion.CASCADE, to='shared_schema_tenants.Tenant'),
        ),
        migrations.AlterUniqueTogether(
            name='tenantspecifictablesgroup',
            unique_together=set([('group', 'tenant')]),
        ),
        migrations.AlterUniqueTogether(
            name='tenantspecifictable',
            unique_together=set([('tenant', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='tenantspecificfielddefinition',
            unique_together=set([('tenant', 'table_id', 'table_content_type', 'name')]),
        ),
    ]
