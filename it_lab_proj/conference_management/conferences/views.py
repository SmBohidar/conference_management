from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Conference
from django.shortcuts import render, redirect, get_object_or_404


from .models import Chair, Reviewer, User

# Login Views
from django.contrib.auth.hashers import check_password

from django.contrib.auth.hashers import check_password
from .models import Chair
from .forms import ResearchPaperForm, ReviewForm
from django.shortcuts import render, redirect
from .forms import ResearchPaperForm

def add_review(request):
    if request.method == 'POST':
        conference_id = request.POST.get('conference')
        conference = get_object_or_404(Conference, pk=conference_id)
        review_text = request.POST.get('review')

        if review_text:
            conference.review = review_text
            conference.save()
            return redirect('user_dashboard')  # Redirect to user dashboard after adding the review
    else:
        form = ReviewForm()  # Assuming you have a ReviewForm defined in forms.py
    return render(request, 'add_review.html', {'form': form, 'conferences': Conference.objects.all()})


def add_research_paper(request):
    if request.method == 'POST':
        conference_id = request.POST.get('conference')
        conference = Conference.objects.get(pk=conference_id)
        research_paper = request.FILES.get('paper')

        if research_paper:
            conference.research_paper = research_paper
            conference.save()
            return redirect('user_dashboard')
    else:
        form = ResearchPaperForm()
    return render(request, 'add_research_paper.html', {'form': form, 'conferences': Conference.objects.all()})





def reviewer_dashboard(request):
    myconferences = Conference.objects.all().values()
    template = loader.get_template('reviewer_dashboard.html')
    context = {
        'myconferences': myconferences,
    }
    return HttpResponse(template.render(context, request))

def user_dashboard(request):
    myconferences = Conference.objects.all().values()
    template = loader.get_template('user_dashboard.html')
    context = {
        'myconferences': myconferences,
    }
    return HttpResponse(template.render(context, request))



def chair_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        chair = Chair.objects.filter(username=username, password=password).first()
        
        if chair:
            # Authentication successful, redirect to chair dashboard or any other page
            return redirect('conferences')
        else:
            # Authentication failed, redirect back to login page or display an error message
            return render(request, 'chair_login.html', {'error_message': 'Invalid username or password'})
    
    return render(request, 'chair_login.html')



def reviewer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        reviewer = Reviewer.objects.filter(username=username, password=password).first()
        
        if reviewer:
            # Authentication successful, redirect to chair dashboard or any other page
            return redirect('reviewer_dashboard')
        else:
            # Authentication failed, redirect back to login page or display an error message
            return render(request, 'reviewer_login.html', {'error_message': 'Invalid username or password'})
    
    return render(request, 'reviewer_login.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()
        
        if user:
            # Authentication successful, redirect to chair dashboard or any other page
            return redirect('user_dashboard')
        else:
            # Authentication failed, redirect back to login page or display an error message
            return render(request, 'user_login.html', {'error_message': 'Invalid username or password'})
    
    return render(request, 'user_login.html')

# Registration Views
def chair_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        Chair.objects.create(username=username, password=password)
        return redirect('chair_login')
    return render(request, 'chair_registration.html')

def reviewer_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # Handle other form fields and create Reviewer instance
        password=request.POST.get('password')
        Reviewer.objects.create(username=username,password=password)
        return redirect('reviewer_login')
    return render(request, 'reviewer_registration.html')

def user_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # Handle other form fields and create User instance
        password=request.POST.get('password')
        User.objects.create(username=username,password=password)
        return redirect('user_login')
    return render(request, 'user_registration.html')


def login(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'chair':
            return redirect('chair_login')
        elif role == 'user':
            return redirect('user_login')
        elif role == 'reviewer':
            return redirect('reviewer_login')
    return render(request, 'login.html')

def edit_conference(request, conference_id):
    conference = get_object_or_404(Conference, pk=conference_id)
    if request.method == 'POST':
        # Update conference details
        conference.title = request.POST.get('title')
        conference.description = request.POST.get('description')
        conference.start_date = request.POST.get('start_date')
        conference.end_date = request.POST.get('end_date')
        conference.save()
        return redirect('conferences')
    return render(request, 'edit_conference.html', {'conference': conference})

def delete_conference(request, conference_id):
    conference = get_object_or_404(Conference, pk=conference_id)
    if request.method == 'POST':
        conference.delete()
        return redirect('conferences')
    return render(request, 'delete_conference.html', {'conference': conference})

def create_conference(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        Conference.objects.create(title=title, description=description, start_date=start_date, end_date=end_date)
        message = "Conference created successfully!"
    else:
        message = ""
    return render(request, 'create_conference.html', {'message': message})

def conferences(request):
    myconferences = Conference.objects.all().values()
    template = loader.get_template('all_conferences.html')
    context = {
        'myconferences': myconferences,
    }
    return HttpResponse(template.render(context, request))
# Create your views here.

