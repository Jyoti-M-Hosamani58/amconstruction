from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from Am_app.models import Login ,Service_image, Residential,Building,Struturaldesign,Renovation,Swimming,Freelancing,Joinventure,Landscape,Fabrication,Paintcontract,Retro,Completed_project,Ongoing_project,Elevation,Dop,Certificate,Listofmachine
from django.views.decorators.http import require_http_methods
from pyexpat.errors import messages




# Create your views here.
def index(request):  # Fetch all service images from the database
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            udata = Login.objects.get(username=username)
            if password == udata.password:  # Use hashed password checks in production
                request.session['username'] = username
                request.session['utype'] = udata.utype

                if udata.utype == 'user':
                    return redirect('index')  # Redirect to a user-specific page
                else:
                    return redirect('admin_dashboard')  # Adjust as necessary
            else:
                messages.error(request, 'Invalid password')
        except Login.DoesNotExist:
            messages.error(request, 'Invalid Username')

    return render(request, 'login.html')





def admin_dashboard(request):
    return render(request,'admin_dshboard.html')


def service(request):
    return render(request,'service.html')


def upload_service_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Service_image(image=image, description=desc)
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Service_image.objects.all()  # Fetch all images to display on the page
    return render(request, 'service.html', {'success': success, 'images': images})


def service_view(request):
    services = Service_image.objects.all()  # Fetch all service images
    return render(request, 'service_view.html', {'services': services})


def service_view1(request):
    services = Service_image.objects.all()  # Fetch all service images
    return render(request, 'service_view1.html', {'services': services})

def elevation(request):
    return render(request,'elevation.html')

def upload_Elevation_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Residential(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Residential.objects.all()  # Fetch all images to display on the page
    return render(request, 'elevation.html', {'success': success, 'images': images})


def elevation_view(request):
    images = Residential.objects.all()  # Fetch all Residential objects
    return render(request, 'elevation_view.html', {'images': images})

def elevation_view1(request):
    images = Residential.objects.all()  # Fetch all Residential objects
    return render(request, 'elevation_view1.html', {'images': images})

def building(request):
    return render(request,'building.html')

def upload_building_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Building(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Building.objects.all()  # Fetch all images to display on the page
    return render(request, 'building.html', {'success': success, 'images': images})


def building_view(request):
    images = Building.objects.all()  # Fetch all Residential objects
    return render(request, 'building_view.html', {'images': images})

def building_view1(request):
    images = Building.objects.all()  # Fetch all Residential objects
    return render(request, 'building_view1.html', {'images': images})

@require_http_methods(["DELETE"])
def delete_building(request, image_id):
    try:
        image = Building.objects.get(id=image_id)
        image.delete()
        return JsonResponse({'success': True})
    except Building.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Image not found.'}, status=404)


def structural(request):
    return render(request,'structural.html')

def upload_structural_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Struturaldesign(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Struturaldesign.objects.all()  # Fetch all images to display on the page
    return render(request, 'structural.html', {'success': success, 'images': images})


def structural_view(request):
    images = Struturaldesign.objects.all()  # Fetch all Residential objects
    return render(request, 'structural_view.html', {'images': images})



def structural_view1(request):
    images = Struturaldesign.objects.all()  # Fetch all Residential objects
    return render(request, 'structural_view1.html', {'images': images})


@require_http_methods(["DELETE"])
def delete_strutural(request, image_id):
    try:
        image = Struturaldesign.objects.get(id=image_id)
        image.delete()
        return JsonResponse({'success': True})
    except Struturaldesign.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Image not found.'}, status=404)





def renovation(request):
    return render(request,'renovation.html')

def upload_renovation_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Renovation(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Renovation.objects.all()  # Fetch all images to display on the page
    return render(request, 'renovation.html', {'success': success, 'images': images})


def renovation_view(request):
    images = Renovation.objects.all()  # Fetch all Residential objects
    return render(request, 'renovation_view.html', {'images': images})


def renovation_view1(request):
    images = Renovation.objects.all()  # Fetch all Residential objects
    return render(request, 'renovation_view1.html', {'images': images})

def swimming(request):
    return render(request,'swimming.html')

def upload_swimming_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Swimming(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Swimming.objects.all()  # Fetch all images to display on the page
    return render(request, 'swimming.html', {'success': success, 'images': images})


def swimming_view(request):
    images = Swimming.objects.all()  # Fetch all Residential objects
    return render(request, 'swimming_view.html', {'images': images})


def swimming_view1(request):
    images = Swimming.objects.all()  # Fetch all Residential objects
    return render(request, 'swimming_view1.html', {'images': images})



def freelancing(request):
    return render(request,'freelancing.html')

def upload_freelancing_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Freelancing(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Freelancing.objects.all()  # Fetch all images to display on the page
    return render(request, 'freelancing.html', {'success': success, 'images': images})


def freelancing_view(request):
    images = Freelancing.objects.all()  # Fetch all Residential objects
    return render(request, 'freelancing_view.html', {'images': images})


def freelancing_view1(request):
    images = Freelancing.objects.all()  # Fetch all Residential objects
    return render(request, 'freelancing_view1.html', {'images': images})




def joinventure(request):
    return render(request,'joinventure.html')

def upload_joinventure_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Joinventure(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Joinventure.objects.all()  # Fetch all images to display on the page
    return render(request, 'joinventure.html', {'success': success, 'images': images})


def joinventure_view(request):
    images = Joinventure.objects.all()  # Fetch all Residential objects
    return render(request, 'joinventure_view.html', {'images': images})


def joinventure_view1(request):
    images = Joinventure.objects.all()  # Fetch all Residential objects
    return render(request, 'joinventure_view1.html', {'images': images})


def landscape(request):
    return render(request,'landscape.html')

def upload_landscape_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Landscape(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Landscape.objects.all()  # Fetch all images to display on the page
    return render(request, 'landscape.html', {'success': success, 'images': images})


def landscape_view(request):
    images = Landscape.objects.all()  # Fetch all Residential objects
    return render(request, 'landscape_view.html', {'images': images})

def landscape_view1(request):
    images = Landscape.objects.all()  # Fetch all Residential objects
    return render(request, 'landscape_view1.html', {'images': images})





def fabrication(request):
    return render(request,'fabrication.html')

def upload_fabrication_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Fabrication(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Fabrication.objects.all()  # Fetch all images to display on the page
    return render(request, 'fabrication.html', {'success': success, 'images': images})


def fabrication_view(request):
    images = Fabrication.objects.all()  # Fetch all Residential objects
    return render(request, 'fabrication_view.html', {'images': images})



def fabrication_view1(request):
    images = Fabrication.objects.all()  # Fetch all Residential objects
    return render(request, 'fabrication_view1.html', {'images': images})




def paintcontract(request):
    return render(request,'paintcontract.html')

def upload_paintcontract_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Paintcontract(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Paintcontract.objects.all()  # Fetch all images to display on the page
    return render(request, 'paintcontract.html', {'success': success, 'images': images})


def paintcontract_view(request):
    images = Paintcontract.objects.all()  # Fetch all Residential objects
    return render(request, 'paintcontract_view.html', {'images': images})



def paintcontract_view1(request):
    images = Paintcontract.objects.all()  # Fetch all Residential objects
    return render(request, 'paintcontract_view1.html', {'images': images})


def retro_fitting(request):
    return render(request,'retro_fitting.html')

def upload_paintcontract_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Retro(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Retro.objects.all()  # Fetch all images to display on the page
    return render(request, 'retro_fitting.html', {'success': success, 'images': images})


def retro_fitting_view(request):
    images = Retro.objects.all()  # Fetch all Residential objects
    return render(request, 'retro_fitting_view.html', {'images': images})


def retro_fitting_view1(request):
    images = Retro.objects.all()  # Fetch all Residential objects
    return render(request, 'retro_fitting_view1.html', {'images': images})




def completed_project(request):
    return render(request,'completed_project.html')
def upload_completed_project(request):
    success = None
    if request.method == 'POST' and request.FILES:
        title = request.POST.get('title')  # Get the project title
        description = request.POST.get('description')  # Get the description
        image_file = request.FILES['image']  # Get the image file

        # Save the project details into the database
        new_project = Completed_project(title=title, description=description, image=image_file)
        new_project.save()

        success = 'Project uploaded successfully!'

    # Fetch all projects to display them
    projects = Completed_project.objects.all()
    return render(request, 'completed_project.html', {'success': success, 'projects': projects})

def completed_project_view(request):
    projects = Completed_project.objects.all()  # Fetch all Residential objects
    return render(request, 'completed_project_view.html', {'projects': projects})


def completed_project_view1(request):
    projects = Completed_project.objects.all()  # Fetch all Residential objects
    return render(request, 'completed_project_view1.html', {'projects': projects})


def ongoing_project(request):
    return render(request,'ongoing_project.html')

def upload_ongoing_project(request):
    success = None
    if request.method == 'POST' and request.FILES:
        title = request.POST.get('title')  # Get the project title
        description = request.POST.get('description')  # Get the description
        image_file = request.FILES['image']  # Get the image file

        # Save the project details into the database
        new_project = Ongoing_project(title=title, description=description, image=image_file)
        new_project.save()

        success = 'Project uploaded successfully!'

    # Fetch all projects to display them
    projects = Ongoing_project.objects.all()
    return render(request, 'ongoing_project.html', {'success': success, 'projects': projects})
def ongoing_project_view(request):
    projects = Ongoing_project.objects.all()  # Fetch all Residential objects
    return render(request, 'ongoing_project_view.html', {'projects': projects})

def ongoing_project_view1(request):
    projects = Ongoing_project.objects.all()  # Fetch all Residential objects
    return render(request, 'ongoing_project_view1.html', {'projects': projects})






def upload_dop(request):
    if request.method == 'POST':
        pdf = request.FILES.get('pdf')
        description = request.POST.get('description', '')

        if pdf:
            # Save the uploaded file and description
            dop = Dop(pdf=pdf, description=description)
            dop.save()

            return redirect('dop')  # Redirect to a success page or another view

    return render(request, 'dop.html')

def dop(request):
    return render(request,'dop.html')


def dop_view1(request):
    dop_objects = Dop.objects.all()  # Retrieve all Dop records
    return render(request, 'dop_view1.html', {'dop_objects': dop_objects})

def dop_view(request):
    dop_objects = Dop.objects.all()  # Retrieve all Dop records
    return render(request, 'dop_view.html', {'dop_objects': dop_objects})


def certificate(request):
    return render(request,'dop.html')



def upload_certificate(request):
    if request.method == 'POST':
        pdf = request.FILES.get('pdf')
        description = request.POST.get('description', '')

        if pdf:
            # Save the uploaded file and description
            dop = Certificate(pdf=pdf, description=description)
            dop.save()

            return redirect('certificate')  # Redirect to a success page or another view

    return render(request, 'certificate.html')


def certificate_view1(request):
    dop_objects = Certificate.objects.all()  # Retrieve all Dop records
    return render(request, 'certificate_view1.html', {'dop_objects': dop_objects})

def certificate_view(request):
    dop_objects = Certificate.objects.all()  # Retrieve all Dop records
    return render(request, 'dop_view.html', {'dop_objects': dop_objects})

def listofmachine(request):
    return render(request,'listofmachine.html')


def upload_listofmachine(request):
    if request.method == 'POST':
        pdf = request.FILES.get('pdf')
        description = request.POST.get('description', '')

        if pdf:
            # Save the uploaded file and description
            dop = Listofmachine(pdf=pdf, description=description)
            dop.save()

            return redirect('listofmachine')  # Redirect to a success page or another view

    return render(request, 'listofmachine.html')


def listofmachine_view1(request):
    dop_objects = Listofmachine.objects.all()  # Retrieve all Dop records
    return render(request, 'listofmachine_view1.html', {'dop_objects': dop_objects})

def listofmachine_view(request):
    dop_objects = Listofmachine.objects.all()  # Retrieve all Dop records
    return render(request, 'listofmachine_view.html', {'dop_objects': dop_objects})



def about(request): # Retrieve all Directos objects
    return render(request, 'about.html')