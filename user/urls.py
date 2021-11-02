from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('signup', signup, name='signup'),
    path('loginProcess', loginProcess, name='loginProcess'),
    path('logoutProcess', logoutProcess, name='logoutProcess'),
    path('dashboard', dashboard, name='dashboard'),
    path('updatepassword', updatepassword, name='updatepassword'),
    path('forgetpassword', forgetpassword, name='forgetpassword'),
    path('confirmforgotPassword/<uidb64>/<token>/',confirmforgotPassword,name="confirmforgotPassword"),
    path('confirmforgotPasswordForm',confirmforgotPasswordForm,name="confirmforgotPasswordForm"),
    path('btc_data/',get_latest_btc),
    path('eth_data/',get_latest_eth),
    path('iot_data/',get_latest_iot),
    path('rep_data/',get_latest_rep),
    path('bts_data/',get_latest_bts),
    path('dash_data/',get_latest_dash),
    path('eur_data/',get_latest_eur),
    path('ltc_data/',get_latest_ltc),
    path('xmr_data/',get_latest_xmr),
    path('neo_data/',get_latest_neo),
    path('all_data/<str:crypto>',crypto_all_data),
    path('history/<str:crypto>',crypto_history),
    path('history_data/<str:crypto>',crypto_history_data),
    path('avg_price/<str:crypto>',average_price),
    path('demo', demo, name='demo'),
  
]