from django.shortcuts import render

# Create your views here.
def show(request,number):
    s=[]
    n=[]
    for i in range(1,13):
        s.append(number*i)
        n.append(i)
    # n = str(number)*3
    context={'number':number,'list_number':s,'list_n':n}


    return render(request,'multi/show.html',context)
