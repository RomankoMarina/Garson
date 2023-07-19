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
from menu.models.category import Category
from menu.forms.category import CategoryForm


def categories(request: WSGIRequest) -> render:
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()

            return redirect('categories')

    context = {'data': request,
               "form": CategoryForm()
               }

    query_set = Category.objects.all()
    context.update({"categories": query_set})
    return render(request, 'categories.html', context)


def category_edit(request, nn):
    instance = get_object_or_404(Category, pk=nn)  # BD
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=instance)   # for HTML
    return render(request, 'category.html', {'form': form})


def category_delete(request, nn):
    instance = get_object_or_404(Category, pk=nn)
    instance.delete()
    return redirect('category')