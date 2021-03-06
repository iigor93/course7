from bot.models import TgUser
from bot.serializers import CheckVerificationCodeSerializer
from bot.tg.client import TgClient

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

import redis

from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


class CheckVerificationCode(generics.GenericAPIView):
    """Проверка кода и привязка пользователя Телеграмм и django"""
    model = TgUser
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CheckVerificationCodeSerializer
    redis_instance = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, decode_responses=True)

    def patch(self, request, *args, **kwargs):
        instance = self.get_queryset()
        instance.user = request.user
        instance.save()
        tg_client = TgClient() 
        tg_client.send_message(chat_id=instance.chat_tgid, text='Verification done')
        
        return Response()
        
    def get_queryset(self): 
        verification_code = self.request.data.get('verification_code')
        tg_userid = self.redis_instance.get(verification_code)
        try:
            return TgUser.objects.filter(user_tgid=tg_userid).get()
        except ObjectDoesNotExist:
            raise ValidationError({'code': 'wrong code'})
