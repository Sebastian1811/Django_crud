from rest_framework.response import Response
from rest_framework.decorators import api_view
from plato.models import Plato
from plato.models import Alimento
from .serializers import PlatoSerializer
from .serializers import AlimentoSerializer



@api_view(['GET'])
def getPlatos(request):
    platos = Plato.objects.all()
    serializer = PlatoSerializer(platos,many=1)
    return Response(serializer.data)

@api_view(['GET'])
def getPlato(request,id):
    plato = Plato.objects.get(id=id)
    serializer = PlatoSerializer(plato)
    return Response(serializer.data)

@api_view(['GET'])
def getAlimentos(request):
    alimentos = Alimento.objects.all()
    serializer = AlimentoSerializer(alimentos,many=1)
    return Response(serializer.data)

@api_view(['GET'])
def getAlimento(request,id):
    alimento = Alimento.objects.get(id=id)
    serializer = AlimentoSerializer(alimento)
    return Response(serializer.data)
    
@api_view(['POST'])
def postPlato(request):
    serializer = PlatoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
@api_view(['POST'])
def postAlimento(request):
    serializer = AlimentoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
@api_view(['DELETE'])
def deletePlato(request,id):
    plato = Plato.objects.get(id=id)
    plato.delete()
    return Response(200)

@api_view(['DELETE'])
def deleteAlimento(request,id):
    alimento = Alimento.objects.get(id=id)
    alimento.delete()
    return Response(200)