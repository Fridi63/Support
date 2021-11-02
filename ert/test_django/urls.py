from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
# from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from main.views import CreateUserView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-token-auth/', views.obtain_auth_token),
    path("api/create/", CreateUserView.as_view()),
    path('main/', include('main.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    # path('api/token/verify/', TokenVerifyView.as_view()),

]
