
from __future__ import unicode_literals
import os 
from django.db import models
from django.http import HttpResponse
from xlplatpy.XlplatMiddleware import XlplatAuthMiddleware
from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your models here. 



class Document(models.Model):
	file_uploaded=models.FileField(upload_to='')
	uploaded_by=models.BigIntegerField()
	uploaded_on=models.DateTimeField(auto_now_add=True)
	document_name=models.CharField(max_length=100, null=True)
	verified=models.BooleanField(default=False)
	user_or_cid=models.CharField(max_length=100, null=True)
	class Meta:
		managed = True

	def __str__(self):
		return self.document_name;

class Declaration_form(models.Model):
	c_id=models.BigIntegerField()
	req_id=models.BigIntegerField()
	filled_on=models.DateTimeField(auto_now_add=True)
	question_id=models.BigIntegerField()
	question_response=models.BooleanField(default=False)
	question_details=models.CharField(max_length=100, null=True, blank=True)

class Vendor_form(models.Model):
	vendor_id=models.IntegerField()
	first_name=models.CharField(max_length=100, null=True, blank=True)
	last_name=models.CharField(max_length=100, null=True, blank=True)
	company_name=models.CharField(max_length=100, null=True, blank=True)
	date_of_collabration=models.DateTimeField(null=True)
	vendor_location=models.CharField(max_length=100, null=True, blank=True)
	vendor_gender=models.CharField(max_length=100)
	picture_uploaded=models.FileField(upload_to='',null=True, blank=True)
	created_by=models.IntegerField(null=True)

class Vendor_files(models.Model):
	vendor_id=models.ForeignKey(Vendor_form, on_delete=models.CASCADE)
	file_uploaded=models.FileField(upload_to='',null=True, blank=True)
	uploaded_on=models.DateTimeField(auto_now_add=True)
	uploaded_by=models.IntegerField(null=True)

class Resignation_data(models.Model):
	resignation_of=models.IntegerField(null=False,blank=False)
	application_status=models.CharField(max_length=250, null=False, blank=False)
	relieve_date=models.DateField(auto_now_add=False, null=False, blank=False)
	user_resign_date=models.DateField(auto_now_add=True, blank=True, null=False)
	user_relieve_date=models.CharField(max_length=250, null=False, blank=False)
	reason_of_leaving=models.CharField(max_length=250, null=False, blank=False)
	resignation_approved_on=models.DateField(null=True,blank=True)
	date_changed_by=models.IntegerField(null=False,default='')
	manager_clearance_json=models.CharField(max_length=10000,null=False,default='')
	accounts_clearance_json=models.CharField(max_length=10000,null=False,default='')
	admin_clearance_json=models.CharField(max_length=10000,null=False,default='')
	it_clearance_json=models.CharField(max_length=10000,null=False,default='')
	hr_clearance_json=models.CharField(max_length=10000,null=False,default='')
	exit_form_json=models.CharField(max_length=10000,null=False,default='')
	exit_closing_date=models.DateField(null=True,blank=True)
	exit_closed_by=models.IntegerField(null=False, blank=True)
	exit_approved=models.BooleanField(default=False)
	it_clearance_approved=models.BooleanField(default=False)
	manager_clearance_approved=models.BooleanField(default=False)
	accounts_it_clearance_approved=models.BooleanField(default=False)
	admin_clearance_approved=models.BooleanField(default=False)
	hr_clearance_approved=models.BooleanField(default=False)
	deleted=models.BooleanField(default=False)
	employee_clearance_filled=models.BooleanField(default=False)
	manager_clearance_date=models.DateField(null=True,blank=True)
	accounts_clearance_date=models.DateField(null=True,blank=True)
	admin_clearance_date=models.DateField(null=True,blank=True)
	it_clearance_date=models.DateField(null=True,blank=True)
	hr_clearance_date=models.DateField(null=True,blank=True)
	hr_clearance_date_final=models.DateField(null=True,blank=True)
	processing_date=models.DateField(null=True,blank=True)
	hr_clearance_approved_final=models.BooleanField(default=False)
	correspondence_address=models.CharField(max_length=500, null=True, blank=True)
	relieving_template=models.CharField(max_length=10000, null=True, blank=True)
	relieving_reference_no=models.BooleanField(default=False)
	send_to_vp=models.BooleanField(default=False)

def get_file_path(instance, filename):
	if instance.type_name == 1 or instance.type_name == 4 or instance.type_name == 7:
		directory_string_var = 'HR Process'
		return os.path.join('xlplat_ats/', directory_string_var, filename)
	elif instance.type_name == 2 or instance.type_name == 5 or instance.type_name == 8:
		directory_string_var = 'HR System Process'
		return os.path.join('xlplat_ats/', directory_string_var, filename)
	elif instance.type_name == 3 or instance.type_name == 6 or instance.type_name == 9:
		directory_string_var = 'Policies'
		return os.path.join('xlplat_ats/', directory_string_var, filename)

private_storage = FileSystemStorage(location=settings.MEDIA_ROOT)
class hr_document_data(models.Model):
	# HR_MANUAL_PROC = 1
	# HR_SYSTEM_PROC = 2
	# POLICIES = 3
	# OTHERS = 10
	# STATUS_CHOICES = (
	#     (HR_MANUAL_PROC, 'HR Process'),
	#     (HR_SYSTEM_PROC, 'HR System Process'),
	#     (POLICIES, 'Policies'),
	#     (OTHERS, 'Others'),
	# )
	row_id=models.AutoField(primary_key=True)
	file_upload=models.FileField(upload_to = get_file_path,storage=private_storage,default="")
	type_name=models.IntegerField(default=1)
	uploaded_date=models.DateField(auto_now_add=True,null=False)
	uploaded_by=models.IntegerField(null=True,default=44)

class pf_gratuity_data(models.Model):
	c_id=models.BigIntegerField()
	req_id=models.BigIntegerField()
	filled_on=models.DateTimeField(auto_now_add=True)
	ans_name=models.CharField(max_length=1000, null=False, blank=False)
	ans_responce=models.CharField(max_length=1000, null=False, blank=False)
	avail_pf=models.BigIntegerField(default=0)
	pf_gr_status=models.IntegerField(null=False,default=0)
	form_name=models.CharField(max_length=100,default="")

class twl_log_data(models.Model):
	call_sid=models.CharField(max_length=2000, default="")
	call_to=models.CharField(max_length=2000, default="")
	call_from=models.CharField(max_length=2000, default="")
	call_forwarded_to=models.CharField(max_length=2000, default="")
	call_status=models.CharField(max_length=1000, default="")
	record_sid=models.CharField(max_length=2000, default="")
	record_url=models.CharField(max_length=2000, default="")
	trans_id=models.CharField(max_length=2000, default="")
	trans_text=models.CharField(max_length=90000, default="")
	user_id=models.CharField(max_length=2000, default="")
	call_time=models.DateTimeField(auto_now_add=True)

class twillio_email(models.Model):
	user_id=models.CharField(max_length=2000, default="")

class health_ins_prem_price(models.Model):
	emp_id=models.BigIntegerField()
	premium=models.DecimalField(null=False,default=0,max_digits = 10,decimal_places=2)
	jan=models.DecimalField(null=False,default=0,max_digits = 10,decimal_places=2)
	feb=models.DecimalField(null=False,default=0,max_digits = 10,decimal_places=2)
	mar=models.DecimalField(null=False,default=0,max_digits = 10,decimal_places=2)
	apr=models.DecimalField(null=False,default=0,max_digits = 10,decimal_places=2)
	may=models.DecimalField(null=False,default=0,max_digits = 10,decimal_places=2)
	jun=models.DecimalField(null=False,default=0,max_digits = 10,decimal_places=2)
	jul=models.DecimalField(null=False,default=0,max_digits = 10,decimal_places=2)
	aug=models.DecimalField(null=False,default=0,max_digits = 10,decimal_places=2)
	sep=models.DecimalField(null=False,default=0,max_digits = 10,decimal_places=2)
	oct=models.DecimalField(null=False,default=0,max_digits = 10,decimal_places=2)
	nov=models.DecimalField(null=False,default=0,max_digits = 10,decimal_places=2)
	dec=models.DecimalField(null=False,default=0,max_digits = 10,decimal_places=2)
	sheet_label=models.CharField(max_length=2000, default="")
	completion_status=models.CharField(max_length=50,default="")
	exit_status=models.CharField(max_length=50,default="")
	data_entry_time=models.DateTimeField(auto_now_add=True)

class health_ins_details(models.Model):
	ref_no=models.IntegerField(null=False,default=0)
	emp_id=models.BigIntegerField()
	policy_info=models.CharField(max_length=2000, default="self")
	relation=models.CharField(max_length=2000, default="")
	ins_name=models.CharField(max_length=2000, default="")
	dob=models.DateField(null=True,blank=True)
	add_del_status=models.CharField(max_length=2000, default="")
	gender=models.CharField(max_length=2000, default="",null=True,blank=True)

class greetings_data_details(models.Model):
	user_id_for=models.CharField(max_length=100, default="")
	messagecharacter=models.CharField(max_length=2000, default="")
	user_id_by=models.CharField(max_length=100, default="")

class health_ins_fix_premium(models.Model):
	criteria_policy=models.CharField(max_length=2000, default="")
	price=models.IntegerField(null=False,default=0)
	ins_month=models.IntegerField(null=False,default=0)