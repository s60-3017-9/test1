from django.shortcuts import render

# Create your views here.
def show(request,number):
    s=[]
    for i in range(1,13):
        s.append(number*i)
    # n = str(number)*3
    context={'number':number,'list_number':s}


    return render(request,'multi/show.html',context)

def input(request):
    try:
        number=int(request.POST['num_input'])
        s = []
        for i in range(1, 13):
            s.append(number * i)
        context = {'number': number, 'list_number': s}
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
