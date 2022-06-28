from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedBackForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('done')
    form = FeedBackForm()
    return render(request, 'feedback/index.html', context={'form': form})


def done(request):
    return render(request, 'feedback/done.html')
