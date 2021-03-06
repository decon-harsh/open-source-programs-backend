# Generated by Django 3.0.7 on 2020-07-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "osp",
            "0011_answer_checkboxvalue_choicevalue_datevalue_dropdownvalue_fileuploadvalue_formfeedback_paragraphvalue",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="choicevalue",
            name="value",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="dropdownvalue",
            name="value",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="fileuploadvalue",
            name="value",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="paragraphvalue",
            name="value",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="shortanswervalue",
            name="value",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
