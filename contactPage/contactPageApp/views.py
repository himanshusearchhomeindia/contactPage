from django.shortcuts import render,HttpResponse
import json
from contactPageApp.models import UserContactData
# Create your views here.
def ContactPage(request):
    """
    This function is used to show the contact page to the user.
    """
    return render(request, 'contactUs.html')

def ContactData(request):
    """
    This function will handle the data coming from the contact page.
    """
    if request.method == 'POST':
        print("working")
        success = True
        Data = json.loads(request.body.decode("utf-8")) #loading th 
        Name = Data['Name']
        Email = Data['Email']
        Phone = Data['Phone']
        Address = Data['Address']
        Message = Data['Message']
        userData = UserContactData(name=Name, email=Email,
                        phone=Phone, address=Address,
                        message=Message)
        userData.save()
        params = {
            'success':success
        }
        successData = json.dumps(params)
        return HttpResponse(successData)