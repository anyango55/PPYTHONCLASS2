
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics'),
        ),
    ]
