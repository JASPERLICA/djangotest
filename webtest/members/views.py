from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from members import models


def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())
    #return HttpResponse("hello world ")
# Create your views here.
def show(request):
    data = models.Manager.objects.all()
    return render(request, 'show_UI.html', {'data_list': data})


def write_in(request):
    if request.method == 'GET':
        return render(request, 'write.html')

    id = request.POST.get('id')
    name = request.POST.get('name')
    date = request.POST.get('date')
    time = request.POST.get('time')
    #image = request.POST.get('image')
    #models.Manager.objects.create(id=id, name=name, date=date, time=time, image=image)
    models.Manager.objects.create(id=id, name=name, date=date, time=time)

    return redirect('/show')

