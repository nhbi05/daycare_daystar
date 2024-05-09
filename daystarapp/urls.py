from django.urls import path
from daystarapp import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', views.landing_page,name="landingpage"),
    path('register/', views.register,name="register"),
    path('login/', views.login,name="login"),
    path('index/', views.index,name="index"),
    path('logout/', views.user_logout,name="logout"),
    #baby_views
    path('baby/', views.baby,name="baby"),
    path('baby_reg/', views.addBaby,name="baby_reg"),
    path('<int:id>',views.view_baby, name='view_baby'),
    path('b_edit/<int:id>',views.babyedit, name='b_edit'),
    path ('delete/<int:id>', views.delete_baby, name="delete_baby"),
    #sitter views
    path('sitter/', views.sitter,name="sitter"),
    path('sitter_reg/', views.addSitter,name="sitter_reg"),
    path('<int:id>', views.view_sitter,name="view_sitter"),
    path('s_edit/<int:id>', views.sitter_edit,name="s_edit"),
    path('delete/<int:id>', views.delete_sitter,name="delete_sitter"),
    
    #payment_views
    path('payments/', views.payment, name='payments'),
    path('payment_reg/', views.create_payment, name='payment_reg'),
    path('<int:id>', views.view_payment, name='view_payment'),
    #path('create_payment/<int:id>', views.create_payment, name='create_payment'),
    path('update_payment/<int:id>', views.payment_update, name='update_payment'),
    path('delete_payment/<int:id>', views.payment_delete, name='delete_payment'),
    path('login/',auth_views.LoginView.as_view(template_name="mydaystarapp/login.html"),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name="daystarapp/logout.html"),name="logout"),
    
]
