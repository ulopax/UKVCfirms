from django.shortcuts import render
from django.views import View
from .models import Firm, Employee

class Home(View):

    def get(self, request):

        # returning 3 at the moment but this should change later on

        context = dict()
        context['firms'] = Firm.objects.order_by('-id')[:3]
        return render(request, 'firms/home.html', context=context)