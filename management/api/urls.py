from django.urls import path
from management.api.views import *

app_name = 'management'



urlpatterns = [
    path('creat', creat_student, name='creat'),
    path('all', get_all_detail_student, name='detail'),
    path('<id>', get_detail_student, name='detail'),
    path('<id>/update', get_update_student, name='update'),
    path('<id>/delete', get_delete_student, name='delete'),
]