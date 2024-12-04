from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'recipes_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.list_recipes, name='list_recipes'),
    path('recipes/<int:id>/', views.getRecipeByID, name='recipe_by_id'),
    path('recipe/', views.createRecipe, name='create_recipe')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)