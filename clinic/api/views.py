from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class ServicesView(APIView):
    def get(self,request,*args,**kwargs):
        try:
            services=Services.objects.all()
            serialize=ServiceSerializer(services,many=True)
            return Response(data=serialize.data)
        except:
            return Response({"msg":"Data not exist"},status=status.HTTP_404_NOT_FOUND)


class ServiceInfoView(APIView):#http://127.0.0.1:8000/v1/services/{id}/
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        try:
            qs=Services.objects.get(id=id)
            serialize=ServiceSerializer(qs)
            return Response(data=serialize.data)
        except:
            return Response({"msg":"data not exist"},status=status.HTTP_404_NOT_FOUND)

class ServiceByCategoryView(APIView):#http://127.0.0.1:8000/v1/services/{id}/
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        try:
            qs=Services.objects.filter(category=id)
            serialize=ServiceSerializer(qs,many=True)
            return Response(data=serialize.data)
        except:
            return Response({"msg":"data not exist"},status=status.HTTP_404_NOT_FOUND)

    # def put(self,request,*args,**kwargs):
    #     id = kwargs.get("id")
    #     try:
    #         object = Ser.objects.get(id=id)
    #         serialize=MobileSerializer(data=request.data)
    #         if serialize.is_valid():
    #             object.name=serialize.validated_data.get("name")
    #             object.price=serialize.validated_data.get("price")
    #             object.band=serialize.validated_data.get("band")
    #             object.display=serialize.validated_data.get("display")
    #             object.processor=serialize.validated_data.get("processor")
    #             object.save()
    #             return Response(data=serialize.data)
    #     except:
    #         return Response({"msg": "data not exist"}, status=status.HTTP_404_NOT_FOUND)

    # def delete(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     try:
    #         object=Mobiles.objects.get(id=id)
    #         object.delete()
    #         return Response({"msg":"data deleted"})
    #     except:
    #         return Response({"msg":"data not exist"},status=status.HTTP_404_NOT_FOUND)

class BeauticianView(APIView):
    def get(self,request,*args,**kwargs):
        try:
            beauticians=Beautician.objects.all()
            serialize=BeauticianSerializer(beauticians,many=True)
            return Response(data=serialize.data)
        except:
            return Response({"msg":"data not found"},status=status.HTTP_404_NOT_FOUND)

class BeauticianDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        try:
            beautician=Beautician.objects.get(id=id)
            serialize=BeauticianSerializer(beautician)
            return Response(data=serialize.data)
        except:
            return Response({"msg":"Data not found"},status=status.HTTP_404_NOT_FOUND)

class MaleBeauticianView(APIView):
    def get(self,request,*args,**kwargs):
        try:
            beauticians=Beautician.objects.filter(gender="male")
            serialize=BeauticianSerializer(beauticians,many=True)
            return Response(data=serialize.data)
        except:
            return Response({"msg":"data not found"},status=status.HTTP_404_NOT_FOUND)


class TimeslotView(APIView):
    def get(self,request,*args,**kwargs):
        try:
            timeslots=Timeslots.objects.all()
            serialize=TimeslotSerializer(timeslots,many=True)
            return Response(data=serialize.data)
        except:
            return Response({"msg":"data not found"},status=status.HTTP_404_NOT_FOUND)

class TimeslotDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        try:
            timeslot=Timeslots.objects.get(id=id)
            serialize=TimeslotSerializer(timeslot)
            return Response(data=serialize.data)
        except:
            return Response({"msg":"Data not found"},status=status.HTTP_404_NOT_FOUND)
        
class AddonsByCategory(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        try:
            addons=AddOns.objects.filter(category=id)
            serialize=AddOnSerializer(addons,many=True)
            return Response(data=serialize.data)
        except:
            return Response({"msg":"Data not found"},status=status.HTTP_404_NOT_FOUND)
        

class CartAddView(APIView):
    def post(self,request,*args,**kwargs):
        info=request.data
        sid=info['sid']
        date=info['date']
        beautician=info['beautician']
        addon_name=info['addon']
        slot_id=info['slot_id']
        service=Services.objects.get(id=sid)
        cost=service.cost
        slot=Timeslots.objects.get(id=slot_id)
        time=slot.time
        addon=None
        if addon_name:
            addon=AddOns.objects.get(name=addon_name)
        if slot.status == 'available':
            if addon:
                cost+=addon.cost
                service_cart=ServiceCart.objects.create(user=request.user,service=service,timeslot=slot,date=date,cost=cost,time=time,beautician=beautician,addons=addon)
            else:
                service_cart=ServiceCart.objects.create(user=request.user,service=service,timeslot=slot,date=date,cost=cost,time=time,beautician=beautician)

        return Response(data=service_cart.id,status=status.HTTP_201_CREATED)