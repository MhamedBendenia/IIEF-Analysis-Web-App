from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import IiefQuestionnaire

class IiefQuestionnaireTests(APITestCase):
    def test_create_iief_questionnaire(self):

        url = reverse('iiefquestionnaire-list')
        data = {"data": 
                    {"type": "IiefQuestionnaire", 
                     "attributes": {"confidence": 4, "penetration": 2, "intercourse": 4,"completion": 3, "satisfaction": 2}
                    }
                }
        response = self.client.post(url, data)

        # Ensure we can create a new iief_questionnaire object.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Ensure the iief_questionnaire object is well created.
        self.assertEqual(IiefQuestionnaire.objects.count(), 1)

        # Ensure the score is correct.
        self.assertEqual(IiefQuestionnaire.objects.get().score, 15)
