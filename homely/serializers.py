from rest_framework import serializers
from models import PropertyDetails,HomeOwnerAccount
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username','first_name','last_name','email','is_staff')
class HomeOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeOwnerAccount
        fields = ('id','name','contact_number')
	# def create
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.contact_number = validated_data.get('contact_number',instance.contact_number)
        instance.save()
        return instance
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return HomeOwnerAccount.objects.create(**validated_data)

class PropertyDetailSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=100, default=None)
    # city = serializers.CharField(max_length=100)
    # state = serializers.CharField(max_length=100)
    # country = serializers.CharField(max_length=100)
    # zip_code = serializers.IntegerField()
    # home_owner = serializers.ForeignKey(HomeOwnerAccount)
    # contact_number = serializers.CharField(max_length=100)
    #user_id = serializers.IntegerField()

    class Meta:
    	model = PropertyDetails
    	fields = ('id','created','title',
    		'city','state','country','zip_code','owner','reservation_status')
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return PropertyDetails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.created = validated_data.get('created', instance.created)
        instance.title = validated_data.get('title', instance.title)
        instance.title = validated_data.get('city', instance.city)
        instance.city = validated_data.get('owner', instance.owner)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance
class HomeOwnerAccountSerializer(serializers.ModelSerializer):
	# owner_property = serializers.PrimaryKeyRelatedField(
	# 	many=True, read_only=True)
    property_details = PropertyDetailSerializer(many=True,read_only=False)
    class Meta:
        model = HomeOwnerAccount
        fields = ('name','contact_number','property_details')
    def create(self, validated_data):
    	# import ipdb
    	# ipdb.set_trace()
        # print validated_data
        property_details_data = validated_data.pop('property_details')
        
        owner = HomeOwnerAccount.objects.create(**validated_data)
        for property_detail_data in property_details_data:
            PropertyDetails.objects.create(owner=owner, **property_detail_data)
        return owner
    def update(self,owner,validated_data):
    	property_details_data = validated_data.pop('property_details')
        
        for property_detail_data in property_details_data:
            PropertyDetails.objects.update(owner=owner, **property_detail_data)
        return owner
    	# owner.contact_number = validated_data.get('contact_number',
    	# 	owner.contact_number)
    	# owner.name = validated_data.get('name',owner.name)
    	# owner.save()
    	# owner_property_details = validated_data.get('property_details')
     #    if owner_property_details:
     #    	# owner = HomeOwnerAccount.objects.create(**validated_data)
     #    	for property_detail_data in owner_property_details_data:
     #        	owner_id = property_detail_data.get('owner',None)
     #        	if owner_id:
     #        		owner_property_data = PropertyDetails.objects.get(
     #        			owner=owner_id,)
     #        	PropertyDetails.objects.update(owner=owner, **property_detail_data)
        # return owner

