# Generated by Django 5.0 on 2023-12-22 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_blog_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default='', max_length=10),
        ),
    ]
