# Generated by Django 4.2.17 on 2024-12-18 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('altpoet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(default='/{item)', max_length=80)),
                ('base', models.CharField(default='', max_length=80)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documents', to='altpoet.project')),
            ],
        ),
        migrations.RemoveField(
            model_name='img',
            name='page',
        ),
        migrations.AddField(
            model_name='alt',
            name='img',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alts', to='altpoet.img'),
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.AddField(
            model_name='img',
            name='document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imgs', to='altpoet.document'),
        ),
    ]
