from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'order/index.html')


    if request.method == 'POST':

        #Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #Check for errorneous inputs



        #check the user
        myuser = User.objects.create_user(username, email, pass1)
        mysuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('/order')

    else:
        return HttpResponse('404 - Not Found')
