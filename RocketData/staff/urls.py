from django.urls import path
from .views import StaffView, Filter_B, Filter_C, Filter_D, Filter_E

app_name = "staff"

urlpatterns = [
    path('staff/', StaffView.as_view()),
    path('position_B/', Filter_B.as_view()),
    path('position_C/', Filter_C.as_view()),
    path('position_D/', Filter_D.as_view()),
    path('position_E/', Filter_E.as_view()),
]

