from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError

from .serializer import RegistrationSerializer


@api_view(["POST"])
def register_user(request):
    serializer_reg = RegistrationSerializer(data=request.data)
    try:
        serializer_reg.is_valid(raise_exception=True)
    except ValidationError:
        return HttpResponseRedirect(redirect_to='/api/reg_err')
    else:
        serializer_reg.save()
        return HttpResponseRedirect(redirect_to='/api/reg_succ')
