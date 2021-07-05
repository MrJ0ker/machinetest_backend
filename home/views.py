from django.db import connection
from bd_myproj.settings import ALLOWED_HOSTS
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import InvoiceMaster
from datetime import date, datetime
from django.core.mail import send_mail
import bitly_api


# Create your views here.
class AddInvoice(APIView):
    def post(self,request):
        try:
            vchr_invoice_id =request.data.get('strInvoiceId')
            vchr_cust_name = request.data.get('strCustName')
            vchr_email = request.data.get('strEmail')
            dbl_amt = request.data.get('dblAmount')
            ins_invoice = InvoiceMaster.objects.create(vchr_invoice_id=vchr_invoice_id,
                                                       vchr_cust_name=vchr_cust_name,
                                                       vchr_email=vchr_email,
                                                       dbl_amt=dbl_amt,
                                                       int_status = 0,
                                                       dat_created = datetime.now())
            
            if ins_invoice:
                return Response({'status':1,'message':"success"})
            else:
                return Response({'status':0,'message':"failed"})
        except Exception as e:
            return Response({'status':0,'message':str(e)})
class Payment(APIView):
    def get(self,request,id):
        ins_invoice = InvoiceMaster.objects.filter(pk_bint_id = id,int_status=0).values('pk_bint_id','vchr_cust_name','vchr_email','dbl_amt','vchr_invoice_id').first()
        if ins_invoice:
            return Response({'status':1,'message':"success",'data':ins_invoice})
        else:
            return Response({'status':0,'message':'No data'})
            
class SavePayment(APIView):
    def post(self,request):
        try:
            int_id = request.data.get('intId')
            if int_id:
                InvoiceMaster.objects.filter(pk_bint_id = int_id).update(int_status = 1)
                return Response({'status':1,'message':"Updated"})
        except Exception as e:
            return Response({'status':0,'message':str(e)})
            
    
class SendMail(APIView):
    def get(self,request):
        bitly_token = '0fdc40983521b163c8307ee73b47d25526d0e8b1'
        connection = bitly_api.Connection(access_token = bitly_token) 
        
        ins_invoice = InvoiceMaster.objects.filter(int_status =0 ).values('pk_bint_id','vchr_cust_name','vchr_email','dbl_amt','vchr_invoice_id')
        if not ins_invoice:
            return Response({'status':0,'message':"No data"})
        else:
            for ins_data in ins_invoice:
                vchr_url = 'http://127.0.0.1:4200/payment/'+str(ins_data['pk_bint_id'])
                vchr_short_url = connection.shorten(vchr_url)['url']
                vchr_subject = 'Invoice Payment Request'
                vchr_message = 'Dear '+str(ins_data['vchr_cust_name'])+'\n Kindly pay the invoice amount of Rs '+str(ins_data['dbl_amt'])+'for the invoice '+str(ins_data['vchr_invoice_id'])+'\nPlease use the payment link '+str(vchr_short_url)+'\n Thank You.'
                
                send_mail(subject=vchr_subject,message=vchr_message,recipient_list=[ins_data['vchr_email']],from_email='chriztophermoriarity@gmail.com',fail_silently=True)
                
            return Response({'status':1,'message':"success"})
                

