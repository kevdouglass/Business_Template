from django.shortcuts import render
#   Step (1) for email: import DJANGO's send_mail library 
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html')


# def send_thank_you():
    

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        #   Step (1) for email: import DJANGO's send_mail library 
        #from django.core.mail import send_mail
        # Step (2)  Send an email
        #   GET -> (to my email)
        send_mail(
            'Message from ' + message_name, # Subject
            message, # message
            message_email, # FROM - email
            ['kevdouglass@gmail.com'], # TO - email
        )   #   Step (3) setup email settings in our Settings.py file
        
        #   POST -> (to user email)
        contact_ss = f"Welcome {message_name}!\n\nThank you for contacting Dr. Kevin Douglass DDS. We look forward to speaking with you shortly :)"
        send_mail(
            'Thank you!', # subject
            contact_ss, #   message
            #   From email
            'kevdouglass@gmail.com',
            [message_email],     #   To Email
        )
        return render(request, 'contact.html', {'message_name': message_name})
    else:   
        return render(request, 'contact.html', {})
    
    
    
    
    
    
    
    
    
    # Create your views here.
    
def appointment(request):
    '''
        If someone is accidently directed to this page without filling out the <FORM> fields, They will be redirected to our HOME.html page..
    '''
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_email = request.POST['your-email']
        your_phone = request.POST['your-phone']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']

                             
                    

        # #   Step (1) for email: import DJANGO's send_mail library 
        # #from django.core.mail import send_mail
        # # Step (2)  Send an email
        appointment_email = "Name: " + your_name + "\n Phone: " + your_phone + "\n Address: " + your_address + "\n Day: " + your_date + "\n Time: " + your_schedule + "\n Message: " + your_message
        html_appointment_email = "Name: " + your_name + "<br/> <strong>Phone: </strong>" + your_phone + "<br/> <strong>Address: </strong>" + your_address + "<br/> <strong>Day: </strong>" + your_date + "<br/> <strong>Time: </strong>" + your_schedule + "<br/> <strong>Message: </strong>" + your_message

        send_mail(
            'Appointment Request', # Subject
            appointment_email, # message
            your_email, # FROM - email
            ['kevdouglass@gmail.com'], # TO - email
        )   #   Step (3) setup email settings in our Settings.py file
        
        contact_ss = f"Welcome {your_name}!\n\nThank you for contacting Dr. Kevin Douglass DDS. We look forward to speaking with you shortly :)"
        send_mail(
            'Thank you!', # subject
            contact_ss, #   message
            #   From email
            ['kevdouglass@gmail.com'],
            your_email,     #   To Email
        )
        
        return render(request, 'appointment.html', {'your_name': your_name,
                    'your_email': your_email,
                    'your_phone': your_phone,
                    'your_address': your_address,                            
                    'your_schedule': your_schedule,
                    'your_date': your_date,
                    'your_message': your_message})
                    
        # return render(request, 'appointment.html', {'message_name': message_name})
    else:   
        return render(request, 'home.html', {})
    # return render(request, 'appointment.html', {})





def about(request):
    return render(request, 'about.html')


def pricing(request):
    return render(request, 'pricing.html', {})





def service(request):
    return render(request, 'service.html', {})




def blog(request):
    return render(request, 'blog.html', {})




def blog_details(request):
    return render(request, 'blog-details.html', {})

