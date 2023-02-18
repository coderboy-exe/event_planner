from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

# Create your views here.

# CRUD

# Return all listings
def all_listings(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)

# Return a particular listing by id
def get_listing(request, id):
    listing = Listing.objects.get(id=id)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)

# Creates a new listing
def create_listing(request):
    form = ListingForm()
    # Validate request
    if request.method == "POST":
        form = ListingForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save() # This method is available on model forms
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "create_listing.html", context)


# Updates a  listing
def update_listing(request, id):
    listing = Listing.objects.get(id=id)
    form = ListingForm(instance=listing)

    # Validate request
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        print(request.POST)
        if form.is_valid():
            form.save() # This method is available on model forms
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "update_listing.html", context)

def delete_listing(request, id):
    listing = Listing.objects.get(id=id)
    listing.delete()
    return redirect("/")