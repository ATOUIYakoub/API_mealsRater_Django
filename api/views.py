from rest_framework import viewsets
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User


# Create your views here.
class MealViewsets(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    
    @action(methods='POST',detail=True)
    def rate_meal(self, REQUEST, pk=None):
        if 'stars' in request.data:
            '''create or update'''
            meal = Meal.objects.get(id=pk)
            username = request.data['username']
            stars = request.data['stars']
            user = User.objects.get(username=username)
            
            try:
                #update
                rate = Rating.objects.get(user=user.id , meal=meal.id)
                rating.stars = stars
                rating.save
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'meassage':'meal Rate updated',
                    'result':serializer.data
                }
                return Response(json, status=status.HTTP_400_BAD_REQUEST)
            except:
                #create
                rating = Rating.objects.create(stars=stars,meal=meal,user=user)
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'meassage':'meal Rate created',
                    'result':serializer.data
                }
                return Response(json, status=status.HTTP_200_OK)
            
        else:
            json = {
                'message':'stars not provided'
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)
    
class RatingViewsets(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer