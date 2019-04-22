from django.shortcuts import render
from . import serializers
from rest_framework import status
from rest_framework.views import APIView
from webapp.api_utils import utils as api_utils
from . import models
from rest_framework import serializers as af_serializer
from rest_framework.response import Response

class AfRoleMaster(APIView):
	"""
		API for Role Master Management
	"""
	def get(self, request):
		"""
		List all the Role records according to the filter applied
		"""

		i_user_type = request.GET.get('i_user_type', None)
		e_status = request.GET.get('e_status', None)

		if i_user_type:
			try:
				role_master_list = models.AfRole.objects.filter(i_user_type=int(i_user_type))
			except models.AfRole.DoesNotExist:
				return api_utils.response({"message": "error"}, status.HTTP_400_BAD_REQUEST,
									  'No record found')
		elif e_status:
			try:
				role_master_list = models.AfRole.objects.filter(e_status=int(e_status))
			except models.AfRole.DoesNotExist:
				return api_utils.response({"message": "error"}, status.HTTP_400_BAD_REQUEST,
									  'No record found')
		else:
			try:
				role_master_list = models.AfRole.objects.all()
				serializer = serializers.AfRoleGetSerializer(role_master_list, many=True)
			except models.AfRole.DoesNotExist:
				return api_utils.response({"message": "error"}, status.HTTP_400_BAD_REQUEST,
									  'No record found')
		return Response({'result':serializer.data})	


	def post(self, request):
		"""
		Create new Role to the system
		"""
		serializer = serializers.AfRoleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return api_utils.response({"message": "success"}, status.HTTP_200_OK)
		return api_utils.response({"message": "error"}, status.HTTP_400_BAD_REQUEST,
								  api_utils.generate_error_message(serializer.errors))


class AfUserTypeMaster(APIView):
	"""
		API for User Type Management
	"""
	def get(self, request):
		"""
		List all the User type records according to the filter applied
		"""
		try:
			usertype_master_list = models.AfUserType.objects.all()
		except models.AfUserType.DoesNotExist:
			return api_utils.response({"message": "error"}, status.HTTP_400_BAD_REQUEST,
									  'No record found')
		serializer = serializers.AfUserTypeGetSerializer(usertype_master_list, many=True)
		return Response({'result':serializer.data})	
	
	def post(self, request):
		"""
		Create new User type to the system
		"""
		serializer = serializers.AfUserTypeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return api_utils.response({"message": "success"}, status.HTTP_200_OK)
		return api_utils.response({"message": "error"}, status.HTTP_400_BAD_REQUEST,
								  api_utils.generate_error_message(serializer.errors))


class AfMenuMaster(APIView):
	"""
		API for Menu Master Management
	"""
	def get(self, request):
		"""
		List all the Menu records according to the filter applied
		"""
		try:
			menu_master_list = models.AfMenu.objects.all()
		except models.AfMenu.DoesNotExist:
			return api_utils.response({"message": "error"}, status.HTTP_400_BAD_REQUEST,
									  'No record found')
		serializer = serializers.AfMenuGetSerializer(menu_master_list, many=True)
		return Response({'result':serializer.data})	


	def post(self, request):
		"""
		Create new Role to the system
		"""
		serializer = serializers.AfMenuSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return api_utils.response({"message": "success"}, status.HTTP_200_OK)
		return api_utils.response({"message": "error"}, status.HTTP_400_BAD_REQUEST,
								  api_utils.generate_error_message(serializer.errors))