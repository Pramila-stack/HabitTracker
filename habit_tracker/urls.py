from django.urls import path

from habit_tracker import views

urlpatterns = [
    path("",views.HabitListView.as_view(),name="habit-list"),
    path("create-habit/",views.HabitCreateView.as_view(),name="create-habit"),
    path("mark-done/<int:pk>/",views.MarkDoneView.as_view(),name="mark-done"),
    path("view-streak/<int:pk>/",views.ViewStreakView.as_view(),name="view-streak"),
    path("delete-habit/<int:pk>/",views.HabitDeleteView.as_view(),name="delete-habit"),
]