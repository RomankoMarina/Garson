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
from menu.models.feature import Feature
from menu.forms.feature import FeatureForm


def features(request: WSGIRequest) -> render:
    if request.method == "POST":
        form = FeatureForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()

            return redirect('features')

    context = {'data': request,
               "form": FeatureForm()
               }

    query_set = Feature.objects.all()
    context.update({"features": query_set})
    return render(request, 'features.html', context)


def feature_edit(request, nn):
    instance = get_object_or_404(Place, pk=nn)  # BD
    if request.method == "POST":
        form = FeatureForm(request.POST, request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('features')
    else:
        form = FeatureForm(instance=instance)   # for HTML
    return render(request, 'feature.html', {'form': form})


def feature_delete(request, nn):
    instance = get_object_or_404(Feature, pk=nn)
    instance.delete()
    return redirect('feature')