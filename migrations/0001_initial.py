# Generated by Django 2.1.7 on 2019-05-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_uploaded', models.FileField(upload_to='')),
                ('uploaded_by', models.BigIntegerField()),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('document_name', models.CharField(max_length=100, null=True)),
                ('verified', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
