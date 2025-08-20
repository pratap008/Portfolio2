from django.contrib import admin
from .models import (
    Hero,
    Technology,
    About,
    SkillCategory,
    Skill,
    ProcessStep,
    Project,
    Stat,
    Article,
    Contact,
    ContactMessage,
    SocialLink,
)

# --- Admin Customizations ---

# Inline Skill editing within SkillCategory
class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1  # How many extra forms to show

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    inlines = [SkillInline]
    list_display = ("name",)

# Customize the display for Projects
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "case_study_link", "github_link")
    search_fields = ("title", "description")

# Customize the display for Articles
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date", "read_time")
    list_filter = ("published_date",)
    search_fields = ("title", "description")

# Customize the display for Contact Messages (Read-Only)
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("name", "email", "subject", "message", "created_at")

    def has_add_permission(self, request):
        return False # Prevent adding new messages from the admin

    def has_delete_permission(self, request, obj=None):
        return True # Allow deleting messages

# --- Singleton Model Admin (Allow only one instance) ---

class SingletonModelAdmin(admin.ModelAdmin):
    """A ModelAdmin that prevents the creation of more than one instance."""
    def has_add_permission(self, request):
        # If there's already an object, don't allow adding another
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

# --- Registering Models ---

# Register models with basic display
admin.site.register(Technology)
admin.site.register(ProcessStep)
admin.site.register(Stat)
admin.site.register(SocialLink)
admin.site.register(Skill) # Also register Skill separately for direct access if needed

# Register Singleton models
admin.site.register(Hero, SingletonModelAdmin)
admin.site.register(About, SingletonModelAdmin)
admin.site.register(Contact, SingletonModelAdmin)

# Note: SkillCategory, Project, Article, and ContactMessage are registered
# above using the @admin.register decorator with their custom admin classes.
