# Generated by Django 4.2.6 on 2023-10-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_contact_persons_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='persons_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='your_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='your_message',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='your_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]