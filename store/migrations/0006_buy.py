# Generated by Django 3.2.4 on 2021-06-26 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_delete_buy'),
    ]

    operations = [
        migrations.CreateModel(
            name='buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billid', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('cost', models.FloatField()),
                ('mid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='store.medicine')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicines', to='store.patient')),
            ],
        ),
    ]
