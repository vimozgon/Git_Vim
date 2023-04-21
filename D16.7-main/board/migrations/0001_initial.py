# Generated by Django 4.0.5 on 2022-06-14 13:18

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Tanks', 'Танки'), ('Healers', 'Хилы'), ('DD', 'ДД'), ('Merch', 'Торговцы'), ('Guild', 'Гилдмастеры'), ('Quest', 'Квестгиверы'), ('Black', 'Кузнецы'), ('Tanner', 'Кожевники'), ('Potion', 'Зельевары'), ('Spell', 'Мастера заклинаний')], max_length=10, verbose_name='Категория')),
                ('time_public', models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('text', ckeditor.fields.RichTextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('status', models.BooleanField(default=False)),
                ('time_public', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.post')),
            ],
        ),
    ]
