from django import forms
from .models import Document,Declaration_form,Vendor_form,Vendor_files,hr_document_data
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file_uploaded',)

class DeclarationForm(forms.ModelForm):
    class Meta:
        model = Declaration_form
        fields = ('c_id','req_id')

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor_form
        fields = ('first_name','last_name','company_name','date_of_collabration','vendor_location','vendor_gender','picture_uploaded')

class VendorUploadDocumentForm(forms.ModelForm):
    class Meta:
        model = Vendor_files
        fields = ('file_uploaded',)
        
class hrDocumentForm(forms.ModelForm):
    class Meta:
        model = hr_document_data
        fields = ('file_upload',)




# vendorlist: {.
    #     302: {
    #         'first_name': 'Shivani', 
    #         'last_name': 'Sharma', 
    #         'date_of_collabration': 'Jun 07, 2019', 
    #         'created_by': 'Shivani Sharma', 
    #         'picture_uploaded': 'rangoli.jpg', 
    #         1: {
    #             1: {
    #                 'filename': 'declaration.pdf', 
    #                 'uploaded_by': 'Shivani Sharma', 
    #                 'uploaded_on': datetime.datetime(2019, 6, 21, 7, 9, 44, 130441, tzinfo=<UTC>)
    #             }, 
    #             2: {
    #                 'filename': 'Dummy_CV.pdf', 
    #                 'uploaded_by': 'Shivani Sharma', 
    #                 'uploaded_on': datetime.datetime(2019, 6, 21, 7, 10, 8, 923899, tzinfo=<UTC>)
    #             }, 
    #             3: {
    #                 'filename': 'funny-wallpapers-cat-88922736.jpg', 
    #                 'uploaded_by': 'Shivani Sharma', 
    #                 'uploaded_on': datetime.datetime(2019, 6, 21, 7, 12, 20, 330121, tzinfo=<UTC>)
    #             }
    #         }
    #     }, 
    #     303: {
    #         'first_name': 'Simran', 
    #         'last_name': 'Sharma', 
    #         'date_of_collabration': 'Jun 07, 2019', 
    #         'created_by': 'Shivani Sharma', 
    #         'picture_uploaded': '', 
    #         2: {
    #             4: {
    #                 'filename': 'funny-wallpapers-cat-88922736.jpg', 
    #                 'uploaded_by': 'Shivani Sharma', 
    #                 'uploaded_on': datetime.datetime(2019, 6, 21, 7, 13, 13, 511406, tzinfo=<UTC>)
    #             }
    #         }
    #     }
    # }
