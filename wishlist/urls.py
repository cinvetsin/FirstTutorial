from django.urls import path
from wishlist.views import register, login_user, logout_user, show_wishlist, send_wishlist_xml, send_wishlist_json, show_json_by_id, show_xml_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', send_wishlist_xml, name='send_wishlist_xml'),
    path('json/', send_wishlist_json, name='send_wishlist_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]