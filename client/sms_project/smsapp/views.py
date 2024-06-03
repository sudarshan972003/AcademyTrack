from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from .models import StudentModel
import requests
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Exists, OuterRef
import random
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response.get("ip")

def get_location(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "city": response.get("city", "Unknown"),
        "region": response.get("region", "Unknown"),
        "country": response.get("country_name", "Unknown"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude")
    }
    return location_data


def get_weather(latitude, longitude):
    weather_api_key = '81e58cb1ac3fefa0e7e36112ec7d3789'
    if latitude and longitude:
        weather_response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid={weather_api_key}')
        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            temperature = weather_data.get('main', {}).get('temp')
            return temperature
    return None


def home(request):
    if request.user.is_authenticated:
        try:
            # Fetch quotes from the API
            quotes_response = requests.get('https://starc00009.pythonanywhere.com/')
            if quotes_response.status_code == 200:
                quotes = quotes_response.json()
                # Get a random quote from the list
                random_quote = random.choice(quotes)
                quote_text = random_quote['quote']
                quote_author = random_quote['author']
            else:
                quote_text = "Failed to fetch quote"
                quote_author = "Unknown"

            ip_address = get_ip()
            location_data = get_location(ip_address)
            latitude, longitude = location_data.get('latitude'), location_data.get('longitude')
            temperature = get_weather(latitude, longitude)
        except Exception as e:
            print(f"Error fetching data: {e}")
            location_data = {
                "city": 'Unknown',
                "region": 'Unknown',
                "country": 'Unknown',
                "latitude": None,
                "longitude": None
            }
            temperature = None

        return render(request, 'home.html', {'location': location_data, 'temperature': temperature, 'quote_text': quote_text, 'quote_author': quote_author})
    else:
        return redirect("ulogin")


def addstudent(request):
	if request.user.is_authenticated:
		error_message = ""
		if request.method == 'POST':
			name = request.POST['name']
			roll_number = request.POST['roll_number']
			if StudentModel.objects.filter(user=request.user, rno=roll_number).exists():
				message = "<div style='text-align: center; margin-top: 50px; font-size: 35px;'>You already have a student with this roll number. GO BACK !!</div>"
				return HttpResponseBadRequest(message)
			mobile = request.POST['mobile']
			email = request.POST['email']
			marks1 = request.POST['marks1']
			marks2 = request.POST['marks2']
			marks3 = request.POST['marks3']
			marks4 = request.POST['marks4']
			marks5 = request.POST['marks5']
            
			roll_number_exists = StudentModel.objects.filter(user=request.user, rno=roll_number).exists()
			if roll_number_exists:
				error_message = "Roll number {} already exists.".format(roll_number)
			else:
				student = StudentModel(
					user=request.user,
					name=name,
					rno=roll_number,
					mobile=mobile,
					email=email,
					marks1=marks1,
					marks2=marks2,
					marks3=marks3,
					marks4=marks4,
					marks5=marks5
				)
				student.save()
				return redirect('showstudent')
            
		return render(request, 'addstudent.html', {'error_message': error_message})
	else:
		return redirect("ulogin")


def showstudent(request):
	if request.user.is_authenticated:
		students = StudentModel.objects.filter(user=request.user)
		return render(request, 'showstudent.html', {'students': students})
	else:
		return redirect("ulogin")


def updatestudent(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            roll_number = request.POST.get('roll_number')
            try:
                student = StudentModel.objects.get(rno=roll_number, user=request.user)
                student.name = request.POST.get('name')
                student.mobile = request.POST.get('mobile')
                student.email = request.POST.get('email')
                student.marks1 = request.POST.get('marks1')
                student.marks2 = request.POST.get('marks2')
                student.marks3 = request.POST.get('marks3')
                student.marks4 = request.POST.get('marks4')
                student.marks5 = request.POST.get('marks5')
                student.save()
                return redirect('showstudent')
            except StudentModel.DoesNotExist:
                error_message = "Student with roll number {} does not exist.".format(roll_number)
                return render(request, 'updatestudent.html', {'error_message': error_message})
        return render(request, 'updatestudent.html')
    else:
        return redirect("ulogin")


def deletestudent(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            roll_number = request.POST.get('roll_number')
            try:
                student = StudentModel.objects.get(rno=roll_number, user=request.user)
                student.delete()
                return redirect('showstudent')
            except ObjectDoesNotExist:
                error_message = "Student with roll number {} does not exist.".format(roll_number)
                return render(request, 'deletestudent.html', {'error_message': error_message})
        return render(request, 'deletestudent.html')
    else:
        return redirect("ulogin")


def ulogin(request):
	if request.user.is_authenticated:
		return redirect("home")
	else:
		if request.method == "POST":
			un = request.POST.get("un")
			pw = request.POST.get("pw")
			usr = authenticate(username=un, password=pw)
			if usr is None:
				msg = "Check username/password"
				return render(request,"ulogin.html",{"msg":msg})
			else:
				login(request,usr)
				return redirect("home")
		else:
			return render(request,"ulogin.html")

def usignup(request):
	if request.user.is_authenticated:
		return redirect("home")
	else:
		if request.method == "POST":
			un = request.POST.get("un")
			pw1 = request.POST.get("pw1")
			pw2 = request.POST.get("pw2")
			if pw1 == pw2:
				try:
					usr = User.objects.get(username=un)
					msg = "User already exists"
					return render(request,"usignup.html",{"msg":msg})
				except User.DoesNotExist:
					usr = User.objects.create_user(username=un, password=pw1)
					usr.save()
					return redirect("ulogin")
			else:
				msg = "Password did not match"
				return render(request,"usignup.html",{"msg":msg})
		else:
			return render(request,"usignup.html")

def ulogout(request):
	logout(request)
	return redirect("ulogin")






















