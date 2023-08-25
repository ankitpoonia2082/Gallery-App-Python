from django.urls import path
from .import views
# from django.conf import settings
# from django.conf.static import static 

urlpatterns = [
    path('',views.Home_View.as_view(), name='home'),
    path('register/',views.Register_View.as_view(), name='register'),
    path('gallery/',views.GalleryView.as_view(), name='gallery'),
    path('logout/',views.SignOut_View, name='logout'),
    path('cat/<int:id>/',views.Cat_View.as_view(), name='cat'),
    path('addimages',views.addimage_view.as_view(), name='addimages'),
    path('myuploads',views.MyUpload_View.as_view(), name='myuploads'),
    path('viewinfo/<int:id>/',views.View_Info.as_view(), name='viewinfo')
]

