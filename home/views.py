from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from home.models import ListModel,ListsModel

# Create your views here.

def home_page(request):
    return render(request, 'home.html')

def list(request,list_name):
    listItems = ListModel.objects
    arr=[]
    for item in listItems:
        if(item.list_type==int(list_name)):
            arr.append(item)
    return render(request, 'list.html', {'listItems': arr})

def add_list(request,list_name):
    print(list_name)
    if request.is_ajax() and request.method == 'POST':
        text = request.POST.get('item', 'qw')
    listItems = ListModel.objects
    i=0
    for item in listItems:
        i=i+1
    id=i
    if(i!=0):
        item = ListModel(list_id=id+1)
        item.list_item=text
        item.list_type=int(list_name)
    else:
        item = ListModel(list_id=1)
        item.list_item=text
        item.list_type=int(list_name)
    item.save()
    return HttpResponse("haha")

def updata_list(request,list_name):
    if request.is_ajax() and request.method == 'POST':
        text = request.POST.get('item', 'qw')
        print(text)
        itemid = request.POST.get('id', 555)
        print(int(itemid))
    listItems = ListModel.objects()
    for item in listItems:
        if(item.list_id==int(itemid)):
            updetaItem = item
    updetaItem.list_item = str(text)
    updetaItem.save()
    return HttpResponse("haha")

def delete_list(request,list_name):
    if request.is_ajax() and request.method == 'POST':
        itemid = request.POST.get('id', 555)
        listItems = ListModel.objects()
        for item in listItems:
            if(item.list_id==int(itemid)):
                item.delete()
            elif(item.list_id>int(itemid)):
                item.list_id = item.list_id -1
                item.save()
    return HttpResponse("haha")


def lists(request):
    lists = ListsModel.objects()
    return render(request,'lists.html',{'lists':lists})

def add_lists(request):
    if request.is_ajax() and request.method == 'POST':
        text = request.POST.get('item', 'qw')
    listItems = ListsModel.objects
    i=0
    for item in listItems:
        i=i+1
    id=i
    if(i!=0):
        item = ListsModel(list_id=id+1)
        item.list_name=text
    else:
        item = ListsModel(list_id=1)
        item.list_name=text
    item.save()
    return HttpResponse("haha")

def delete_lists(request):
    if request.is_ajax() and request.method == 'POST':
        itemid = request.POST.get('id', 555)

        listItems = ListsModel.objects()
        for item in listItems:
            if(item.list_id==int(itemid)):
                item.delete()
            elif(item.list_id>int(itemid)):
                item.list_id = item.list_id -1
                item.save()
    return HttpResponse("haha")