# Generated by Django 5.1.1 on 2024-09-19 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisgehc', '0007_alter_evento_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='professor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
