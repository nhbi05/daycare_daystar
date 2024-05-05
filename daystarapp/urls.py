from django.urls import path
from daystarapp import views

urlpatterns=[
    path('', views.index,name="index"),
    path('baby/', views.baby,name="baby"),
    path('baby_reg/', views.addBaby,name="baby_reg"),
    path('<int:id>',views.view_baby, name='view_baby'),
    path('b_edit/<int:id>',views.babyedit, name='b_edit'),
    path ('delete/<int:id>', views.delete_baby, name="delete_baby"),
    path('sitter/', views.sitter,name="sitter"),
    path('sitter_reg/', views.addSitter,name="sitter_reg"),
    path('<int:id>', views.view_sitter,name="view_sitter"),
    path('s_edit/<int:id>', views.sitter_edit,name="s_edit"),
    path('delete/<int:id>', views.delete_sitter,name="delete_sitter"),
    path('create_payment/<int:baby_id>/<payment_type>/', views.create_payment, name='create_payment'),
    
]