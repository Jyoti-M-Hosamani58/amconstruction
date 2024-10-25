# Generated by Django 5.1.2 on 2024-10-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Am_app', '0003_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listofmachine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='pdfs/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
