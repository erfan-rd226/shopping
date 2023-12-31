from django.urls import path , include

from rest_framework.routers import DefaultRouter 
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views


router = DefaultRouter()
router.register('categories',views.CategoryViewSetApi)
router.register('products',views.ProductViewSetApi)


schema_view = get_schema_view(
   openapi.Info(
      title="shopping",
      default_version='v1.0.0',
      description="this is about shopping",
      contact=openapi.Contact(email="erfanrajabzade7278@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticated,),
   authentication_classes=(JWTAuthentication,),
)


urlpatterns = [

    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
] 
