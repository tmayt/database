from django.http import JsonResponse
from .models import Data
from django.views.decorators.csrf import csrf_exempt

def get_data(request):
    try:
        d = Data.objects.get(key=request.GET.get('key'),user=request.GET.get('user'))
        js = {
            'key': d.key,
            'value': d.value,
            'user': d.user,
        }
        return JsonResponse(js)
    except:
        return JsonResponse({'status':'error'}, status=500)
            
@csrf_exempt
def set_data(request):
    try:
        Data.objects.create(
            key = request.POST.get('key'),
            value = request.POST.get('value'),
            user = request.POST.get('user')
        )
        return JsonResponse({'status':'OK'})
    except:
        return JsonResponse({'status':'error'}, status=500)