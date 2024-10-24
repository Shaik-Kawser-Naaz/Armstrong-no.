from django.shortcuts import render

# Create your views here.
def func1(request):
    result=None
    print(request.GET)
    if request.method=="POST":
        a=int(request.POST.get('snum'))
        k=a
        l=[]
        p=0
        while a!= 0:
            m = a%10
            l.append(m)
            a= a//10
        for i in l:
            i = i**len(str(k))
            p+=i
        if k == p:
            result=True
        else:
            result=False
    return render(request,'index.html',{'res':result})        
