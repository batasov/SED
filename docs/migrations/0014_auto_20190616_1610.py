# Generated by Django 2.2.1 on 2019-06-16 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0013_auto_20190616_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='reg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doc_reg', to='docs.Reg'),
        ),
    ]
