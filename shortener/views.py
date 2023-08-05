import csv

from django.http import HttpResponse, HttpResponseRedirect,HttpRequest
from django.views import View

from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import UrlSerializer
from .forms import UrlForm
from .tasks import *

from django.shortcuts import render

class Index(View):

    def get(self,request:HttpRequest):
        url_form = UrlForm()
        context = {
            'form':url_form,
        }
        return render(request,'shortener/index.html',context)
    
    def post(self,request:HttpRequest):
        form = UrlForm(request.POST)
        print(f"Hello{form.changed_data}")
        url_form = UrlForm()
        if form.is_valid():
            new_url = form.save()
            context = {
                'form':url_form,
                'url':new_url
            }
            return render(request,'shortener/url.html',context)
        else:
            context = {
                'form':url_form,
                'error':'Something went wrong!'
            }            
            return render(request,'shortener/url.html',context)



class UrlListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UrlSerializer
    queryset = Url.objects.all()


class UrlShortener(APIView):
    def post(self, request, origin_uri):
        try:
            url = Url.objects.get(url=origin_uri)
        except:
            url = Url(url=origin_uri)
            url.save()

        short_url = url.short_url

        return Response(short_url)
        

class UrlView(APIView):
    def get(self, request, hash):
        url = Url.objects.get(url_hash=hash)
        url = url.url
        
        return HttpResponseRedirect(url)


class UrlExport(APIView):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'

        writer = csv.writer(response)
        fields = Url.objects.all().values_list('url', 'short_url')

        for row in fields:
            writer.writerow(row)

        return response
