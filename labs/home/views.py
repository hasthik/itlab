from django.shortcuts import render,HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar
# Create your views here.
def index(request):
    return render(request,'index.html')

def aboutus(request):
    return HttpResponse("Hi this is my about")

def contact(request):
    return render(request,'contact.html')

def index(request,year,month):
    year = int(year)   
    month = int(month)    
    if year < 1900 or year > 2099: year = date.today().year    
    month_name = calendar.month_name[month]
    title = "MyClub Event Calendar -%s %s" % (month_name,year)
    cal = HTMLCalendar().formatmonth(year, month)
    return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal))