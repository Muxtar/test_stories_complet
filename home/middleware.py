from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from accounts.models import BlockUser as ModelBlockUser

class BlockUser(MiddlewareMixin):
    def __call__(self, request: HttpRequest) -> HttpResponse:
        blokcUsers = ModelBlockUser.objects.all().values_list('user__username')
        username =  (request.user.username, )
        if username in blokcUsers  and request.path == '/en/stories/':
            return HttpResponse("<h1 style='color:red'>Sizin bu seifeye giris qadagandir</h1>")
        return super().__call__(request)

class BlockIp(MiddlewareMixin):
    def __call__(self, request: HttpRequest) -> HttpResponse:
        # # get users ip
        if request.META.get("REMOTE_ADDR") == '192.168.0.112':
            return HttpResponse("<h1 style='color:red'>Sayta giris qadagandir xais edirik 2 gun sonra yeniden ceht edin</h1>")
            
        return super().__call__(request)    