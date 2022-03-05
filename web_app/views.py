from rest_framework import viewsets
from .serializers import IiefQuestionnaireSerializer
from .models import IiefQuestionnaire
from rest_framework.response import Response
from rest_framework import status

# IIEF Questionnaire ViewSet
class IiefQuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = IiefQuestionnaire.objects.all()
    serializer_class = IiefQuestionnaireSerializer

    # Overriding the create method response
    def create(self, request, *args, **kwargs):
        res = super(IiefQuestionnaireViewSet, self).create(request, *args, **kwargs)
        return Response({"type":"IiefQuestionnaire","id":res.data['id'],"attributes":{"score":res.data['score']}}, status=status.HTTP_201_CREATED)
