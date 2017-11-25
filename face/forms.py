from django import forms


class CrawlerForm(forms.Form):
    crawler = forms.CharField(label="crawler", max_length=20)
    url = forms.URLField(label="url", max_length=100)
