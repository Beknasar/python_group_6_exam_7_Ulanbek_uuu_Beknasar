# Generated by Django 2.2 on 2020-08-29 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200829_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_choice', to='webapp.Choice', verbose_name='Варианты ответа'),
        ),
    ]
