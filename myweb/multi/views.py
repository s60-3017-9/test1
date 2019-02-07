from django.shortcuts import render

# Create your views here.
def show(request,number):
    # s=[]
    # for i in range(1,12):
    #     s.append(number*i)
    n = str(number)*3
    context={'number':n}


    return render(request,'multi/show.html',context)
