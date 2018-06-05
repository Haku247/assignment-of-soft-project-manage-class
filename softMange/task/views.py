from django.shortcuts import render

# Create your views here.
from .models import *

def check(func):
    def wrapper(request):
        context = dict()
        account = request.session.get('account')
        if account:
            print('flag')
            context['account'] = account
        return func(request,context)
    return wrapper

@check
def home(request,context):
    return  render(request, 'home.html', context)

@check
def publish(request,context):
    if request.method == 'POST':
        data = request.POST
        t = Task(publisher=context['account'],
               name=data['name'],
               describe=data['describe'],
               start=data['start'],
               period=data['period'],
               cost =data['cost'],
               status=0,)
        t.save()
        q = Task.objects.filter(publisher=context['account']).order_by('-id')
        context['published_task'] = q
    return render(request, 'published.html', context)

@check
def published(request,context):
    q = Task.objects.filter(publisher=context['account'])
    context['published_task'] = q
    return render(request, 'published.html', context)

@check
def complete(request,context):
    if request.method=='POST':
        q=Task.objects.get(id=request.POST['id'])
        q.completed=True
        q.save()
        q=Task.objects.filter(publisher=context['account'])
        context['published_task']=q
        return render(request,'published.html',context)

@check
def receive(request,context):
    if context.get('account'):
        receivable = Task.objects.filter(receiver='')
        context['receivable'] = receivable
    return render(request, 'receive.html',context)

@check
def receive_get(request,context):
    if request.method == 'POST':
        q = Task.objects.get(id=request.POST['id'])
        if q.receiver == '':
            q.receiver = request.POST['receiver']
            q.save()
            return render(request,'received.html',context)
    return render(request,'receive.html',context)


@check
def received(request,context):
    q = Task.objects.filter(receiver=context['account'])
    context['received_task'] = q
    return render(request, 'received.html',context)

@check
def received_report(request,context):
    if request.method == 'POST':
        q = Task.objects.get(id=request.POST['id'])
        q.status = request.POST['status']
        q.save()
        q=Task.objects.filter(receiver =request.POST['receiver'])
        context['received_task']=q
        return render(request,'received.html',context)
    #return render(request,'received.html',context)


@check
def me(request,context):
    return render(request, 'me.html', context)

def signin(request):
    context = dict()
    if request.method == 'POST':
        account = context['account'] = request.POST['user_id']
        query = User.objects.get(account=account)
        if query:
            if request.POST['pswd'] == query.pswd:
                request.session['account'] = account
                return render(request, 'home.html', context)
        else:
            pass #account is not available
    else:
        return render(request, 'home.html', context)

def register(request):
    context = dict()
    if request.method == 'POST':
        account = context['account'] = request.POST['user_id']
        query = User.objects.filter(account=account)
        if not query:
            u = User(account=request.POST['user_id'],
                     pswd=request.POST['pswd'],
                     email=request.POST['email'],
                     phone=request.POST['phone'])
            u.save()
            request.session['account'] = account
            return render(request, 'home.html', context)
        else:
            pass #account is not available
    else:
        return render(request, 'home.html', context)

def log_out(request):
    return render(request, 'home.html')