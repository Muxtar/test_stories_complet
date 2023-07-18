from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from home.models import Contact, AboutUs, Category, Story, Subcribe
from home.forms import ContactForm, ContactForm2
# from django.http import HttpResponse
# from django.template import loader

# def render(request, html):
#     html = loader.get_template('index.html')
#     return HttpResponse(html.render())

a = 'aysel'

class Home(TemplateView):
   template_name = 'index.html'

def home(request):  
   context = {
               'recent_stories':Story.objects.all().order_by('-id')[:4], # select * from Story order by id desc limit 4
               'slider':Story.objects.all().order_by('-id')[:3] # select * from Story order by id desc limit 2

            }
   return render(request, 'index.html', context=context)

def contact(request):
   form = ContactForm2()
   if request.method == 'POST':
      # name = request.POST.get('name')
      # email = request.POST.get('email')
      # subject = request.POST.get('subject')    
      # message = request.POST.get('message')
      # form = ContactForm(request.POST)
      # if form.is_valid():
      #    Contact.objects.create(name = form.cleaned_data['name'], email = form.cleaned_data['email'], subject = form.cleaned_data['subject'], message = form.cleaned_data['message'])

      form = ContactForm2(request.POST)
      if form.is_valid():
         form.save()

   context = {
                  'form':form, 
                  'aboutUs':AboutUs.objects.get(id = 1),
                  'a':a
            }
   return render(request, 'contact.html', context)

def about(request):
   return render(request=request, template_name='about.html')

def stories(request, slug = None):
   stories = Story.objects.all()
   if slug:
      stories = stories.filter(category__slug = slug)
   context = {
      'stories': stories,
   }
   return render(request=request, template_name='stories.html', context = context)

def single(request, slug):
   story = Story.objects.get(slug = slug)
   context = {'story':story}
   return render(request, 'single.html', context)

def recipes(request):
   return render(request=request, template_name='recipes.html')

def create_story(request):
   return render(request, 'create_story.html')

def subscribe(request):
   if request.method == 'POST':
      email = request.POST.get('email')
      try:
         Subcribe.objects.create(email = email)
         return JsonResponse({'message':'Success'})
      except:
         JsonResponse.status_code = 404
         return JsonResponse({'message':'already exists'})
      