from django import forms

CHOICES = ((1, 'Apparel'), 
            (2, 'Donation'), 
            (3, 'Dues'), 
            (4, 'Equipment'), 
            (5, 'Event'), 
            (6, 'Fundraising'), 
            (7, 'League & Entry Fees'), 
            (8, 'Travel'),
            (9, 'Other'))

class SubmitRequest(forms.Form):
    reason = forms.CharField(label="Reason", max_length=300)
    amount = forms.DecimalField(label="Amount", max_digits=6, decimal_places=2)
    payable_to = forms.CharField(label="Make Check payable to", max_length=50)

class TrackSpending(forms.Form):
    paid_to = forms.CharField(label="Paid To", max_length=50)
    paid_by = forms.CharField(label="From", max_length=50)
    paid_for = forms.CharField(label="Paid for", max_length=50)
    cat = forms.MultipleChoiceField(label="Category", choices=CHOICES)
    amount = forms.DecimalField(label="Amount", max_digits=6, decimal_places=2)
    regatta = forms.CharField(label="Regatta", max_length=50, required=False)

    