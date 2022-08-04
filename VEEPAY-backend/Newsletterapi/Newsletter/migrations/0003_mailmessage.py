# Generated by Django 4.0.6 on 2022-07-14 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newsletter', '0002_alter_newsletter_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('message', models.TextField(null=True)),
            ],
        ),
    ]
