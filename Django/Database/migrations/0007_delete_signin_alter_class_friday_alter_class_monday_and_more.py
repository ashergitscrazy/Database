# Generated by Django 5.0.3 on 2024-04-13 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0006_signin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignIn',
        ),
        migrations.AlterField(
            model_name='class',
            name='friday',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='class',
            name='monday',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='class',
            name='saturday',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='class',
            name='sunday',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='class',
            name='thursday',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='class',
            name='tuesday',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='class',
            name='wednesday',
            field=models.BooleanField(),
        ),
    ]
