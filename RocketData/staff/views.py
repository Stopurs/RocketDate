from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Staffmodels
from .serializers import StaffSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StaffView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        staff = Staffmodels.objects.filter(position='A')
        serializer = StaffSerializer(staff, many=True)
        return Response({"staff": serializer.data})


class Filter_B(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        staff = Staffmodels.objects.filter(position='B')
        serializer = StaffSerializer(staff, many=True)
        return Response({"staff": serializer.data})


class Filter_C(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        staff = Staffmodels.objects.filter(position='C')
        serializer = StaffSerializer(staff, many=True)
        return Response({"staff": serializer.data})


class Filter_D(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        staff = Staffmodels.objects.filter(position='D')
        serializer = StaffSerializer(staff, many=True)
        return Response({"staff": serializer.data})


class Filter_E(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        staff = Staffmodels.objects.filter(position='E')
        serializer = StaffSerializer(staff, many=True)
        return Response({"staff": serializer.data})

