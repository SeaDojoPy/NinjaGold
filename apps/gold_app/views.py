# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from random import randint
from datetime import datetime

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activity'] = []
    return render(request, 'gold_app/index.html')

def process(request):
    #random gold amount
    #determine where we came from
    activity = request.POST['activity']
    print activity
    result = ''
    if activity == 'farm':
        gold = randint(10,21)
        request.session['gold'] += gold

        result = {
            'color' : 'green',
            'content':'you visited the farm and earned {} gold at {}'.format(gold, datetime.now().strftime('%Y-%m-%d // %H:%M'))
        }
    if activity == 'cave':
        gold = randint(5,11)
        request.session['gold'] += gold

        result = {
        'color' : 'green',
        'content':'you visited the cave and earned {} gold at {}'.format(gold, datetime.now().strftime('%Y-%m-%d // %H:%M'))
        }
    if activity == 'house':
        gold = randint(2,6)
        request.session['gold'] += gold

        result = {
        'color' : 'green',
        'content':'you visited the house and earned {} gold at {}'.format(gold, datetime.now().strftime('%Y-%m-%d // %H:%M'))
        }
    if activity == 'casino':
        gold = randint(-50,51)
        request.session['gold'] += gold
        if gold < 0:
            result = {
                'color':'red',
                'content':'you visited the casino and lost {} gold at {}'.format(gold * -1, datetime.now().strftime('%Y-%m-%d // %H:%M'))

            }
        else:
            result = {
                'color' : 'green',
                'content':'you visited the casino and earned {} gold at {}'.format(gold, datetime.now().strftime('%Y-%m-%d // %H:%M'))
            }

    print result
    request.session['activity'].insert(0,result)

    #activity log
    #increment session gold

    return redirect('/')