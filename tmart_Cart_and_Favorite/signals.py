from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from tmart_Cart_and_Favorite.models import Order

@receiver(post_save , sender = User)
def cart_for_new_user(sender , instance , created , **kwargs):
	if created:
		order = Order.objects.filter(owner_id=instance.id,is_paid=False)
		if not order:
			order = Order.objects.create(owner_id=instance.id,is_paid=False)