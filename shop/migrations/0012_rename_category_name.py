from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_seed_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
    ]
