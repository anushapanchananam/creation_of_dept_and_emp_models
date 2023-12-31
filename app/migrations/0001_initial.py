# Generated by Django 4.2.3 on 2023-08-17 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dept',
            fields=[
                ('dname', models.CharField(max_length=100)),
                ('dloc', models.CharField(max_length=100)),
                ('dept_no', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='emp',
            fields=[
                ('eno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('hiredate', models.DateField()),
                ('sal', models.IntegerField()),
                ('com', models.IntegerField(default=None, null=True)),
                ('dept_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]
