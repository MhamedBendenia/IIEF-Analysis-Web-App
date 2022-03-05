from django.contrib import admin
from django.template.response import TemplateResponse
from .models import IiefQuestionnaire, CONFIDENCE_CHOICES, COMMUN_CHOICES, COMPLETION_CHOICES
from django.db.models import Avg

class IiefQuestionnaireList(admin.ModelAdmin):
    list_display= ('id', 'show_confidence', 'show_penetration', 'show_intercourse', 'show_completion', 'show_satisfaction', 'score')

    # Getting Confidence choice value
    def show_confidence(self, obj):
        return dict(CONFIDENCE_CHOICES)[int(obj.confidence)]
    
    # Confidence column description
    show_confidence.short_description = 'confidence'


    # Getting Penetration choice value
    def show_penetration(self, obj):
        return dict(COMMUN_CHOICES)[int(obj.confidence)]
    
    # Penetration column description
    show_penetration.short_description = 'penetration'


    # Getting Intercourse choice value
    def show_intercourse(self, obj):
        return dict(COMMUN_CHOICES)[int(obj.confidence)]
    
    # Intercourse column description
    show_intercourse.short_description = 'intercourse'


    # Getting Completion choice value
    def show_completion(self, obj):
        return dict(COMPLETION_CHOICES)[int(obj.confidence)]
    
    # Completion column description
    show_completion.short_description = 'completion'


    # Getting Satisfaction choice value
    def show_satisfaction(self, obj):
        return dict(COMMUN_CHOICES)[int(obj.confidence)]
    
    # Satisfaction column description
    show_satisfaction.short_description = 'satisfaction'


    # Adding average_score to the admin/change_list.html page 
    def changelist_view(self, request, extra_context=""):
        response = super(IiefQuestionnaireList, self).changelist_view(request, extra_context)

        # Calculating the average score
        average_score = IiefQuestionnaire.objects.all().aggregate(Avg('score'))['score__avg']

        if average_score:
            extra_context = {
                'average_score': "%.2f" % average_score,
            }
            response.context_data.update(extra_context)

        return TemplateResponse(request, "admin/change_list.html", response.context_data)


admin.site.register(IiefQuestionnaire, IiefQuestionnaireList)