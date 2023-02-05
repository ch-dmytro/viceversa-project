from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request, 'home.html')

def reverse(request):
	message_text = request.GET['message']
	reversed_text = message_text[::-1]
	words_amount = str(len(message_text.split()))
	return render(request, 'reverse.html', {'message':message_text, 'reversedtext':reversed_text, 'amount':words_amount})
