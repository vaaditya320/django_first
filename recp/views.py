from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def recipe(request):
    if request.method =="POST":
        data =  request.POST
        recipe_image = request.FILES.get('recipe_image') # this is how  you get file type
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        
        
        

        #this is how we create a data entry in sql using python
        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image
        )

        return redirect('/recipes/')
    
    queryset = Recipe.objects.all()
    context = {'recipe' : queryset}
    return render(request,  "recipes.html", context)


def update_recipe(request,  id):
    queryset = Recipe.objects.get(id = id)
    context = {'recipe' : queryset}
    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get('recipe_image') # this is how  you get file type data
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        
        # if you add a new image it will update else the old image remains there
        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/recipes/')

    return render(request,  "update_recipes.html", context)



def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipes/')