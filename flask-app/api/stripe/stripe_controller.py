from flask import Blueprint
from api.stripe import stripe_service
from api.auth import auth


stripe_router = Blueprint('stripe_router', __name__)

@stripe_router.route('/publishable-key', methods = ['GET'], strict_slashes=False)
def get_publishable_key():
  return stripe_service.get_publishable_key()

@stripe_router.route("/create-checkout-session", methods = ['POST'], strict_slashes=False)
def create_checkout_session():
    return stripe_service.create_checkout_session()
    
@stripe_router.route("/webhook", methods=["POST"])
def stripe_webhook():
    return stripe_service.stripe_webhook()