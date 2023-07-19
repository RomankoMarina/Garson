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
from geo.models.region import Region
from geo.forms.regions import RegionForm

def regions(request):
    if request.method == "POST":
        form = RegionForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()

            return redirect('regions')

    context = {'data' : request,
               "form" : RegionForm()
        }

    query_set = Region.objects.all()
    context.update({"regions": query_set})
    return render(request, 'regions.html',context)


