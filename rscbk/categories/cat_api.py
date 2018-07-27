from rest_framework import serializers
from .models import Items

class NoteSerialiser(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Items
        fields = ('id', 'item_name',)


from rest_framework import viewsets

class NoteViewSet(viewsets.ModelViewSet):

    queryset = Items.objects.all()
    serializer_class = NoteSerialiser