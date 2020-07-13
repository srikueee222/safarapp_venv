# Generated by Django 3.0 on 2020-07-13 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=20)),
                ('firstName', models.CharField(default='', max_length=90)),
                ('surName', models.CharField(default='', max_length=90)),
                ('dob', models.CharField(default='', max_length=90)),
                ('mobile', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('confirmpassword', models.CharField(max_length=100)),
                ('addressline1', models.CharField(default='', max_length=300)),
                ('addressline2', models.CharField(blank=True, default='', max_length=300)),
                ('town', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('postcode', models.CharField(default='', max_length=100)),
                ('addDoctDetails', models.CharField(blank=True, default='', max_length=100)),
                ('efirstName', models.CharField(blank=True, default='', max_length=300)),
                ('esurName', models.CharField(blank=True, default='', max_length=300)),
                ('emobile', models.CharField(blank=True, default='', max_length=300)),
                ('activestatus', models.CharField(blank=True, default='', max_length=100)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=1024)),
                ('refresh_token', models.CharField(max_length=1024)),
                ('access_token_created_at', models.DateTimeField(auto_now_add=True)),
                ('refresh_token_created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField(default=0)),
            ],
        ),
    ]