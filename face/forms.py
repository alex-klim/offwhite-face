from django import forms


class CrawlerForm(forms.Form):
    args = [('offwhite', 'offwhite')]
    spider = forms.ChoiceField(label='crawler', widget=forms.Select, choices=args)
    url = forms.URLField(
        label="url",
        max_length=500,
        initial="https://www.off---white.com/en/US/men/t/seasons/ss2018"
    )
