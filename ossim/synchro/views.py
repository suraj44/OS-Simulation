from django.shortcuts import render

# Create your views here.
from . models import SynchroAlg


def semaphores(request):

    return render(request, 'synchro/semaphores_index.html')

def socket(request):
    algos = SynchroAlg.objects.filter(demourl="tcp")
    context = {'algos': algos}
    return render(request, 'synchro/socket_index.html',context = context)


def sem_demo(request,pk):
    if(pk=='1'):
        return render(request, 'synchro/prodcon2.html')
    if(pk=='2'):
        return render(request, 'synchro/readerwriter.html')
    if(pk=='3'):
        return render(request, 'synchro/diningphils.html')
    if(pk=='4'):
        return render(request, 'synchro/cigsmoker.html')

def socket_demo(request,pk):
    if(pk=='1'):
        return render(request, 'synchro/TCP.html')
    if(pk=='2'):
        return render(request, 'synchro/UDP.html')
