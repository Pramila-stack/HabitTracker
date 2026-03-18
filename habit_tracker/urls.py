from django.urls import path

from habit_tracker import views

urlpatterns = [
    path("",views.HabitListView.as_view(),name="habit-list"),
    path("habit-create/",views.HabitCreateView.as_view(),name="habit-create"),
    path("mark-done/<int:pk>/",views.MarkDoneView.as_view(),name="mark-done"),
    path("habit-detail/<int:pk>/",views.HabitDetailView.as_view(),name="habit-detail")
]