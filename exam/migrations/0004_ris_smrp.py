# Generated by Django 4.1.3 on 2022-12-07 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_remove_smrp_jxr_remove_smrp_modified_remove_smrp_ris_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ris',
            name='smrp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exam.smrp'),
        ),
    ]
