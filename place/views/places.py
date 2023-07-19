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
from place.models.place import Place
from place.forms.places import PlaceForm


def places(request: WSGIRequest) -> render:
    if request.method == "POST":
        form = PlaceForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()

            return redirect('places')

    context = {'data': request,
               "form": PlaceForm()
               }

    query_set = Place.objects.all()
    context.update({"places": query_set})
    return render(request, 'places.html', context)


def place_edit(request, nn):
    instance = get_object_or_404(Place, pk=nn)  # BD
    if request.method == "POST":
        form = PlaceForm(request.POST, request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('places')
    else:
        form = PlaceForm(instance=instance)   # for HTML
    return render(request, 'place.html', {'form': form})


def place_delete(request, nn):
    instance = get_object_or_404(Place, pk=nn)
    instance.delete()
    return redirect('places')