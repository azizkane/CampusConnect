from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

CATEGORY_CHOICES = [
    ('default', 'Select a category'),
    ('Seminar', 'Seminar'),
    ('Workshop', 'Workshop'),
    ('StudySession', 'StudySession'),
    ('ClubActivity', 'ClubActivity'),
    ('ClassProject', 'ClassProject'),
    ('ResearchProject', 'ResearchProject'),
    ('Presentation', 'Presentation'),
    ('Conference', 'Conference'),
    ('OpenDay', 'OpenDay'),
    ('GroupWork', 'GroupWork'),
    ('IndividualWork', 'IndividualWork'),
    ('Competition', 'Competition'),
    ('Exhibition', 'Exhibition'),
    ('FieldTrip', 'FieldTrip'),
    ('CaseStudy', 'CaseStudy'),
    ('Thesis', 'Thesis'),
    ('Internship', 'Internship'),
    ('Mentorship', 'Mentorship'),
    ('PeerTutoring', 'PeerTutoring'),
    ('SkillsWorkshop', 'SkillsWorkshop'),
    ('TechnicalProject', 'TechnicalProject'),
    ('CreativeProject', 'CreativeProject'),
    ('CommunityService', 'CommunityService'),
    ('StartupProject', 'StartupProject'),
    ('Innovation', 'Innovation'),
    ('Hackathon', 'Hackathon'),
    ('DebateCompetition', 'DebateCompetition'),
    ('AcademicContest', 'AcademicContest'),
]
# Pour définir une valeur par défaut dans un champ de modèle Django utilisant ces choix:
# category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Seminar')

ACCESS_LEVEL_CHOICES = [
    ('Public', 'Public'),
    ('School', 'School'),
    ('Department', 'Department'),
    ('Private', 'Private'),
]