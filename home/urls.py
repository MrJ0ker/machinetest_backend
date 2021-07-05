from django.urls import path
from .views import AddInvoice,Payment,SendMail,SavePayment

urlpatterns = [
    path('add_invoice', AddInvoice.as_view(), name='add_invoice'),
    path('send_email', SendMail.as_view(), name='send_email'),
    path('save_payment', SavePayment.as_view(), name='save_payment'),
    path('payment/<int:id>',Payment.as_view()),
]