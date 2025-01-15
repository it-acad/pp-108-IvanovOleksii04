# Generated by Django 4.1 on 2025-01-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_count_book_description_book_name_alter_book_id'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('name', models.CharField(blank=True, max_length=20)),
                ('surname', models.CharField(blank=True, max_length=20)),
                ('patronymic', models.CharField(blank=True, max_length=20)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('books', models.ManyToManyField(related_name='authors_of_book', to='book.book')),
            ],
        ),
        migrations.RemoveField(
            model_name='authors',
            name='books',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='Authors',
        ),
    ]
