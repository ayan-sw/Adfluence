#-*- coding: utf-8 -*-

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    """
     This class is necessary to create if using custom user model is desired
    """

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """

        email = self.normalize_email(email)
        extra_fields['s_user_name'] = extra_fields['s_user_name'] if extra_fields.get('s_user_name') else email
        user = self.model(s_email=email, is_staff=is_staff, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return: creates a super user
        """
        u = self.create_user(kwargs['s_email'], password=kwargs['password'])
        u.s_user_name = kwargs['s_email']
        u.is_staff = True
        u.save(using=self._db)
        return u

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)