from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import HomeSite, AboutWeb1, FashionBlog, WorkBlog


class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homesite = HomeSite.objects.all()
        aboutweb1 = AboutWeb1.objects.all()
        fashionblog = FashionBlog.objects.all()
        workblog = WorkBlog.objects.all()
        return render(request, self.template_name, {'homesite':homesite, 'aboutweb1':aboutweb1, 'fashionblog':fashionblog, 'workblog':workblog})