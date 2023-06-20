# Generated by Django 4.1.2 on 2023-04-24 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aufträge', '0004_alter_auftragspositionen_auftragsnummer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auftragspositionen',
            name='auftragsnummer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aufträge.auftrag'),
        ),
        migrations.AlterField(
            model_name='auftragspositionen',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='auftragspositionen',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
