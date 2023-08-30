# Generated by Django 4.2.4 on 2023-08-30 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_text', models.TextField()),
                ('translated_text', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('source_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_translations', to='translator_app.language')),
                ('target_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_translations', to='translator_app.language')),
            ],
        ),
    ]