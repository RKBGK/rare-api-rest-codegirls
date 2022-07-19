"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from datetime import datetime
from rarerestapi.models.rareuser import RareUser

from rarerestapi.models.subscription import Subscription

# from rest_framework.decorators import  permission_classes
# from rest_framework.permissions import AllowAny

class SubscriptionView(ViewSet):
    """Level up game types view"""  

        
    # @permission_classes([AllowAny])
    def list(self, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        print('*' * 100)
        print(serializer)
        return Response(serializer.data)

 
        # author_subs = request.query_params.get('user', None)
        # print('*' * 100)
        # print(author_subs)

        # if author_subs is not None:
        #     authsubs = subscriptions.filter(followerid=author_subs)
            
        #  # Set the `joined` property on every event
        # for authsub in  authsubs:
        #     # Check to see if the gamer is in the attendees list on the event
        #     follower = RareUser.objects.get(user=request.auth.user)
        #     authsub.subscribed = follower in follower.followers.all()          
    # @action(methods=['post'], detail=True)
    # def signup(self, request, pk):
    #     """Post request for a user to sign up for an event"""
    
    #     gamer = Gamer.objects.get(user=request.auth.user)
    #     event = Event.objects.get(pk=pk)
    #     event.attendees.add(gamer)
    #     return Response({'message': 'Gamer added'}, status=status.HTTP_201_CREATED)
    
    # @action(methods=['delete'], detail=True)
    # def leave(self, request, pk):
    #     """Post request for a user to sign up for an event"""
    
    #     gamer = Gamer.objects.get(user=request.auth.user)
    #     event = Event.objects.get(pk=pk)
    #     event.attendees.remove(gamer)
    #     return Response({'message': 'Gamer removed'}, status=status.HTTP_201_CREATED)
    
class SubscriptionSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Subscription
        fields = ('id', 'created_on', 'deleted_on', 'author', 'follower')
        
class CreateSubscriptionSerializer(serializers.ModelSerializer):
    # created_on = datetime.today().strftime('%Y-%m-%d')
    # deleted_on = datetime.today().strftime('%Y-%m-%d')
    class Meta:
        model = Subscription
        fields = ['author', 'follower','created_on', 'deleted_on']  