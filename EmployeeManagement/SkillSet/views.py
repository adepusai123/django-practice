from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
# from EmployeeManagement.SkillSet.models import Skills
# Create your views here.

def homepage(request):
    return HttpResponse('<h1> Welcome to Employee Management System </h1>')

def updateskillset(request):
    if request.method == 'POST':
        email = request.POST['email']
        skillset = ",".join(request.POST.getlist('skills'))
        data = F.Skills(emailid = email, skills = skillset)
        data.save()
    return render(request, 'updateskill.html', {'success': 'Skillset updated successfully'})
    # reurn render(request,'updateskill.html')
