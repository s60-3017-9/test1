from django.shortcuts import render
from .models import number

# Create your views here.
def show(request,number):
    s=[]
    for i in range(1,13):
        s.append(number*i)
    context={'number':number,'list_number':s}


    return render(request,'multi/show.html',context)

def input(request):
    try:
        str_num=(request.POST['num_input'])
        num=int(str_num)
        s = []
        for i in range(1, 13):
            s.append(num * i)
        context = {'number': num, 'list_number': s}
        if len(number.objects.filter(number_text=str_num))==0:
            number.objects.create(number_text=str_num)
        else:
            q=number.objects.get(number_text=str_num).count
            q+=1
            q.save()

        return render(request, 'multi/input.html', context)
    except (KeyError,ValueError):
        return render(request, 'multi/input.html')

# def show_input(request):
#     number=request.POST['num_input']
#     s=[]
#     for i in range(1,13):
#         s.append(number*i)
#     context = {'number': number, 'list_number': s}
#     return render(request, 'multi/input.html', context)
