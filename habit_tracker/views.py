from datetime import timedelta

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from habit_tracker.forms import HabitForm
from habit_tracker.models import Habit
# Create your views here.

class HabitListView(LoginRequiredMixin,ListView):
    model = Habit
    template_name = "habit_list.html"
    context_object_name = "habits"

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user).order_by("-created_at")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now().date()
        return context

class HabitCreateView(LoginRequiredMixin,CreateView):
    model = Habit
    template_name = "create_habit.html"
    form_class = HabitForm
    success_url = reverse_lazy("habit-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class HabitDeleteView(LoginRequiredMixin,DeleteView):
    model = Habit
    template_name = "delete_confirm.html"
    context_object_name = "habit"
    success_url = reverse_lazy("habit-list")

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
    
class ViewStreakView(LoginRequiredMixin,DetailView):
    model = Habit
    template_name = "view_streak.html"
    context_object_name = "habit"

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        today = timezone.now().date()
        yesterday = today - timedelta(days=1)
        habit = self.object

        if habit.last_marked_date is None:
            status = "not_started"

        elif habit.last_marked_date == today:
            status = "completed_today"
        elif habit.last_marked_date == yesterday:
            status = "active"
        else:
            status = "broken"

        context['status'] = status

        return context





    
class MarkDoneView(LoginRequiredMixin,View):
    def post(self,request,pk):
        habit = get_object_or_404(Habit,pk=pk,user = self.request.user)

        today = timezone.now().date()

        yesterday = today - timedelta(days=1)

        if habit.last_marked_date == today:
            return redirect("habit-list")
        
        if habit.last_marked_date == yesterday:
            habit.streak += 1
        else:
            habit.streak = 1

        habit.last_marked_date = today
        habit.save()

        return redirect("habit-list")
