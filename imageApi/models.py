from django.db import models
from api.models import User

from django.conf import settings
# Create your models here.




# class UserSubscription(models.Model):


#     subscriptions_type = models.CharField(max_length=255)
#     expiration_date = models.DateTimeField()
#     # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions', null=True)

#     pricing  =  models.IntegerField(null=True)
    





#     def __str__(self) -> str:
#         return self.subscriptions_type




class ImageModel(models.Model):

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to ='images/')
    description = models.TextField()
    # user =  models.ForeignKey(CustomUserProfile,on_delete=models.CASCADE ,related_name='user')

    is_subscribers_only = models.BooleanField(default=False)



   
    def __str__(self) -> str:
        return self.name
    def is_downloadable(self, user):
        if user.is_authenticated:
            try:
                user_membership = user.user_membership
                if user_membership.membership and user_membership.membership.active:
                    return True
            except UserMembership.DoesNotExist:
                pass
        return False

    


# class SubscrpitionPlan(models.Model):
#     subscrpiton_name = models.CharField(max_length=255)
#     subscrption_prize = models.IntegerField(null=True)


class Membership(models.Model):
    MEMBERSHIP_CHOICES = (
        ('Premium', 'Premium'),
        ('Free', 'Free')
    )
    PERIOD_DURATION = (
        ('Days', 'Days'),
        ('Week', 'Week'),
        ('Months', 'Months'),
    )
    slug = models.SlugField(null=True, blank=True)
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, default='Free', max_length=30)
    duration = models.PositiveIntegerField(default=7)
    duration_period = models.CharField(max_length=100, default='Day', choices=PERIOD_DURATION)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
 
    def _str_(self):
       return self.membership_type
 
#### User Membership
class UserMembership(models.Model):
    user = models.OneToOneField(User, related_name='user_membership', on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, related_name='user_membership', on_delete=models.SET_NULL, null=True)
 
    def _str_(self):
       return self.user.username
 
#### User Subscription
class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, related_name='subscription', on_delete=models.CASCADE)
    expires_in = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
 
    def _str_(self):
      return self.user_membership.user.username