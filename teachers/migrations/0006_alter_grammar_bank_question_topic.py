# Generated by Django 4.2.7 on 2023-11-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_alter_grammar_bank_question_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grammar_bank',
            name='question_topic',
            field=models.CharField(choices=[('Noun', 'The Noun'), ('Pronoun', 'Pronoun'), ('article', 'Article'), ('So do i', 'So do I'), ('Quantifiers', 'Quantifiers'), ('Tenses', 'Tense Forms'), ('Passive', 'Passive Voice'), ('Modal', 'Modal Verbs')], max_length=40),
        ),
    ]
