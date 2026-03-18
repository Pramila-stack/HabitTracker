from django import forms

from habit_tracker.models import Habit


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ["name","streak"]
        