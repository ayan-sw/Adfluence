# Generated by Django 2.2 on 2019-04-19 08:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import webapp.apps.adfluence.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('i_user_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_first_name', models.CharField(blank=True, default='', max_length=100, verbose_name='first name')),
                ('s_last_name', models.CharField(blank=True, default='', max_length=100, verbose_name='last name')),
                ('s_user_name', models.CharField(max_length=100, unique=True, verbose_name='username')),
                ('s_title', models.CharField(blank=True, default='', max_length=100, verbose_name='title')),
                ('s_email', models.EmailField(max_length=100, unique=True, verbose_name='email address')),
                ('s_is_verified', models.BooleanField(default=False, verbose_name='user registration status')),
                ('s_profile_image', models.ImageField(blank=True, max_length=700, null=True, upload_to='adfluence/image/')),
                ('is_staff', models.BooleanField(default=False)),
                ('s_street', models.CharField(blank=True, default='', max_length=150)),
                ('s_city', models.CharField(blank=True, default='', max_length=50)),
                ('s_state', models.CharField(blank=True, default='', max_length=50)),
                ('s_country', models.CharField(blank=True, default='', max_length=50)),
                ('s_postal_code', models.CharField(blank=True, default='', max_length=20)),
                ('s_mobile', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '9999999999'. Up to 15 digits allowed.", regex='[0-9]{10,15}')])),
                ('s_phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '9999999999'. Up to 15 digits allowed.", regex='[0-9]{10,15}')])),
                ('s_fax', models.CharField(blank=True, default='', max_length=50)),
                ('i_time_zone_id', models.IntegerField(blank=True, null=True)),
                ('i_created_by', models.ForeignKey(blank=True, db_column='i_created_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='User_created_by', to=settings.AUTH_USER_MODEL)),
                ('dt_created_on', models.DateTimeField(auto_now_add=True)),
                ('i_updated_by', models.ForeignKey(blank=True, db_column='i_updated_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='User_updated_by', to=settings.AUTH_USER_MODEL)),
                ('dt_updated_on', models.DateTimeField(auto_now=True)),
                ('e_status', models.CharField(blank=True, choices=[('0', 'Active'), ('1', 'Inactive'), ('2', 'Deleted')], default='0', max_length=1)),
            ],
            options={
                'db_table': 'af_user',
            },
            managers=[
                ('objects', webapp.apps.adfluence.manager.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AfMenu',
            fields=[
                ('i_menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_menu_name', models.CharField(blank=True, max_length=100, null=True)),
                ('s_link', models.CharField(blank=True, max_length=100, null=True)),
                ('i_parent', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='adfluence.AfMenu')),
                ('s_icon_class', models.CharField(blank=True, max_length=100, null=True)),
                ('i_display_order', models.IntegerField(blank=True, null=True)),
                ('i_created_by', models.ForeignKey(blank=True, db_column='i_created_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfMenu_created_by', to=settings.AUTH_USER_MODEL)),
                ('dt_created_on', models.DateTimeField(blank=True, null=True)),
                ('i_updated_by', models.ForeignKey(blank=True, db_column='i_updated_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfMenu_updated_by', to=settings.AUTH_USER_MODEL)),
                ('dt_updated_on', models.DateTimeField(blank=True, null=True)),
                ('e_status', models.CharField(blank=True, choices=[('0', 'Active'), ('1', 'Inactive'), ('2', 'Deleted')], default='0', max_length=1)),
            ],
            options={
                'db_table': 'af_menu',
            },
        ),
        migrations.CreateModel(
            name='AfMenuAction',
            fields=[
                ('i_menu_action_id', models.AutoField(primary_key=True, serialize=False)),
                ('i_menu', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='adfluence.AfMenu')),
                ('s_action_name', models.CharField(blank=True, max_length=100, null=True)),
                ('s_link', models.CharField(blank=True, max_length=100, null=True)),
                ('i_created_by', models.ForeignKey(blank=True, db_column='i_created_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfMenuAction_created_by', to=settings.AUTH_USER_MODEL)),
                ('dt_created_on', models.DateTimeField(blank=True, null=True)),
                ('i_updated_by', models.ForeignKey(blank=True, db_column='i_updated_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfMenuAction_updated_by', to=settings.AUTH_USER_MODEL)),
                ('dt_updated_on', models.DateTimeField(blank=True, null=True)),
                ('e_status', models.CharField(blank=True, choices=[('0', 'Active'), ('1', 'Inactive'), ('2', 'Deleted')], default='0', max_length=1)),
            ],
            options={
                'db_table': 'af_menu_action',
            },
        ),
        migrations.CreateModel(
            name='AfRole',
            fields=[
                ('i_role_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_role_name', models.CharField(blank=True, max_length=100, null=True)),
                ('s_key', models.CharField(blank=True, max_length=100, null=True)),
                ('i_display_order', models.IntegerField(blank=True, null=True)),
                ('i_created_by', models.ForeignKey(blank=True, db_column='i_created_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfRole_created_by', to=settings.AUTH_USER_MODEL)),
                ('dt_created_on', models.DateTimeField(blank=True, null=True)),
                ('i_updated_by', models.ForeignKey(blank=True, db_column='i_updated_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfRole_updated_by', to=settings.AUTH_USER_MODEL)),
                ('dt_updated_on', models.DateTimeField(blank=True, null=True)),
                ('e_status', models.CharField(blank=True, choices=[('0', 'Active'), ('1', 'Inactive'), ('2', 'Deleted')], default='0', max_length=1)),
            ],
            options={
                'db_table': 'af_role',
            },
        ),
        migrations.CreateModel(
            name='AfUserType',
            fields=[
                ('i_user_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_user_type_name', models.CharField(blank=True, max_length=100, null=True)),
                ('i_created_by', models.ForeignKey(blank=True, db_column='i_created_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfUserType_created_by', to=settings.AUTH_USER_MODEL)),
                ('dt_created_on', models.DateTimeField(blank=True, null=True)),
                ('i_updated_by', models.ForeignKey(blank=True, db_column='i_updated_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfUserType_updated_by', to=settings.AUTH_USER_MODEL)),
                ('dt_updated_on', models.DateTimeField(blank=True, null=True)),
                ('e_status', models.CharField(blank=True, choices=[('0', 'Active'), ('1', 'Inactive'), ('2', 'Deleted')], default='0', max_length=1)),
            ],
            options={
                'db_table': 'af_user_type',
            },
        ),
        migrations.CreateModel(
            name='AfUserRole',
            fields=[
                ('i_user_role_id', models.AutoField(primary_key=True, serialize=False)),
                ('i_user', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
                ('i_role', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='adfluence.AfRole')),
                ('e_access_type', models.BooleanField(default=False)),
                ('e_default_role', models.BooleanField(default=False)),
                ('i_created_by', models.ForeignKey(blank=True, db_column='i_created_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfUserRole_created_by', to=settings.AUTH_USER_MODEL)),
                ('dt_created_on', models.DateTimeField(blank=True, null=True)),
                ('i_updated_by', models.ForeignKey(blank=True, db_column='i_updated_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfUserRole_updated_by', to=settings.AUTH_USER_MODEL)),
                ('dt_updated_on', models.DateTimeField(blank=True, null=True)),
                ('e_status', models.CharField(blank=True, choices=[('0', 'Active'), ('1', 'Inactive'), ('2', 'Deleted')], default='0', max_length=1)),
            ],
            options={
                'db_table': 'af_user_role',
            },
        ),
        migrations.CreateModel(
            name='AfTimeZone',
            fields=[
                ('i_time_zone_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_time_zone_name', models.CharField(blank=True, max_length=100, null=True)),
                ('s_utc_offset', models.CharField(blank=True, max_length=100, null=True)),
                ('i_created_by', models.ForeignKey(blank=True, db_column='i_created_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfTimeZone_created_by', to=settings.AUTH_USER_MODEL)),
                ('dt_created_on', models.TextField(blank=True, null=True)),
                ('i_updated_by', models.ForeignKey(blank=True, db_column='i_updated_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfTimeZone_updated_by', to=settings.AUTH_USER_MODEL)),
                ('dt_updated_on', models.DateTimeField(blank=True, null=True)),
                ('e_status', models.CharField(blank=True, choices=[('0', 'Active'), ('1', 'Inactive'), ('2', 'Deleted')], default='0', max_length=1)),
            ],
            options={
                'db_table': 'af_time_zone',
            },
        ),
        migrations.AddField(
            model_name='afrole',
            name='i_user_type',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='adfluence.AfUserType'),
        ),
        migrations.CreateModel(
            name='AfMenuRole',
            fields=[
                ('i_menu_role_id', models.AutoField(primary_key=True, serialize=False)),
                ('i_menu', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='adfluence.AfMenu')),
                ('i_parent', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfMenuRole_parent', to='adfluence.AfMenu')),
                ('i_user', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
                ('i_role', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='adfluence.AfRole')),
                ('i_menu_action', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='adfluence.AfMenuAction')),
                ('i_created_by', models.ForeignKey(blank=True, db_column='i_created_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfMenuRole_created_by', to=settings.AUTH_USER_MODEL)),
                ('dt_created_on', models.DateTimeField(blank=True, null=True)),
                ('i_updated_by', models.ForeignKey(blank=True, db_column='i_updated_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfMenuRole_updated_by', to=settings.AUTH_USER_MODEL)),
                ('dt_updated_on', models.DateTimeField(blank=True, null=True)),
                ('e_status', models.CharField(blank=True, choices=[('0', 'Active'), ('1', 'Inactive'), ('2', 'Deleted')], default='0', max_length=1)),
            ],
            options={
                'db_table': 'af_menu_role',
            },
        ),
        migrations.CreateModel(
            name='AfCompany',
            fields=[
                ('i_company_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('s_company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('s_contact_name', models.CharField(blank=True, max_length=100, null=True)),
                ('i_company_parent', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='adfluence.AfCompany')),
                ('i_user_type', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='adfluence.AfUserType')),
                ('s_email', models.CharField(blank=True, max_length=100, null=True)),
                ('s_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('s_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('s_fax', models.CharField(blank=True, max_length=50, null=True)),
                ('s_website', models.CharField(blank=True, max_length=100, null=True)),
                ('s_address', models.CharField(blank=True, max_length=100, null=True)),
                ('s_city', models.CharField(blank=True, max_length=50, null=True)),
                ('s_state', models.CharField(blank=True, max_length=50, null=True)),
                ('s_country', models.CharField(blank=True, max_length=50, null=True)),
                ('s_zip', models.CharField(blank=True, max_length=10, null=True)),
                ('s_billing_address1', models.CharField(blank=True, max_length=100, null=True)),
                ('s_billing_address2', models.CharField(blank=True, max_length=100, null=True)),
                ('s_billing_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('s_billing_email', models.CharField(blank=True, max_length=20, null=True)),
                ('i_created_by', models.ForeignKey(blank=True, db_column='i_created_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfCompany_created_by', to=settings.AUTH_USER_MODEL)),
                ('dt_created_on', models.DateTimeField(blank=True, null=True)),
                ('i_updated_by', models.ForeignKey(blank=True, db_column='i_updated_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfCompany_updated_by', to=settings.AUTH_USER_MODEL)),
                ('dt_updated_on', models.DateTimeField(blank=True, null=True)),
                ('e_status', models.CharField(blank=True, choices=[('0', 'Active'), ('1', 'Inactive'), ('2', 'Deleted')], default='0', max_length=1)),
            ],
            options={
                'db_table': 'af_company',
            },
        ),
        migrations.CreateModel(
            name='AfBillingFeeDetail',
            fields=[
                ('i_billing_fee_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('i_company', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='adfluence.AfCompany')),
                ('e_bill_type', models.TextField(blank=True, null=True)),
                ('i_minimum_monthly_fee', models.IntegerField(blank=True, null=True)),
                ('i_minimum_monthly_ad_spend', models.IntegerField(blank=True, null=True)),
                ('i_maximum_monthly_ad_spend', models.IntegerField(blank=True, null=True)),
                ('d_percent_of_ad_spend_bill_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('i_created_by', models.ForeignKey(blank=True, db_column='i_created_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfBillingFeeDetail_created_by', to=settings.AUTH_USER_MODEL)),
                ('dt_created_on', models.DateTimeField(blank=True, null=True)),
                ('i_updated_by', models.ForeignKey(blank=True, db_column='i_updated_by', default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='AfBillingFeeDetail_updated_by', to=settings.AUTH_USER_MODEL)),
                ('dt_updated_on', models.DateTimeField(blank=True, null=True)),
                ('e_status', models.CharField(blank=True, choices=[('0', 'Active'), ('1', 'Inactive'), ('2', 'Deleted')], default='0', max_length=1)),
            ],
            options={
                'db_table': 'af_billing_fee_detail',
            },
        ),
    ]