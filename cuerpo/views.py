from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.
def listadoPosts(request):
    posts= Post.objects.filter(fechaPublicacion__lte= timezone.now()).order_by('fechaPublicacion')
    return render(request,'cuerpo/listadoPosts.html',{'posts':posts})