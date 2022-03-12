from django import forms

class CouponApplyForm(forms.Form):
	code = forms.CharField() 

class CheckOutForm(forms.Form):
	address = forms.CharField(
	widget=forms.Textarea(attrs={"placeholder":"لطفا آدرس خود را وارد کنید" , "name":"address"})
	)
	zipcode = forms.CharField(
	widget=forms.TextInput(attrs={"placeholder":"کد پستی", "name":"zipcode" , "maxlength":10})
	)