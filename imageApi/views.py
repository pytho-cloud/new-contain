from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.http import HttpResponse ,Http404 ,HttpResponseForbidden ,FileResponse
from django.shortcuts import get_object_or_404
from imageApi.models import ImageModel
from .models import Subscription
from datetime import datetime

# Create your views here.
from .serializer import *
from .models import *
import os



# class ImageViewset(ModelViewSet):

#     queryset = ImageModel.objects.all()
#     serializer_class = ImageModelSerializer



#     @action(detail =True ,methods=['get'])
#     def download_image(request,image_id):

#         image = ImageModel.objects.get(pk= image_id)

#         user = request.user 

#         if image.is_subscribers_only:

#             subscription = UserSubscription.objects.filter(user=user ,expiration_date__gte = datetime.now()).first()

#             if not subscription :

#                 return HttpResponseForbidden("You must have active subscriptions to download an image ")
        
#         response =  FileResponse(open(image.image.path,'rb'))
            

#         return response


"""

Particular Image Method

"""

# def image_details(request,image_id):

#     image =  get_object_or_404(ImageModel,pk = image_id)

#     return HttpResponse(f'Image Title : {image.name} ,Descriptions : {image.user}')



class SubscriptionsViewset(ModelViewSet):

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionsSerailizer


from rest_framework import generics
from .models import ImageModel


class ImageDetailAPIView(generics.ListCreateAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageModelSerializer



from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import ImageModel
from django.views.static import serve
from django.conf import settings


# def download_image(request, image_id):
#     image = get_object_or_404(ImageModel, pk=image_id)

#     # Get the path to the image file on your server
#     image_path = image.image.path

#     if os.path.exists(image_path):
#         with open(image_path, 'rb') as image_file:
#             response = HttpResponse(image_file.read(), content_type='image/png')
#             response['Content-Disposition'] = f'attachment; filename="{image.name}.png"'
#             return response
#     else:
#         raise Http404("Image not found")

###############
# def download_image(request, image_id):
#     image = get_object_or_404(ImageModel, pk=image_id)
    
#     if not request.user.is_authenticated:
#         return HttpResponse("You must be logged in to download images.")

#     user_membership = UserMembership.objects.filter(user=request.user).first()
    
#     # Check if the user has an active subscription (update based on your model)
#     if user_membership and user_membership.membership and user_membership.membership.active:
#         # Get the path to the image file on your server
#         image_path = image.image.path

#         if os.path.exists(image_path):
#             with open(image_path, 'rb') as image_file:
#                 response = HttpResponse(image_file.read(), content_type='image/png')
#                 response['Content-Disposition'] = f'attachment; filename="{image.name}.png"'
#                 return response
#         else:
#             raise Http404("Image not found")
#     else:
#         return HttpResponse("You must have an active subscription to download this image.")


##################
# def download_image(request, image_id):
#     image = get_object_or_404(ImageModel, pk=image_id)
    
#     if not request.user.is_authenticated:
#         return HttpResponse("You must be logged in to download images.")

#     user_membership = UserMembership.objects.filter(user=request.user).first()
    
#     # Check if the user has an active subscription
#     if user_membership:
#         subscription = user_membership.subscription.first()
#         if subscription and subscription.active:
#             # Get the path to the image file on your server
#             image_path = image.image.path

#             if os.path.exists(image_path):
#                 with open(image_path, 'rb') as image_file:
#                     response = HttpResponse(image_file.read(), content_type='image/png')
#                     response['Content-Disposition'] = f'attachment; filename="{image.name}.png"'
#                     return response
#             else:
#                 raise Http404("Image not found")
#         else:
#             return HttpResponse("You must have an active subscription to download this image.")
#     else:
#         return HttpResponse("You must have an active subscription to download this image.")




from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from .models import ImageModel
from .models import UserMembership  # Import your UserMembership model
from .models import Subscription  # Import your Subscription model
import os

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def download_image(request, image_id):
    image = get_object_or_404(ImageModel, pk=image_id)
    
    user = request.user  # This contains user data from the JWT token, provided by Simple JWT.
    
    user_membership = UserMembership.objects.filter(user=user).first()
    
    # Check if the user has an active subscription
    if user_membership:
        subscription = Subscription.objects.filter(user_membership=user_membership, active=True).first()
        if subscription:
            # Get the path to the image file on your server
            image_path = image.image.path

            if os.path.exists(image_path):
                with open(image_path, 'rb') as image_file:
                    response = HttpResponse(image_file.read(), content_type='image/png')
                    response['Content-Disposition'] = f'attachment; filename="{image.name}.png"'
                    return response
            else:
                raise Http404("Image not found")
        else:
            return HttpResponse("You must have an active subscription to download this image.")
    else:
        return HttpResponse("You must have an active subscription to download this image.")





