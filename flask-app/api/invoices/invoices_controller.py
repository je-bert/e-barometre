from flask import Blueprint
from api.invoices import invoices_service
from api.auth import auth

invoices_router = Blueprint('invoices_router', __name__)

@invoices_router.route('/<invoice_id>', methods = ['GET'], strict_slashes=False)
@auth
def find_one(current_user, invoice_id):
    return invoices_service.find_one(current_user.user_id, invoice_id)

@invoices_router.route('/', methods = ['GET'], strict_slashes=False)
@auth
def find_all(current_user):
  return invoices_service.find_all(current_user.user_id)

