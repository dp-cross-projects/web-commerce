from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello World</h1>")

def about(request):
    return HttpResponse("about")

# Backend User Profile Functions
# Get all user profiles?

# Get a user by id

# Create a user

# Update a user

# Delete a user



# Backend User History Functions
# Get all user_history profiles?

# Get a user_history by id

# Create a user_history

# Update a user_history

# Delete a user_history