# Generated by Django 3.0.7 on 2020-06-09 20:38

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=127)),
                ('slug', models.SlugField(max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=True)),
                ('reviewed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='logger',
            name='access',
            field=models.ManyToManyField(related_name='user_access', related_query_name='user_access', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='logger',
            name='is_encrypted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='logger',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='logger',
            name='short_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='logger',
            name='tag',
            field=models.ManyToManyField(to='log.Tags'),
        ),
    ]
