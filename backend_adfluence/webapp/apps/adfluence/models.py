from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from django.core.validators import RegexValidator
from . import manager
from django.utils.translation import ugettext_lazy as _


STATUS = (
        ('0', 'Active'),
        ('1', 'Inactive'),
        ('2', 'Deleted'),
    )

# Create your models here.
class User(AbstractBaseUser):    
    i_user_id = models.AutoField(primary_key=True)
    s_first_name = models.CharField(_('first name'), max_length=100, blank=True, default="")
    s_last_name = models.CharField(_('last name'), max_length=100, blank=True, default="")
    s_user_name = models.CharField(_('username'), max_length=100, unique=True)
    s_title = models.CharField(_('title'), max_length=100, blank=True, default="")
    s_email = models.EmailField(_('email address'), max_length=100, unique=True)
    s_is_verified = models.BooleanField(_('user registration status'), default=False)
    s_profile_image = models.ImageField(upload_to="adfluence/image/", max_length=700, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    s_street = models.CharField(max_length=150, blank=True, default="")
    s_city = models.CharField(max_length=50, blank=True, default="")
    s_state = models.CharField(max_length=50, blank=True, default="")
    s_country = models.CharField(max_length=50, blank=True, default="")
    s_postal_code = models.CharField(max_length=20, blank=True, default="")

    phone_regex = RegexValidator(regex='[0-9]{10,15}',
                                 message=_("Phone number must be entered in the format:"
                                            " '9999999999'. Up to 15 digits allowed."))
    s_mobile = models.CharField(validators=[phone_regex], max_length=15, blank=False, null=False)
    s_phone = models.CharField(validators=[phone_regex], max_length=15, blank=False, null=False)
    s_fax = models.CharField(max_length=50, blank=True, default="")
    i_time_zone_id = models.IntegerField(blank=True, null=True)
    i_created_by = models.ForeignKey('User', db_column='i_created_by', related_name='User_created_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_created_on = models.DateTimeField(auto_now_add=True)
    i_updated_by = models.ForeignKey('User', db_column='i_updated_by', related_name='User_updated_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_updated_on = models.DateTimeField(auto_now=True)
    e_status = models.CharField(max_length=1, choices=STATUS, blank=True, default="0")
    
    USERNAME_FIELD = 's_email'

    objects = manager.CustomUserManager()

    class Meta:
    	db_table = "af_user"
    

    def save(self, *args, **kwargs):
        try:
            orig = User.objects.get(pk=self.pk)
        except:
            orig = None
        self.i_created_by = orig if orig else None
        self.i_updated_by = orig if orig else None
        
        self.clean()

        super(User, self).save(*args, **kwargs)

    def clean(self):
        super(User, self).clean()
        if self.s_email:
            self.s_user_name = self.s_email

    @property
    def is_superuser(self):
        return self.is_staff

    @property
    def is_admin(self):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        parts = [self.s_first_name, self.s_last_name]
        return " ".join(x for x in parts if x)

    def __str__(self):
        return str(self.get_full_name() + '('+self.s_email+')')


################################################################################


class AfUserType(models.Model):
    i_user_type_id = models.AutoField(primary_key=True)
    s_user_type_name = models.CharField(max_length=100, blank=True, null=True)
    i_created_by = models.ForeignKey('User', db_column='i_created_by', related_name='AfUserType_created_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_created_on = models.DateTimeField(auto_now_add=True)
    i_updated_by = models.ForeignKey('User', db_column='i_updated_by', related_name='AfUserType_updated_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_updated_on = models.DateTimeField(auto_now=True)
    e_status = models.CharField(max_length=1, choices=STATUS, blank=True, default="0")

    class Meta:
        db_table = 'af_user_type'



class AfCompany(models.Model):
    i_company_id = models.BigIntegerField(primary_key=True)
    s_company_name = models.CharField(max_length=100, blank=True, null=True)
    s_contact_name = models.CharField(max_length=100, blank=True, null=True)
    i_company_parent = models.ForeignKey('AfCompany', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    i_user_type = models.ForeignKey(AfUserType, blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    s_email = models.CharField(max_length=100, blank=True, null=True)
    s_mobile = models.CharField(max_length=20, blank=True, null=True)
    s_phone = models.CharField(max_length=20, blank=True, null=True)
    s_fax = models.CharField(max_length=50, blank=True, null=True)
    s_website = models.CharField(max_length=100, blank=True, null=True)
    s_address = models.CharField(max_length=100, blank=True, null=True)
    s_city = models.CharField(max_length=50, blank=True, null=True)
    s_state = models.CharField(max_length=50, blank=True, null=True)
    s_country = models.CharField(max_length=50, blank=True, null=True)
    s_zip = models.CharField(max_length=10, blank=True, null=True)
    s_billing_address1 = models.CharField(max_length=100, blank=True, null=True)
    s_billing_address2 = models.CharField(max_length=100, blank=True, null=True)
    s_billing_phone = models.CharField(max_length=20, blank=True, null=True)
    s_billing_email = models.CharField(max_length=20, blank=True, null=True)
    i_created_by = models.ForeignKey(User, db_column='i_created_by', related_name='AfCompany_created_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_created_on = models.DateTimeField(auto_now_add=True)
    i_updated_by = models.ForeignKey(User, db_column='i_updated_by', related_name='AfCompany_updated_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_updated_on = models.DateTimeField(auto_now=True)
    e_status = models.CharField(max_length=1, choices=STATUS, blank=True, default="0")

    class Meta:
        db_table = 'af_company'

class AfBillingFeeDetail(models.Model):
    i_billing_fee_detail_id = models.AutoField(primary_key=True)
    i_company = models.ForeignKey(AfCompany, blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    e_bill_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    i_minimum_monthly_fee = models.IntegerField(blank=True, null=True)
    i_minimum_monthly_ad_spend = models.IntegerField(blank=True, null=True)
    i_maximum_monthly_ad_spend = models.IntegerField(blank=True, null=True)
    d_percent_of_ad_spend_bill_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    i_created_by = models.ForeignKey(User, db_column='i_created_by', related_name='AfBillingFeeDetail_created_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_created_on = models.DateTimeField(auto_now_add=True)
    i_updated_by = models.ForeignKey(User, db_column='i_updated_by', related_name='AfBillingFeeDetail_updated_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_updated_on = models.DateTimeField(auto_now=True)
    e_status = models.CharField(max_length=1, choices=STATUS, blank=True, default="0")

    class Meta:
        db_table = 'af_billing_fee_detail'


class AfMenu(models.Model):
    i_menu_id = models.AutoField(primary_key=True)
    s_menu_name = models.CharField(max_length=100, blank=True, null=True)
    s_link = models.CharField(max_length=100, blank=True, null=True)
    i_parent = models.ForeignKey('AfMenu', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    s_icon_class = models.CharField(max_length=100, blank=True, null=True)
    i_display_order = models.IntegerField(blank=True, null=True)
    i_created_by = models.ForeignKey(User, db_column='i_created_by', related_name='AfMenu_created_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_created_on = models.DateTimeField(auto_now_add=True)
    i_updated_by = models.ForeignKey(User, db_column='i_updated_by', related_name='AfMenu_updated_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_updated_on = models.DateTimeField(auto_now=True)
    e_status = models.CharField(max_length=1, choices=STATUS, blank=True, default="0")

    class Meta:
        db_table = 'af_menu'


class AfMenuAction(models.Model):
    i_menu_action_id = models.AutoField(primary_key=True)
    i_menu = models.ForeignKey(AfMenu, blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    s_action_name = models.CharField(max_length=100, blank=True, null=True)
    s_link = models.CharField(max_length=100, blank=True, null=True)
    i_created_by = models.ForeignKey(User, db_column='i_created_by', related_name='AfMenuAction_created_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_created_on = models.DateTimeField(auto_now_add=True)
    i_updated_by = models.ForeignKey(User, db_column='i_updated_by', related_name='AfMenuAction_updated_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_updated_on = models.DateTimeField(auto_now=True)
    e_status = models.CharField(max_length=1, choices=STATUS, blank=True, default="0")

    class Meta:
        db_table = 'af_menu_action'


class AfRole(models.Model):
    i_role_id = models.AutoField(primary_key=True)
    s_role_name = models.CharField(max_length=100, blank=True, null=True)
    i_user_type = models.ForeignKey(AfUserType, blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    s_key = models.CharField(max_length=100, blank=True, null=True)
    i_display_order = models.IntegerField(blank=True, null=True)
    i_created_by = models.ForeignKey(User, db_column='i_created_by', related_name='AfRole_created_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_created_on = models.DateTimeField(auto_now_add=True)
    i_updated_by = models.ForeignKey(User, db_column='i_updated_by', related_name='AfRole_updated_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_updated_on = models.DateTimeField(auto_now=True)
    e_status = models.CharField(max_length=1, choices=STATUS, blank=True, default="0")

    class Meta:
        db_table = 'af_role'

class AfMenuRole(models.Model):
    i_menu_role_id = models.AutoField(primary_key=True)
    i_menu = models.ForeignKey(AfMenu, blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    i_parent = models.ForeignKey(AfMenu, related_name='AfMenuRole_parent', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    i_role = models.ForeignKey(AfRole, blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    i_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    i_menu_action = models.ForeignKey(AfMenuAction, blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    i_created_by = models.ForeignKey(User, db_column='i_created_by', related_name='AfMenuRole_created_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_created_on = models.DateTimeField(auto_now_add=True)
    i_updated_by = models.ForeignKey(User, db_column='i_updated_by', related_name='AfMenuRole_updated_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_updated_on = models.DateTimeField(auto_now=True)
    e_status = models.CharField(max_length=1, choices=STATUS, blank=True, default="0")

    class Meta:
        db_table = 'af_menu_role'



class AfTimeZone(models.Model):
    i_time_zone_id = models.AutoField(primary_key=True)
    s_time_zone_name = models.CharField(max_length=100, blank=True, null=True)
    s_utc_offset = models.CharField(max_length=100, blank=True, null=True)
    i_created_by = models.ForeignKey(User, db_column='i_created_by', related_name='AfTimeZone_created_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_created_on = models.DateTimeField(auto_now_add=True)
    i_updated_by = models.ForeignKey(User, db_column='i_updated_by', related_name='AfTimeZone_updated_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_updated_on = models.DateTimeField(auto_now=True)
    e_status = models.CharField(max_length=1, choices=STATUS, blank=True, default="0")

    class Meta:
        db_table = 'af_time_zone'


class AfUserRole(models.Model):
    i_user_role_id = models.AutoField(primary_key=True)
    i_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    i_role = models.ForeignKey(AfRole, blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    e_access_type = models.BooleanField(default=False)
    e_default_role = models.BooleanField(default=False)
    i_created_by = models.ForeignKey(User, db_column='i_created_by', related_name='AfUserRole_created_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_created_on = models.DateTimeField(auto_now_add=True)
    i_updated_by = models.ForeignKey(User, db_column='i_updated_by', related_name='AfUserRole_updated_by', blank=True, null=True, on_delete=models.SET_DEFAULT, default="")
    dt_updated_on = models.DateTimeField(auto_now=True)
    e_status = models.CharField(max_length=1, choices=STATUS, blank=True, default="0")

    class Meta:
        db_table = 'af_user_role'




