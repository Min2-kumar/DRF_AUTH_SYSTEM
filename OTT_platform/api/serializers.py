from rest_framework import serializers
from OTT_platform.models import Movie



# ModelSerializer automatically handle create & update logic 
# Topics:- ModelSerializer | serializerMethod(custome method) | validation
class MovieSerializer(serializers.ModelSerializer):
    len_of_name = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = '__all__'


    def get_len_of_name(self,object):
        return len(object.name)

    # 2. Object-level validation (multiple fields)
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and description should not be same")
        return data

    # 1. single field level validation | instead of this we used validators
    def validate_name(self, value):
        if len(value)<2:
            raise serializers.ValidationError("Name is too short !!")
        return value


# ---------------------------------------------------------------------------------------------

# 3. validators
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short !!")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

    # 2. Object-level validation (multiple fields)
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and description should not be same")
    #     return data

    # 1. single field level validation | instead of this we used validators
    # def validate_name(self, value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is too short !!")
    #     return value
