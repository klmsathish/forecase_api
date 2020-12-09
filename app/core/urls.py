from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('create/', views.signup.as_view(), name='create'),
    path('user/<str:username>',views.UserViewSet.as_view({'get': 'list'})),
    # path('post/',views.PostViewSet.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('tag/<str:username>/', views.TagView.as_view(), name='tag')
    # path('tag/<username>/', views.UserViewSet.as_view(), name='room'),

    
]
