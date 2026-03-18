<!-- POST Method
def post(self, request, pk): -->
This defines what happens when the view receives a POST request.
pk → primary key of the habit we want to mark done.

request → contains user info, form data, etc.

<!-- get_object_or_404(Habit, pk=pk, user=request.user): -->
Fetches the specific habit by its primary key (pk) and ensures it belongs to the logged-in user.
If the habit doesn’t exist or belongs to another user, it raises a 404 error.

<!-- today = timezone.now().date(): -->
Gets the current date (ignoring time) because streaks are calculated per day, not per exact time.

<!-- Check if already marked today:
if habit.last_marked_date == today:
    return redirect("habit-list") -->
Prevents the user from marking the same habit multiple times in one day.

<!-- Calculate streak:
difference = (today - habit.last_marked_date).days -->

If the habit was marked yesterday (difference == 1), the streak continues → increment by 1.

If the habit wasn’t marked for more than a day (difference > 1), the streak breaks → reset to 1.

If this is the first time marking the habit (last_marked_date is None), start streak at 1.

<!-- Update last marked date:
habit.last_marked_date = today
habit.save() -->

Saves the new streak and the date it was marked.

Redirect:
After marking done, the user is sent back to the habit list.



<!-- 2️⃣ Why we pass today

In your template, you have: -->

<button type="submit" class="btn btn-primary" {% if habit.last_marked_date == today %}disabled{% endif %}>
  {% if habit.last_marked_date == today %}Done Today{% else %}Mark Done{% endif %}
</button>

Here, you compare habit.last_marked_date with today.

But today is not automatically available in the template. Django doesn’t know you want it.

So we add it to the context:

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)  # get the default context
    context['today'] = timezone.now().date()      # add today
    return context                                 # return the updated context

Now, in your template, {% if habit.last_marked_date == today %} will work, because today exists.