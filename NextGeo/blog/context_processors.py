from .models import Category

#function that gets all categories
def get_all_categories(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    
    return context
