# Generated by Django 5.1 on 2024-08-18 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0012_alter_course_instructor_alter_signin_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='non_resident_cost',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='resident_cost',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='client',
            name='birthdate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='client',
            name='emergency_contact',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
