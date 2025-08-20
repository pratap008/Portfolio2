from django.shortcuts import render
from .models import (
    Hero,
    Technology,
    About,
    SkillCategory,
    ProcessStep,
    Project,
    Stat,
    Article,
    Contact,
    SocialLink
)

def home(request):
    hero = Hero.objects.first(),
    technologies = Technology.objects.all()
    about = About.objects.first()
    skill_categories = SkillCategory.objects.all()
    process_steps = ProcessStep.objects.all()
    recent_projects = Project.objects.order_by('-id')[:4]
    stats = Stat.objects.all()
    latest_articles = Article.objects.order_by('-published_date')[:3]
    contact = Contact.objects.first()
    social_links = SocialLink.objects.all()

    context = {
        'hero' : hero,
        'technologies' : technologies,
        'about' : about,
        'skill_categories' : skill_categories,
        'process_steps' : process_steps,
        'recent_projects' : recent_projects,
        'stats' : stats,
        'latest_articles' : latest_articles,
        'contact' : contact,
        'social_links' : social_links,
    }

    return render(request, 'portfolio/home.html', context)

def articles(request):
    articles = Article.objects.all()
    
    context = {
        'articles' : articles,
    }
    return render(request, 'portfolio/articles.html', context)

def projects(request):
    projects = Project.objects.all()
    
    context = {
        'projects' : projects,
    }
    return render(request, 'portfolio/projects.html', context)

def contact_me(request):
    return render(request, 'portfolio/contactme.html')