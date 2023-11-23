from django.db import models
from accounts.models import CustomUser

class InstructorFeedback(models.Model):
    SATISFACTORY = 'Satisfactory'
    UNSATISFACTORY = 'Unsatisfactory'

    FEEDBACK_CHOICES = [
        (SATISFACTORY, 'Satisfactory'),
        (UNSATISFACTORY, 'Unsatisfactory'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='instructor_feedbacks')
    completed_level = models.CharField(max_length=255)
    current_level = models.CharField(max_length=255)
    center_name = models.CharField(max_length=255)
    center_address = models.TextField()
    
    punctuality = models.CharField(choices=FEEDBACK_CHOICES, max_length=15)
    attention_to_instructor = models.CharField(choices=FEEDBACK_CHOICES, max_length=15)
    problem_solving_skills = models.CharField(choices=FEEDBACK_CHOICES, max_length=15)
    innovative_method = models.CharField(choices=FEEDBACK_CHOICES, max_length=15)
    teaching_method = models.CharField(choices=FEEDBACK_CHOICES, max_length=15)
    sharing_experiences = models.CharField(choices=FEEDBACK_CHOICES, max_length=15)
    
    comments_suggestions = models.TextField(null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Instructor Feedback - {self.user.username} - {self.date}"
