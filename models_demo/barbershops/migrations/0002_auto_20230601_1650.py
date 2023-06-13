# Generated by Django 3.2.19 on 2023-06-01 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barbershops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BarbershopBarbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateField(auto_now_add=True)),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershops.barber')),
                ('barbershop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershops.barbershop')),
            ],
        ),
        migrations.AddField(
            model_name='barbershop',
            name='barbers',
            field=models.ManyToManyField(through='barbershops.BarbershopBarbers', to='barbershops.Barber'),
        ),
    ]