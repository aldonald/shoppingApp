from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class IndexView(LoginRequiredMixin, View):
    template_name = 'server/index'

    def get(self, request, **kwargs):
        return render(request, 'server/index.html')
