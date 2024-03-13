from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, mixins,generics
from .models import Recipe,Review
from .serializers import RecipeSerializer,ReviewSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class=UserSerializer
class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
class ReviewView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


