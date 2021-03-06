# Generated by Django 2.0.4 on 2018-04-16 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('large_pickle_file', models.FileField(upload_to='')),
                ('sample_input_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ModelTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('model_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ModelOne')),
            ],
        ),
    ]
