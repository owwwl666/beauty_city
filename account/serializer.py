from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.serializers import ModelSerializer

from .models import Registration


class RegistrationSerializer(ModelSerializer):
    phonenumber = PhoneNumberField(region="RU")

    class Meta:
        model = Registration
        fields = "__all__"

    def create(self, validated_data):
        user, _ = Registration.objects.get_or_create(
            firstname=validated_data.get("firstname"),
            lastname=validated_data.get("lastname"),
            phonenumber=validated_data.get("phonenumber")
        )

        return user
