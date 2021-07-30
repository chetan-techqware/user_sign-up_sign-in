from django.shortcuts import render, HttpResponse , redirect
from home.models import Contact, Destination
from django.contrib import messages
from .forms import SignUpForm
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/home.html'

class AboutView(TemplateView):
    template_name = 'home/about.html'



 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            messages.success(request,"Your account has been successfully created")
            raw_password = form.cleaned_data.get('password1')
 
            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request,"Your are successfully Logged In")
 
            # redirect user to home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'home/signup.html', {'form': form})

def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('/')

def blog(request):
    dest1 = Destination()
    dest1.name = 'DECAF'
    dest1.desc = 'Nothing beats the taste of plain coffee. It is basic compared to all the other coffee drinks in this list but is the most widely consumed all over the world.'
    dest1.price = 'Rs. 50'
    dest1.img = '/static/decaf.jpg'
    
 
    dest2 = Destination()
    dest2.name = 'ESPRESSO'
    dest2.desc = 'Espresso is a form of concentrated coffee that is usually served as shots. All espresso based drinks have three common ingredients: espresso, steamed milk and foam.'
    dest2.price = 'Rs. 90'
    dest2.img = '/static/mocha.jpg'
    

    dest3 = Destination()
    dest3.name = 'CAFE LATTE'
    dest3.desc = 'Cafe latte is made with espresso and steamed milk of which, one third is espresso and two third is steamed milk and also consists of at least a centimeter of foam.'
    dest3.price = 'Rs. 100'
    dest3.img = '/static/coffee6.jpg'
    

    dest4 = Destination()
    dest4.name = 'CAFE MOCHA'
    dest4.desc = 'Cafe mocha is a blend of hot chocolate and cappuccino that is prepared by mixing chocolate powder with an espresso shot, which is then mixed with skimmed steamed milk, foam and whipped cream.'
    dest4.price = 'Rs. 100'
    dest4.img = '/static/coffee2.jpg'
    

    dest5 = Destination()
    dest5.name = 'CARAMEL MACCIHATO'
    dest5.desc = 'Caramel Macchiato is a signature drink of Starbucks that is similar to Frappuccino in taste and can be brewed in close to 5 minutes. '
    dest5.price = 'Rs. 120'
    dest5.img = '/static/coffee3.jpeg'
    

    dest6 = Destination()
    dest6.name = 'CAPPUCCINO'
    dest6.desc = 'Cappuccino is coffee drink that is made by mixing double espresso shots with steam milk foam. The steamed milk is poured on top of the espresso shot and is then topped with whipped cream or thick milk foam.'
    dest6.price = 'Rs. 120'
    dest6.img = '/static/coffee7.jpeg'

    
    dest7 = Destination()
    dest7.name = 'PERI-PERI FRIES'
    dest7.desc = 'Spicy fries with firey flavour of peri-peri'
    dest7.price = 'Rs. 80'
    dest7.img = '/static/fries1.jpeg'

    dest8 = Destination()
    dest8.name = 'FRENCH FRIES'
    dest8.desc = 'Classic salty french fries with tomato ketchup '
    dest8.price = 'Rs. 80'
    dest8.img = '/static/fries2.jpg'

    dest9 = Destination()
    dest9.name = 'CHEESY FRIES'
    dest9.desc = 'Potato fries with cheesy dip. Awesome flavour and great taste'
    dest9.price = 'Rs. 100'
    dest9.img = '/static/fries3.jpeg'

    dest10 = Destination()
    dest10.name = 'CRISPY VEG BURGER'
    dest10.desc = 'Chefs special crispy veg pattie. Should try once for deliciousness'
    dest10.price = 'Rs. 65'
    dest10.img = '/static/burger1.jpg'

    dest11 = Destination()
    dest11.name = 'BIG-BURGER'
    dest11.desc = 'Delicious Chef special burger with double pattie and awesome veggies inside'
    dest11.price = 'Rs. 90'
    dest11.img = '/static/burger2.jpeg'

    dest12 = Destination()
    dest12.name = 'WHOOPER MEAL'
    dest12.desc = 'Fantastic super meal for one Burger with medium fries and medium size soft-drink'
    dest12.price = 'Rs. 199'
    dest12.img = '/static/meal.jpg'
    

    dests = [dest1, dest2, dest3, dest4, dest5, dest6, dest7, dest8, dest9, dest10,dest11, dest12]



    return render(request, 'blog/blogHome.html', {'dests': dests})





def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4 :
            messages.error(request,"Please fill the form correctly")

        else:
            contact = Contact(name=name , email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,"Your message has been successfully sent")
    return render(request,'home/contact.html')
    # return HttpResponse('This is contact')




# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import PasswordChangeForm


# def handleLogin(request):
#     if request.method=='POST':
#         loginusername = request.POST['loginusername']
#         loginpassword = request.POST['loginpassword']

#         user = authenticate(username=loginusername, password=loginpassword)

#         if user is not None:
#             login(request,user)
#             messages.success(request,"Successfully Logged In")
#             return redirect('/')

#         else:
#             messages.success(request,"Invalid credentials")
#             return redirect('/')
#     return render(request,'home/login.html')


  
# class SignUpView(CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy('home')
#     template_name= ('home/signup.html')

# class BlogView(TemplateView):
#     template_name = 'blog/blogHome.html'
      





# @login_required
# def blogHome(request):
#     return render(request, 'blog/blogHome.html')
#     # return HttpResponse('This is blogHome')


# def home(request):
#     return render(request,'home/home.html')
#     # return HttpResponse('This is Home')


# def about(request):
    
#     return render(request,'home/about.html')
#     # return HttpResponse('This is about')



# def handleSignup(request):
#     if request.method=='POST':
#         username = request.POST['username']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']

#         # when to give error when given wrong input
#         if len(username)>10:
#             messages.error(request, "Username must be under 10 characters")
#             return redirect('home')


#         if not username.isalnum():
#             messages.error(request, "Username should only contain letters and numbers")
#             return redirect('/')

#         if pass1 != pass2:
#             messages.error(request,"Password doesn't match")
#             return redirect('/')


#         # create User
#         myuser = User.objects.create_user(username, email, pass1)
#         myuser.first_name = fname
#         myuser.last_name =lname
#         myuser.save()
#         messages.success(request, "Your account has been created")
#         return redirect('/')

#     else:
#         return HttpResponse("Not allowed")