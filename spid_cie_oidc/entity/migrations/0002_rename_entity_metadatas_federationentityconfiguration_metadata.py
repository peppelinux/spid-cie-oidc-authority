# Generated by Django 4.0.2 on 2022-02-06 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_entity', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='federationentityconfiguration',
            old_name='entity_metadatas',
            new_name='metadata',
        ),
    ]
