from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from . import models
from django.conf import settings


class AfRoleGetSerializer(serializers.ModelSerializer):
    """
    Serializer to populate data into af_role model
    """
    class Meta:
        model = models.AfRole
        fields = '__all__' 


class AfRoleSerializer(serializers.ModelSerializer):
    """
    Serializer to return data for af_role info
    """
    class Meta:
        model = models.AfRole
        fields = ('s_role_name', 'i_user_type', 's_key', 'i_display_order', 'e_status')


class AfMenuGetSerializer(serializers.ModelSerializer):
    """
    Serializer to populate data into af_menu model
    """
    class Meta:
        model = models.AfMenu
        fields = '__all__'


class AfMenuSerializer(serializers.ModelSerializer):
    """
    Serializer to return data for af_menu info
    """
    class Meta:
        model = models.AfMenu
        fields = ('s_menu_name', 's_link', 'i_parent', 's_icon_class', 'i_display_order', 'e_status')


class AfUserTypeGetSerializer(serializers.ModelSerializer):
    """
    Serializer to populate data into af_user type model
    """
    class Meta:
        model = models.AfUserType
        fields = '__all__'


class AfUserTypeSerializer(serializers.ModelSerializer):
    """
    Serializer to populate data into af_user type model
    """
    class Meta:
        model = models.AfUserType
        fields = ('s_user_type_name', 'e_status')