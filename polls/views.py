from django.shortcuts import render,redirect
from django.http import HttpResponse , JsonResponse
from .forms import CreatePollForm
from .models import Poll
# Create your views here.

def home(request):
    polls = Poll.objects.all()
    context = {
        'polls':polls
    }
    return render(request,'polls/home.html',context)



def create(request):
    if request.method == "POST":
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            # print(form.cleaned_data['question']) this will print in console
    else:
        form = CreatePollForm()
    context = {
        'form':form

    }
    return render(request,'polls/create.html',context)



#VOTE and RESULT views for a single poll, so to specify this views for specific polls we will give them a poll_id

def vote(request,poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == "POST":
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1

        elif selected_option == 'option3':
            poll.option_three_count += 1

        else:
            return HttpResponse(400,'Invalid form')

        poll.save()

        return redirect('results', poll.id)
    context = {
        'poll':poll
    }
    return render(request,'polls/vote.html',context)



def results(request,poll_id):
    poll = Poll.objects.get(pk=poll_id)

    context = {
        'poll':poll
    }
    return render(request,'polls/results.html',context)

def deletePoll(request,poll_id):
    poll =Poll.objects.get(pk=poll_id)
    polls = Poll.objects.all()

    context = {
        'polls':polls
    }
    poll.delete()
    return render(request,'polls/home.html',context)