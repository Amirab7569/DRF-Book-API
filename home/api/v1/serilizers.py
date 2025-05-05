from rest_framework import serializers
from ...models import Book, CustomUser

class BookSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ["author"]
        
    # get url and show 
    def get_abs_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    # Change show data in detail
    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('absolute_url',None)
            rep.pop('snippet',None)
        else:
            rep.pop('body',None)
        return rep
        
    # if srz valid : create in db 
    def create(self, validated_data):
        validated_data['author'] = CustomUser.objects.get(pk=self.context.get('request').user.id)
        return super().create(validated_data)