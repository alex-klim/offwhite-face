from django.shortcuts import render
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from redis import Redis
from .forms import CrawlerForm


class IndexView(FormView):
    template_name = "face/index.html"
    form_class = CrawlerForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            print(url)
            r = Redis()
            r.lpush('offwhite:start_urls', url)
            return HttpResponseRedirect('/')

