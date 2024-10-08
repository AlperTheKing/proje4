# Generated by Django 4.2.11 on 2024-10-08 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='startup',
            name='investment_date',
        ),
        migrations.RemoveField(
            model_name='startup',
            name='sector',
        ),
        migrations.AddField(
            model_name='startup',
            name='image_url',
            field=models.URLField(default='https://example.com/default-image.jpg', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='startup',
            name='website_url',
            field=models.URLField(default='https://example.com/default-image.jpg', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='startup',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
