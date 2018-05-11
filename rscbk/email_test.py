from django.core.mail import send_mail

send_mail('Password Reset Link', 'Please click on the below link to reset your password \n\n <a href="http://www.barterkings.in">Click Here</a>  \n\n\n\n\n\n Regards,\nTeam BarterKings', 
            'just2deepu@gmail.com', ['deepakkumar.py@gmail.com'],fail_silently=False)
print ("Mail sent successfully {}".format(send_mail))