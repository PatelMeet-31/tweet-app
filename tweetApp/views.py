from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# Create your views here.
def index(request):
    return render(request,'index.html')

def tweet_list(request):
    query = request.GET.get('q', '').strip()  # Get search query from URL
    if query:
        tweets = Tweet.objects.filter(text__icontains=query).order_by('-created_at') # Filter tweets by search text (case-insensitive) and show newest first
    else:
        tweets = Tweet.objects.all().order_by('-created_at') # from newest to oldest tweet
    return render(request, 'tweet_list.html', {
        'tweets': tweets,
        'query': query
        })

@login_required
def tweet_create(request):
    if request.method == "POST":  # Form submitted by user
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():     # Django's built-in method to validate form data
            tweet = form.save(commit=False)     # False means do not save the form to the database yet
            tweet.user = request.user    # Get the user from the request who created the tweet
            tweet.save()    # Store the tweet in the database
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet) # Pass tweet instance to ensure tweet is already exists in which editing 
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet) # passed the tweet instance because there is data in the tweet form when going to edit  
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})


def register(request):
    if request.method == "POST":
         # Create a form instance (form filled with submitted POST data)
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # False means do not save the form to the database yet
            # Get the validated plain password from Django’s built-in form.cleaned_data and hash it using built-in set_password() before saving
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        # Create an empty form instance to display in the template
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
