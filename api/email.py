

# from django.core.mail import send_mail
# from django.conf import settings
# from random import randint
# # from .models import CustomUserProfile
# def send_mail_via_email(email):
    

    

#     subject = 'Hello, Django Email!'
#     otp =  randint(999,9999)
#     message = 'Your OTP is ' + str(otp)
#     from_email =  settings.EMAIL_HOST # Replace with your email
#     recipient_list = [email]  # Replace with the recipient's email address

#     send =send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#     user_obj = CustomUserProfile.objects.get(email = email)
#     user_obj.otp = otp
    
#     user_obj.save()
#     if send :
#         return True
#     else:
#         return False
    



# def send_forget_password_mail(username,email):

    
#     subject = 'Hello, Your Forget Password OTP'
#     otp =  randint(999,9999)
#     message = 'Your OTP is {subject} ' + str(otp)
#     from_email =  settings.EMAIL_HOST # Replace with your email
#     recipient_list = [email]  # Replace with the recipient's email address

#     send =send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#     user_obj = CustomUser.objects.get(email = email)
#     user_obj.otp = otp
    
#     user_obj.save()
#     if send :
#         return True
#     else:
#         return False
    
