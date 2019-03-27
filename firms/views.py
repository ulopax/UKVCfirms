from django.shortcuts import render
from django.views import View
from .models import Firm

import random


class Home(View):

    def get(self, request):

        # returning 3 at the moment but this should change later on

        context = dict()

        firms = [firm for firm in Firm.objects.all()]
        context['firms'] = random.sample(firms, 3)
        return render(request, 'firms/home.html', context=context)