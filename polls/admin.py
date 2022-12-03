from django.contrib import admin
from .models import Question ,Choice

class Choice_admin(admin.TabularInline):
	model = Choice
	extra = 5
class Question_admin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['question_content']}), ('Date Information', {'fields': ['date_posted'], 'classes': ['collapse']}), ]
	inlines = [Choice_admin]
  
  
admin.site.register(Question, Question_admin)	
