# Generated by Django 4.0.5 on 2022-07-02 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publication_date', models.DateField()),
                ('image_url', models.URLField(default=None, max_length=500)),
                ('content', models.CharField(max_length=500)),
                ('approved', models.CharField(max_length=50)),
                ('category', models.ManyToManyField(to='rarerestapi.category')),
            ],
        ),
        migrations.CreateModel(
            name='RareUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=50)),
                ('image_url', models.URLField(default=None, max_length=500)),
                ('created_on', models.DateField()),
                ('active', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('image_url', models.URLField(default=None, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField()),
                ('deleted_on', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rarerestapi.rareuser')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='rarerestapi.rareuser')),
            ],
        ),
        migrations.CreateModel(
            name='PostReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rarerestapi.post')),
                ('reaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rarerestapi.reaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rarerestapi.rareuser')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='posttag',
            field=models.ManyToManyField(to='rarerestapi.tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rarerestapi.rareuser'),
        ),
        migrations.CreateModel(
            name='DemotionQueue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=50)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rarerestapi.rareuser')),
                ('approver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approving', to='rarerestapi.rareuser')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('created_on', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rarerestapi.rareuser')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rarerestapi.post')),
            ],
        ),
    ]
