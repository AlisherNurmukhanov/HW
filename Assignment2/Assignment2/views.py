from django.shortcuts import render
from Assignment2.models import UserModel
from django.contrib import messages

def showuser(request):
    showall = UserModel.objects.all()
    return render(request,'Index.html', {"data":showall} )



def Insertuser(request):
    if request.method == "POST":
        if request.POST.get('email') and request.POST.get('name') and request.POST.get('surname') and request.POST.get('salary') and request.POST.get('phone') and request.POST.get('cname'):
            saverecord = UserModel()
            saverecord.email = request.POST.get('email')
            saverecord.name = request.POST.get('name')
            saverecord.surname = request.POST.get('surname')
            saverecord.salary = request.POST.get('salary')
            saverecord.phone = request.POST.get('phone')
            saverecord.cname = request.POST.get('cname')
            saverecord.save()
            messages.success(request,'User '+ saverecord.name + ' is saved successfully!')
            return render(request,'Insert.html')
    else:
            return render(request,'Insert.html')

def Edituser(request, id):


    edituserobj = UserModel.objects.get(id = email)

    return render(request, 'Edit.html',{"UserModel":edituserobj})

#def Deleteuser(request, email)
