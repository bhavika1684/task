from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path


# app_name="xlplat_ats"


urlpatterns=[
	url(r'^map_documents/$',views.map_documents.as_view(),name='map_documents'),
	url(r'^map_appraisal/$',views.map_appraisal.as_view(),name='map_appraisal'),
	url(r'^map_appraisal_mail',views.map_appraisal_mail.as_view(),name='map_appraisal_mail'),
	url(r'^upload_documents/$',views.Upload_documents.as_view(),name='upload_documents'),
	url(r'^declaration_form/$',views.declaration_form.as_view(),name='declaration_form'),
	url(r'^upload_hr_documents/$',views.upload_hr_documents.as_view(),name='upload_hr_documents'),
	url(r'^document_checklist/$',views.document_checklist.as_view(),name='document_checklist'),
	url(r'^vendor_documents/$',views.vendor_documents.as_view(),name='vendor_documents'),
	url(r'^apply_resign/$',views.apply_resign.as_view(),name='apply_resign'),
	url(r'^pf_gratuity/$',views.pf_gratuity.as_view(),name='pf_gratuity'),
	path('modify_user_application/<slug:ap_id>',views.modify_user_application,name='modify_user_application'),
	path('exit_employee_form/<slug:ap_id>',views.exit_employee_form,name='exit_employee_form'),
	# url(r'^greeting_card/$',views.greeting_card.as_view(),name='greeting_card'),
	path('greeting_card/<slug:ap_id>',views.greeting_card,name='greeting_card'),
	path('employee_clearance_form/<slug:ap_id>/<str:type_val>',views.employee_clearance_form,name='employee_clearance_form'),
	path('exit_employee_form_internal/<slug:ap_id>',views.exit_employee_form_internal,name='exit_employee_form_internal'),
	path('employee_clearance_form_internal/<slug:ap_id>/<str:type_val>',views.employee_clearance_form_internal,name='employee_clearance_form_internal'),
	path('relieving_letter/<slug:ap_id>',views.relieving_letter_emp,name='relieving_letter_emp'),
	path('print_relieving_letter/<slug:ap_id>',views.print_relieving_letter,name='print_relieving_letter'),
	path('twl_call_meta/',views.twl_call_meta,name="twl_call_meta"),
	path('twl_call_check/',views.twl_call_check,name="twl_call_check"),
	path('twl_call_record/',views.twl_call_record,name="twl_call_record"),
	path('twl_start_call/',views.twl_start_call,name="twl_start_call"),
	path('call/',views.call_req.as_view(),name="call_req"),
	path('twillio_email_admin/',views.twillio_email_admin.as_view(),name="twillio_email_admin"),
	path('health_track_sys/',views.health_track_sys.as_view(),name="health_track_sys")
] 

# if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)