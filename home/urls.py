from django.urls import path
from . import service_views, views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/gst-registration/', service_views.gst_registration, name='gst_registration'),
    path('services/msme-udyam-registration/', service_views.msme_registration, name='msme_registration'),
    path('services/fssai-registration/', service_views.fssai_registration, name='fssai_registration'),
    path('services/import-export-code-registration/', service_views.iec_registration, name='iec_registration'),
    path('services/pan-tan-services/', service_views.pan_tan_services, name='pan_tan_services'),
    path('services/shop-establishment-registration/', service_views.shop_establishment_registration, name='shop_establishment_registration'),
    path('services/startup-india-registration/', service_views.startup_india_registration, name='startup_india_registration'),
    path('services/gem-seller-registration/', service_views.gem_registration, name='gem_registration'),
    path('services/trademark-registration/', service_views.trademark_registration, name='trademark_registration'),
    path('services/copyright-registration/', service_views.copyright_registration, name='copyright_registration'),
    path('services/aadhaar-services/', service_views.aadhaar_services, name='aadhaar_services'),
    path('services/voter-id-services/', service_views.voter_id_services, name='voter_id_services'),
    path('services/passport-services/', service_views.passport_services, name='passport_services'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('terms-and-conditions/', views.terms, name='terms'),
    path('refund-policy/', views.refund, name='refund'),
]
