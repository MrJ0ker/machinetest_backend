from django.db import models

# Create your models here.
## invoice_master table is defined here for saving invoices
class InvoiceMaster(models.Model):
    pk_bint_id = models.BigAutoField(primary_key=True)
    vchr_invoice_id = models.CharField(max_length=50, blank=True, null=True)
    vchr_cust_name = models.CharField(max_length=100, blank=True, null=True)
    vchr_email = models.CharField(max_length=100, blank=True, null=True)
    dbl_amt = models.BigIntegerField(blank=True, null=True)
    dat_created = models.DateTimeField(blank=True, null=True)
    dat_action = models.DateTimeField(blank=True, null=True)
    int_status = models.SmallIntegerField(blank=True, null=True)# 0- Unpaid Invoices 1- Paid Invoices

    class Meta:
        managed = False
        db_table = 'invoice_master'
