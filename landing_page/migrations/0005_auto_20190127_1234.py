# Generated by Django 2.1.4 on 2019-01-27 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0004_auto_20190126_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
        migrations.RemoveField(
            model_name='blogstuff',
            name='post_image',
        ),
        migrations.AddField(
            model_name='blogdetails',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing_page.BlogStuff'),
        ),
    ]
