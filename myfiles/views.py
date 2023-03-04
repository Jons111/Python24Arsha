import datetime



from django.db.models import Q
from django.shortcuts import render
from myfiles.models import  Portfolio,Murojaat
# Create your views here.
def index(request):
    if 'text' in request.POST:
        malumot = request.POST.get('text')
        soz = str(malumot).strip()
        qidirish = Q(nomi__contains=soz) | Q(comp_name__contains =soz)|Q(url__contains =soz)|\
                   Q(date__contains =soz)|Q(text__contains =soz)|Q(tur__nomi__contains =soz)
        port = Portfolio.objects.filter(qidirish)
        return render(request, 'index.html', {'works': port})
    if 'name' in request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        vaqt = datetime.datetime.now()
        Murojaat(ism=name,mail=email,sub=sub,text=msg,date=vaqt).save()
    port  = Portfolio.objects.all()
    return render(request,'index.html',{'works':port})
def portifilyo_detalis(request,id):
    port = Portfolio.objects.get(id=id)
    return render(request,'portfolio-details.html',{'work':port})