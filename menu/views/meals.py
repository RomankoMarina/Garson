from django.shortcuts import render

# Create your views here.
"""
def cams(request):
    print(os.getcwd())
    cams = Cam.objects.order_by('-pk')[:30]
    if request.method == "POST":
        form = CamFilter(request.POST)
        if form.is_valid():

            namefilter=form.cleaned_data['namefilter']
            cams = Cam.objects.filter(title__icontains=namefilter)[:30]


            return render(request, 'VN/cams.html', {'form': form, 'cams': cams})


    else:
        form = CamFilter()
    return render(request, 'VN/cams.html', {'form': form, 'cams': cams})

"""
from django.shortcuts import render, redirect,get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from menu.models.meal import Meal
from menu.forms.meal import MealForm


def meals(request: WSGIRequest) -> render:
    if request.method == "POST":
        form = MealForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form.save_m2m()
            return redirect('meals')

    context = {'data': request,
               "form": MealForm()
               }

    query_set = Meal.objects.all()
    context.update({"meals": query_set})
    return render(request, 'meals.html', context)


def meal_edit(request, nn):
    instance = get_object_or_404(Meal, pk=nn)  # BD
    if request.method == "POST":
        form = MealForm(request.POST, request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            form.save_m2m()
            return redirect('meals')
    else:
        form = MealForm(instance=instance)   # for HTML
    return render(request, 'meal.html', {'form': form})


def meal_delete(request, nn):
    instance = get_object_or_404(Meal, pk=nn)
    instance.delete()
    return redirect('meals')