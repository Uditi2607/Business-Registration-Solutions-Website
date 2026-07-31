"""Views for dedicated service landing pages.

Keep service-specific views here as the catalogue grows, while general website
pages remain in ``views.py``.
"""

from django.shortcuts import render


def gst_registration(request):
    """Render the GST Registration service page."""
    return render(request, "services/gst_registration.html")


def msme_registration(request):
    """Render the MSME / Udyam Registration service page."""
    return render(request, "services/msme_registration.html")


def fssai_registration(request):
    """Render the FSSAI Registration and Food License service page."""
    return render(request, "services/fssai_registration.html")


def iec_registration(request):
    """Render the Import Export Code registration service page."""
    return render(request, "services/iec_registration.html")


def pan_tan_services(request):
    """Render the PAN and TAN registration services page."""
    return render(request, "services/pan_tan_services.html")


def shop_establishment_registration(request):
    """Render the Shop and Establishment registration service page."""
    return render(request, "services/shop_establishment_registration.html")


def startup_india_registration(request):
    """Render the Startup India Registration service page."""
    return render(request, "services/startup_india_registration.html")


def gem_registration(request):
    """Render the GeM Seller Registration service page."""
    return render(request, "services/gem_registration.html")


def trademark_registration(request):
    """Render the Trademark Registration service page."""
    return render(request, "services/trademark_registration.html")


def copyright_registration(request):
    """Render the Copyright Registration service page."""
    return render(request, "services/copyright_registration.html")


def aadhaar_services(request):
    """Render the Aadhaar Services assistance page."""
    return render(request, "services/aadhaar_services.html")


def voter_id_services(request):
    """Render the Voter ID Services assistance page."""
    return render(request, "services/voter_id_services.html")


def passport_services(request):
    """Render the Passport Services assistance page."""
    return render(request, "services/passport_services.html")



