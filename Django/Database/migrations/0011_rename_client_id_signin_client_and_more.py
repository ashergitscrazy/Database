# Generated by Django 5.0.3 on 2024-04-13 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0010_alter_signin_client_id_alter_signin_course_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signin',
            old_name='client_id',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='signin',
            old_name='course_id',
            new_name='course',
        ),
    ]
