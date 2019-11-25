# Generated by Django 2.2.6 on 2019-11-18 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizer_game', '0006_add_question_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizer_game.Question', verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='value',
            field=models.IntegerField(default=0, verbose_name='Value'),
        ),
        migrations.AlterField(
            model_name='player',
            name='current_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quizer_game.Question'),
        ),
        migrations.AlterField(
            model_name='player',
            name='is_achieved',
            field=models.BooleanField(default=False, verbose_name='Achieve status'),
        ),
        migrations.AlterField(
            model_name='player',
            name='is_failed',
            field=models.BooleanField(default=False, verbose_name='Fail status'),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='player',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quizer_game.Quiz', verbose_name='Quiz'),
        ),
        migrations.AlterField(
            model_name='player',
            name='selected_difficulty',
            field=models.IntegerField(default=0, verbose_name='Difficulty'),
        ),
        migrations.AlterField(
            model_name='player',
            name='time',
            field=models.TimeField(blank=True, null=True, verbose_name='Time spent'),
        ),
        migrations.AlterField(
            model_name='question',
            name='number',
            field=models.IntegerField(default=0, verbose_name='Number'),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizer_game.Quiz', verbose_name='Quiz'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='topic',
            field=models.CharField(max_length=200, verbose_name='Topic'),
        ),
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_point', models.TimeField(blank=True, null=True, verbose_name='Start point')),
                ('end_point', models.TimeField(blank=True, null=True, verbose_name='Stop point')),
                ('name', models.CharField(default='A timer of <django.db.models.fields.related.ForeignKey>', max_length=200, verbose_name='Timer name')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizer_game.Player', verbose_name='Player')),
            ],
        ),
    ]