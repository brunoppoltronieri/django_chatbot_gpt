# Generated by Django 4.2.3 on 2023-10-30 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_feedbacks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbacks',
            name='user',
        ),
        migrations.AddField(
            model_name='feedbacks',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='feedbacks',
            name='chat_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='feedbacks',
            name='message_group',
            field=models.TextField(null=True),
        ),
    ]