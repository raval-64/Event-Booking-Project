from django.shortcuts import render,get_object_or_404,reverse,redirect
from .models import event,booking
from .forms import BookForm
from datetime import datetime
from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache

# Create your views here.
def index(request):
    request = del_session(request)
    try:
        event_list = {'event_list':event.objects.all()}
        return render(request,'event/event-list.html',event_list)
    except:
        return render(request,'event/event-list.html',{'error':'There are currently no events available.'})

@never_cache
def eventdetail(request,id):
    request = del_session(request)
    event_id = get_object_or_404(event,pk=id)
    if(event_id.seats==event_id.booked_seats):
        return redirect('/')
    else:
        if request.method == "POST":
            form = BookForm(request.POST or None)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                mobile = form.cleaned_data['mobile']
                book = booking(name=name, email=email, mobile=mobile, event=event_id)
                if(event_id.seats==event_id.booked_seats):
                    return redirect('/')
                eve = event.objects.get(id=event_id.id)
                eve.booked_seats = eve.booked_seats + 1
                eve.save()
                book.save()
                request.session['event_id'] = event_id.id
                request.session['context'] = {'id':book.id,'name':name,'email':email,'mobile':str(mobile)}
                return HttpResponseRedirect('/event/book-summary/')
            else:
                context = {'event_detail':event_id,'form': form}
                return render(request, 'event/event-view.html', context)
        else:
            form = BookForm()
            event_detail = {'event_detail':event_id,'form':form}
            request.session['event_id'] = event_id.id
            return render(request,'event/event-view.html', event_detail)
    
@never_cache
def booksummary(request):
    try:
        context = request.session['context']
        event_data = event.objects.get(id=request.session['event_id'])
    except (KeyError, event.DoesNotExist):
        event_data = None
        return redirect('/')   
    return render(request,'event/book-summary.html',{'event':event_data,'context':context})


def del_session(request):
    if 'context' in request.session:
        del request.session['context']
    if 'event_id' in request.session:
        del request.session['event_id']
    return request
    