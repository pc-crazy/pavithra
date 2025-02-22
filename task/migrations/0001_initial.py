# Generated by Django 5.1.3 on 2024-11-27 07:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(blank=True, max_length=1024, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('due_data', models.DateField(blank=True, null=True)),
                ('assigned_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
