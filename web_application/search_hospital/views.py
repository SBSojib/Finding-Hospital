from django.shortcuts import render
from fpdf import FPDF
from .mySQLDB import MySQLDB
from .location import Location
from .pdf_creator import PDF_Creator
from .email_sender import Email_Sender
from .PDF import PDF
from django.views.decorators.csrf import csrf_protect

import subprocess


def hi(request):
    return render(request, 'search_hospital/hello.html')


def test_page(request):
    return render(request, 'search_hospital/test.html')

"""
def hospital_details(request):
    return render(request, 'search_hospital/hospital_details.html')

"""
def show_hospital(request):

    if request.method == 'POST':

        name = request.POST['name']
        number = request.POST['number']
        email1 = request.POST['email1']
        email2 = request.POST['email2']
        reservation = request.POST['reservation']
        data_time = request.POST['date_time']
        address = request.POST.get('address')
        message = request.POST.get('message')

        creator = PDF_Creator()
        creator.generate_pdf(name, number, email1, reservation, data_time, address, message)

        emailer = Email_Sender()
        emailer.send_mail(email2)

    hospital_list = []

    db = MySQLDB()
    institution = db.select_institution()

    for x in institution:
        person = []

        id = str(x[0])
        type = x[1]
        location = x[2]
        name = x[3]

        lat_lon = location.split(" ")
        lat = lat_lon[0]
        lon = lat_lon[1]

        loc = Location()
        current_lat, current_lon = loc.get_location()
        #print(current_lon)

        if lat == current_lat and lon == current_lon:
            hosp = []
            hospital = db.select_hospital(id)
            hosp.append(name)
            hosp.append(hospital[0][1])
            hosp.append(hospital[0][2])
            hosp.append(hospital[0][3])
            hosp.append(hospital[0][4])
            hosp.append(hospital[0][5])
            hosp.append(hospital[0][6])
            hosp.append(hospital[0][7])
            hosp.append(hospital[0][8])

            hospital_list.append(hosp)

    return render(request, "search_hospital/result_hospital.html", {'result': hospital_list})


def choose_specialist(request):

    if request.method == 'POST':

        name = request.POST['name']
        number = request.POST['number']
        email1 = request.POST['email1']
        email2 = request.POST['email2']
        reservation = request.POST['reservation']
        data_time = request.POST['date_time']
        address = request.POST.get('address')
        message = request.POST.get('message')

        creator = PDF_Creator()
        creator.generate_pdf(name, number, email1, reservation, data_time, address, message)

        emailer = Email_Sender()
        emailer.send_mail(email2)

    db = MySQLDB()
    specialist_type = db.select_specialist_type()
    s_type = []
    for t in specialist_type:
        t = str(t)
        t = t.replace(",", "")
        t = t.replace("'", "")
        t = t.replace("(", "")
        t = t.replace(")", "")
        s_type.append(t)
    print(s_type)
    return render(request, "search_hospital/choose_specialist.html", {'result': s_type})

def show_specialist(request):

    if request.method == 'POST':

        specialist_in = request.POST.get('btn', False)


    doctor_list = []

    db = MySQLDB()
    doctors = db.select_specialist(specialist_in)

    for x in doctors:
        doctor = []
        doctor.append(specialist_in)

        id = str(x[2])
        cost = str(x[5])
        doctor.append(id)
        doctor.append(cost)

        db = MySQLDB()
        doc = db.select_doctor(id)

        for d in doc:
            print(d)
            name = str(d[1])
            degree = str(d[2])
            year = str(d[3])
            work_place = str(d[4])

        doctor.append(name)
        doctor.append(degree)
        doctor.append(year)
        doctor.append(work_place)

        doctor_list.append(doctor)

    return render(request, "search_hospital/result_specialist.html", {'result': doctor_list})

def choose_surgery(request):

    if request.method == 'POST':

        name = request.POST['name']
        number = request.POST['number']
        email1 = request.POST['email1']
        email2 = request.POST['email2']
        reservation = request.POST['reservation']
        data_time = request.POST['date_time']
        address = request.POST.get('address')
        message = request.POST.get('message')

        creator = PDF_Creator()
        creator.generate_pdf(name, number, email1, reservation, data_time, address, message)

        emailer = Email_Sender()
        emailer.send_mail(email2)

    db = MySQLDB()
    specialist_type = db.select_surgery_type()
    s_type = []
    for t in specialist_type:
        t = str(t)
        t = t.replace(",", "")
        t = t.replace("'", "")
        t = t.replace("(", "")
        t = t.replace(")", "")
        s_type.append(t)
    print(s_type)
    return render(request, "search_hospital/choose_surgery.html", {'result': s_type})

def show_surgery(request):

    if request.method == 'POST':

        specialist_in = request.POST.get('btn', False)


    doctor_list = []

    db = MySQLDB()
    doctors = db.select_surgery(specialist_in)

    for x in doctors:
        doctor = []
        doctor.append(specialist_in)

        id = str(x[2])
        cost = str(x[5])
        doctor.append(id)
        doctor.append(cost)

        db = MySQLDB()
        doc = db.select_doctor(id)

        for d in doc:
            print(d)
            name = str(d[1])
            degree = str(d[2])
            year = str(d[3])
            work_place = str(d[4])

        doctor.append(name)
        doctor.append(degree)
        doctor.append(year)
        doctor.append(work_place)

        doctor_list.append(doctor)

    return render(request, "search_hospital/result_surgery.html", {'result': doctor_list})

def choose_diagonosis(request):

    if request.method == 'POST':

        name = request.POST['name']
        number = request.POST['number']
        email1 = request.POST['email1']
        email2 = request.POST['email2']
        reservation = request.POST['reservation']
        data_time = request.POST['date_time']
        address = request.POST.get('address')
        message = request.POST.get('message')

        creator = PDF_Creator()
        creator.generate_pdf(name, number, email1, reservation, data_time, address, message)

        emailer = Email_Sender()
        emailer.send_mail(email2)

    db = MySQLDB()
    specialist_type = db.select_diagonosis_type()
    s_type = []
    for t in specialist_type:
        t = str(t)
        t = t.replace(",", "")
        t = t.replace("'", "")
        t = t.replace("(", "")
        t = t.replace(")", "")
        s_type.append(t)
    print(s_type)
    return render(request, "search_hospital/choose_diagonosis.html", {'result': s_type})

def show_diagonosis(request):

    if request.method == 'POST':

        specialist_in = request.POST.get('btn', False)


    doctor_list = []

    db = MySQLDB()
    doctors = db.select_diagonosis(specialist_in)

    for x in doctors:
        doctor = []
        doctor.append(specialist_in)

        id = str(x[2])
        cost = str(x[5])
        doctor.append(id)
        doctor.append(cost)

        db = MySQLDB()
        doc = db.select_doctor(id)

        for d in doc:
            print(d)
            name = str(d[1])
            degree = str(d[2])
            year = str(d[3])
            work_place = str(d[4])

        doctor.append(name)
        doctor.append(degree)
        doctor.append(year)
        doctor.append(work_place)

        doctor_list.append(doctor)

    return render(request, "search_hospital/result_diagonosis.html", {'result': doctor_list})

