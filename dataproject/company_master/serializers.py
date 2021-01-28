from rest_framework import serializers


class AuthSerializer(serializers.Serializer):
    '''
    Serialize plot 1 data
    '''
    intervals = serializers.CharField()
    count = serializers.IntegerField()


class RegistrationSerializer(serializers.Serializer):
    '''
    Serialize plot 2 data
    '''
    DATE_OF_REGISTRATION__year = serializers.CharField()
    count = serializers.IntegerField()


class TopRegSerializer(serializers.Serializer):
    '''
    Serialize plot 3 data
    '''
    BUSINESS_ACTIVITY = serializers.CharField()
    count = serializers.IntegerField()


class PbaSerializer(serializers.Serializer):
    '''
    Serialize plot 4 data
    '''
    DATE_OF_REGISTRATION__year = serializers.CharField()
    BUSINESS_ACTIVITY = serializers.CharField()
    count = serializers.IntegerField()
