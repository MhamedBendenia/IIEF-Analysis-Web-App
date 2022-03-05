from .models import IiefQuestionnaire
from rest_framework_json_api import serializers

# IIEF Questionnaire Serializer
class IiefQuestionnaireSerializer(serializers.ModelSerializer):
    # Read only field
    score = serializers.IntegerField(read_only=True)

    class Meta:
        model = IiefQuestionnaire
        fields = '__all__'
    