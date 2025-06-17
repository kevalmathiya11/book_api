from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from functools import wraps

def require_api_key(view_func):
    @wraps(view_func)
    def wrapped_view(self,request,*args, **kwargs):
        key = request.headers.get('x-api-key')
        if key != settings.API_KEY :
            return Response({"error":"INVALID_API_KEY","message": "missing or invalid API key"},status=status.HTTP_401_UNAUTHORIZED)
        return view_func(self,request,*args, **kwargs)
    return wrapped_view