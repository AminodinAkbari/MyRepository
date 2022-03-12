from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(
		widget =forms.TextInput(attrs={"name" : "subject","placeholder":"موضوع" , "class":"rtl" , "type":"text"})
	)
	message = forms.CharField(
		widget =forms.Textarea(attrs={"name" : "message","placeholder":"متن پیام" , "class":"rtl" , "type":"text"})
	)