from ast import Delete
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Ejercicios
from django.http import JsonResponse
from django.utils.decorators import method_decorator
import json
from django.forms.models import model_to_dict

# Create your views here.
class EjerciciosListView(View) :
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        cList = Ejercicios.objects.all ()
        return JsonResponse(list(cList.values()), safe=False)
     
    def post(self, request) :
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Ejercicios.objects.create(titulo=jd['titulo'], descripcion=jd['descripcion'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def put(self, request, pk) :
            jd = json.loads(request.body)
            dLista = Ejercicios.objects.get(pk=pk)
            Ejercicios.objects.update_or_create(titulo=jd['titulo'], descripcion=jd['descripcion'])
            datos = {'message': "Success"}
            return JsonResponse(datos)
        
    def delete(self, request, id):
            clist = Ejercicios.objects.filter(id=id)
            
            datos = {'message': "Success"}
            return JsonResponse(clist)
            
        

        
            
class EjercicioDetalladoView(View):
        def get(self, request, pk):
            list = Ejercicios.objects.get(pk=pk)
            return JsonResponse (model_to_dict(list))
        

