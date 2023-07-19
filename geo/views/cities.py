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
from django.shortcuts import render,redirect
from geo.models.city import City
from geo.forms.cities import CityForm

def cities(request):
    if request.method == "POST":
        form = CityForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()

            return redirect('cities')

    context = {'data' : request,
               "form" : CityForm()
        }

    query_set = City.objects.all()
    context.update({"cities": query_set})
    return render(request, 'cities.html',context)


