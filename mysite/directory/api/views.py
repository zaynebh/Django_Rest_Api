from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from directory.api.filtersets import UsersFilterSet
from directory.api.serializers import UserSerializer, CompanySerializer
from directory.models import User, Company

from rest_framework import filters
from django_filters import Filter, FilterSet
class UsersViewSet(viewsets.ModelViewSet):
    """
    Endpoint for returning User data.
    """
    filterset_class = UsersFilterSet
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def reports(self, request, pk):
        user = self.get_object()
        users = user.reports.all()
        page = self.paginate_queryset(users)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    def get_queryset():
        company=Company.objects.get(name='Test')
       
        return User.objects.filter(company='company')

    

class CompanyViewSet(viewsets.ModelViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class UserSearchViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)

    search_fields = ('company')





