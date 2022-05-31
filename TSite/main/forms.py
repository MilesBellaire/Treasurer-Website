from django import forms


class SubmitRequest(forms.Form):
    reason = forms.CharField(label="Reason", max_length=300)
    amount = forms.DecimalField(label="Amount", max_digits=6, decimal_places=2)
    payable_to = forms.CharField(label="Make Check payable to", max_length=50)
