from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer



class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('full_name', 'email', 'password', )