from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Display all Tweets
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    print(tweets)   
    return render(request, 'tweet_list.html', {'tweets':tweets})

# Search Functionality
def tweet_list(request):
    query = request.GET.get('q','')
    tweets = Tweet.objects.all().order_by('-created_at')
    if query:
        tweets = tweets.filter(text__icontains=query)
    return render(request, 'tweet_list.html', {'tweets':tweets, 'query':query})

# Create/add Tweets
@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')   
    else:
        form = TweetForm()

    return render(request, 'tweet_from.html', {'form':form})

# Edits Tweets
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')  
    else:
        form = TweetForm(instance=tweet)

    return render(request, 'tweet_from.html', {'form':form}) 

# Delete Tweets
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    
    return render(request, 'tweet_delete.html', {'tweet':tweet}) 

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form':form}) 

