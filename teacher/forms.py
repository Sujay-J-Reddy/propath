from django import forms
from .models import InstructorFeedback

class InstructorFeedbackForm(forms.ModelForm):
    class Meta:
        model = InstructorFeedback
        fields = [
            'completed_level',
            'current_level',
            'center_name',
            'center_address',
            'punctuality',
            'attention_to_instructor',
            'problem_solving_skills',
            'innovative_method',
            'teaching_method',
            'sharing_experiences',
            'comments_suggestions',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add radio buttons for feedback options
        feedback_fields = [
            'punctuality',
            'attention_to_instructor',
            'problem_solving_skills',
            'innovative_method',
            'teaching_method',
            'sharing_experiences',
        ]
        for field_name in feedback_fields:
            self.fields[field_name] = forms.ChoiceField(
                choices=InstructorFeedback.FEEDBACK_CHOICES,
                widget=forms.RadioSelect,
            )

    def clean(self):
        cleaned_data = super().clean()

        # Add any additional validation logic here if needed

        return cleaned_data
