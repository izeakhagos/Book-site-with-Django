# Generated by Django 4.0.4 on 2022-05-31 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_remove_book_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_book', models.CharField(max_length=100)),
            ],
        ),
    ]
