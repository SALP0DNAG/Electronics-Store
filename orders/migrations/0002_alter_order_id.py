# Generated by Django 5.0.1 on 2024-07-09 09:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=10, primary_key=True, serialize=False),
        ),
    ]
