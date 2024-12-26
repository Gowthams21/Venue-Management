from django.shortcuts import render, redirect
from home.models import Query
from home.models import Book


# Create your views here.
def home(request):
    return render(request, 'login.html')

# In your views.py, rename the function
def handle_query(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        ins = Query(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("Data has been saved to the database")
    return render(request, 'query.html')

def book(request):
    if request.method == 'POST':
        date = request.POST.get('date', '')
        time = request.POST.get('time', '')  
        organizer = request.POST.get('organizer', '')
        reason = request.POST.get('reason', '')
        venue = request.POST.get('venue', '')
        subvenue = request.POST.get('subvenue', '')  
        refreshments = request.POST.get('refreshments', '')
        chiller = request.POST.get('chiller', '')

        # Create a new Book instance and save it
        bk = Book(date=date, time=time, organizer=organizer, reason=reason, venue=venue, subvenue=subvenue, refreshments=refreshments, chiller=chiller)
        bk.save()
        print("Booking saved")
        return redirect('home')  # Redirect to home page after saving

    return render(request, 'booking.html')


def base(request):
    return render(request, 'base.html') 

def venues(request):
    return render(request, 'venues.html')
