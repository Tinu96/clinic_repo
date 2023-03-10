# Generated by Django 4.1.4 on 2022-12-29 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0049_alter_cart_giftcard_alter_cart_membership'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cart',
            name='giftcard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.giftcards'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='membership',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.memberships'),
        ),
    ]