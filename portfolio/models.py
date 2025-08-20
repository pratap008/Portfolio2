from django.db import models


# Hero Section
class Hero(models.Model):
    title = models.CharField(max_length=200)  # e.g. CREATIVE WEB DEVELOPER
    subtitle = models.TextField()  # Short intro text
    image = models.ImageField(upload_to="hero/", blank=True, null=True)

    def __str__(self):
        return self.title


# Tech Banner (scrolling technologies)
class Technology(models.Model):
    name = models.CharField(max_length=100)  # e.g. ReactJS, NodeJS

    def __str__(self):
        return self.name


# About Me Section
class About(models.Model):
    heading = models.CharField(max_length=200, default="ABOUT ME")
    short_description = models.TextField()
    long_description = models.TextField()

    def __str__(self):
        return self.heading


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)  # e.g. Strategy, My Skills, Advice

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=100)  # e.g. React, Brand Building

    def __str__(self):
        return self.name


# Working Process
class ProcessStep(models.Model):
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ["step_number"]

    def __str__(self):
        return f"{self.step_number}. {self.title}"


# Projects
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/")
    case_study_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


# Stats Section
class Stat(models.Model):
    label = models.CharField(max_length=100)  # e.g. Completed Projects
    value = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.value} {self.label}"


# Blog / Articles
class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="articles/")
    published_date = models.DateField()
    read_time = models.CharField(max_length=50, help_text="e.g. '7 Min Read'")
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


# Contact Section
class Contact(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"



# Footer Links
class SocialLink(models.Model):
    name = models.CharField(max_length=50)  # GitHub, Twitter, LinkedIn
    url = models.URLField()

    def __str__(self):
        return self.name


