from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from accounts.models import Profile
class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ('user', 'organization', 'country', 'city', 'url', )
        read_only_fields = ()
    def create(self, validated_data):
        return Profile.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.tagline = validated_data.get('tagline', instance.tagline)
        instance.save()
        update_session_auth_hash(self.context.get('request'), instance)
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')