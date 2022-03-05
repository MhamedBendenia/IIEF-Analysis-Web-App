from django.db import models

# Confidence choices list
CONFIDENCE_CHOICES = [
        (1, 'Very low'),
        (2, 'Low'),
        (3, 'Moderate'),
        (4, 'High'),
        (5, 'Very high'),
    ]

# Completion choices list
COMPLETION_CHOICES = [
        (1, 'Extremely difficult'),
        (2, 'Very difficult'),
        (3, 'Difficult'),
        (4, 'Slightly difficult'),
        (5, 'Not difficult'),
    ]
# Penetration, Intercourse, and Satisfaction choices list
COMMUN_CHOICES = [
        (1, 'Almost never or never'),
        (2, 'A few times'),
        (3, 'Sometimes'),
        (4, 'Most times'),
        (5, 'Almost always or always'),
    ]

class IiefQuestionnaire(models.Model):
    
    confidence = models.CharField(max_length=9, choices=CONFIDENCE_CHOICES)
    penetration = models.CharField(max_length=23, choices=COMMUN_CHOICES)
    intercourse = models.CharField(max_length=23, choices=COMMUN_CHOICES)
    completion = models.CharField(max_length=19, choices=COMPLETION_CHOICES)
    satisfaction = models.CharField(max_length=23, choices=COMMUN_CHOICES)
    score = models.IntegerField(blank=True, null=True)

    # Auto calculating the score
    def save(self, *args, **kwargs):
        self.score = self.confidence + self.penetration + self.intercourse + self.completion + self.satisfaction
        super(IiefQuestionnaire, self).save(*args, **kwargs)
        