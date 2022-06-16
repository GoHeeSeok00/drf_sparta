from rest_framework import serializers


from product.models import Event as EventModel

""""""
# Event serializer
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = ["title", "thumbnail", "information", "start_point", "end_point"]


# Active Now serializer
class ActiveNowEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = ["title", "thumbnail", "information", "start_point", "end_point"]