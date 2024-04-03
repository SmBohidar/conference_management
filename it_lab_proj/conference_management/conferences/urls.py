from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('conferences/', views.conferences, name='conferences'),  # Corrected URL pattern
    path('create/', views.create_conference, name='create_conference'),
    path('conferences/', views.conferences, name='all_conferences'),  # Corrected URL pattern
    path('edit/<int:conference_id>/', views.edit_conference, name='edit_conference'),
    path('delete/<int:conference_id>/', views.delete_conference, name='delete_conference'),
    path('login/', views.login, name='login'),
    path('chair/login/', views.chair_login, name='chair_login'),
    path('user/login/', views.user_login, name='user_login'),
    path('reviewer/login/', views.reviewer_login, name='reviewer_login'),
    path('register/chair/', views.chair_registration, name='chair_registration'),
    path('register/reviewer/', views.reviewer_registration, name='reviewer_registration'),
    path('register/user/', views.user_registration, name='user_registration'),
    path('dashboard/user/',views.user_dashboard,name='user_dashboard'),
    path('dashboard/reviewer/',views.reviewer_dashboard,name='reviewer_dashboard'),
    path('add_research_paper/', views.add_research_paper, name='add_research_paper'),
    path('add_review/', views.add_review, name='add_review'),
    # Other URL patterns
]
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
