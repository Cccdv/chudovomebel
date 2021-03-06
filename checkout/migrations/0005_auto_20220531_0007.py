# Generated by Django 3.2.7 on 2022-05-30 21:07

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Заказы товаров'},
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='order',
            name='county',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(max_length=50, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='order',
            name='grand_total',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Итого'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(editable=False, max_length=32, verbose_name='Номер заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Сумма заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Индекс'),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address1',
            field=models.CharField(max_length=80, verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254, verbose_name='Ключ оплаты Stripe'),
        ),
        migrations.AlterField(
            model_name='order',
            name='town_or_city',
            field=models.CharField(max_length=40, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(blank=True, help_text='Выберете профиль', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.userprofile'),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='lineitem_total',
            field=models.DecimalField(decimal_places=0, editable=False, max_digits=6, verbose_name='Сумма заказа ₽'),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
    ]
