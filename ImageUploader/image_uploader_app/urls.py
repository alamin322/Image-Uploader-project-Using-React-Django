from image_uploader_app import views
from django.urls import path

app_name = 'api'

urlpatterns = [
    path(route="list/", view=views.ImageList.as_view(), name="listview"),
    path(route='create/', view=views.ImageCreate.as_view(), name='createview'),
    path(route='read/<int:pk>', view=views.ImageRetrieve.as_view(), name='readview'),
    path(route='update/<int:id>', view=views.ImageUpdate.as_view(), name='updateview'),
    path(route='delete/<int:id>', view=views.ImageDestroy.as_view(), name='deleteview'),
]