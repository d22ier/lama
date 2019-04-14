from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic import TemplateView
from django.contrib import messages
from .models import Question

class IndexView(TemplateView):
    template_name = 'whichOne/index.html'

class whichOne(generic.ListView):
    template_name = 'whichOne/whichOne.html'
    model = Question
    def get_queryset(self):
        return Question.objects.order_by('?')[:2]

    @staticmethod
    def init_game(response):
        response.set_cookie('score_lama', '0')
        response.set_cookie('try_lama', '0')
        return response

    @staticmethod
    def game(request, response):
        if 'score_lama' in request.COOKIES and 'try_lama' in request.COOKIES:
            question = request.POST.get('question')
            if 'alpaga_choice.x' in request.POST and question == 'alpaga' or 'lama_choice.x' in request.POST and question == 'lama':
                score_lama = int(request.COOKIES.get('score_lama')) + 1
                response.set_cookie('score_lama', str(score_lama))
            try_lama = int(request.COOKIES.get('try_lama')) + 1
            response.set_cookie('try_lama', str(try_lama))
        return response

    def win_or_lose(self, request, response):
        if 'score_lama' in request.COOKIES and 'try_lama' in request.COOKIES:
            print('\n SCORE LAMA : '+ str(request.COOKIES.get('score_lama'))+ '\n')
            print('\n TRY LAMA : '+ str(request.COOKIES.get('try_lama'))+ '\n')
            if int(request.COOKIES.get('try_lama')) == 4:
                print('\nTRY LAMA : '+ str(request.COOKIES.get('try_lama'))+ '\n')
                response.set_cookie('try_lama', '0')
                if int(request.COOKIES.get('score_lama')) == 4:
                    print('SCORE LAMA > 5')
                    messages.success(request, 'You win bro ! Well done')
                else:
                    messages.error(request, 'You lost ! Try again')
                response.set_cookie('score_lama', '0')
                response.set_cookie('try_lama', '0')
        return response

    def post(self, request, **kwargs):
        response = HttpResponseRedirect(request.path)

        if not request.COOKIES.get('score_lama'):
            response = self.init_game(response)
            response = self.game(request, response)

        if request.method == 'POST':
            response = self.game(request, response)
            response = self.win_or_lose(request, response)
            print('\n AFTER SCORE LAMA : '+ str(request.COOKIES.get('score_lama'))+ '\n')
            print('\n AFTER TRY LAMA : '+ str(request.COOKIES.get('try_lama'))+ '\n')
        return response
