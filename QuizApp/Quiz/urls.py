from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='Log In'),
    path('sign_up/',views.sign_up,name="Sign Up"),
    path('quiz/',views.quiz,name="Quiz"),
    path('login_submission/',views.login_submission,name="login_form_submission"),
    path('signup_submission/',views.signup_submission,name="signup_form_submission"),
    path('score_submission/',views.score_submission,name="score_submission"),
]
