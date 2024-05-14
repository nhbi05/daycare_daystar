from django.urls import path
from daystarapp import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', views.landing_page,name="landingpage"),
    path('register/', views.register,name="register"),
    path('index/', views.index,name="index"),
    path('login/', views.user_login,name="login"),
    path('logout/', views.user_logout,name="logout"),
    
    
    #baby_views
    path('baby/', views.baby,name="baby"),
    path('baby_reg/', views.addBaby,name="baby_reg"),
    path('<int:id>',views.view_baby, name='view_baby'),
    path('b_edit/<int:id>',views.babyedit, name='b_edit'),
    path ('baby_delete/<int:id>', views.delete_baby, name="baby_delete"),
    #sitter views
    path('sitter/', views.sitter,name="sitter"),
    path('sitter_reg/', views.addSitter,name="sitter_reg"),
    path('<int:id>', views.view_sitter,name="view_sitter"),
    path('s_edit/<int:id>', views.sitter_edit,name="s_edit"),
    path('sitter_delete/<int:id>', views.delete_sitter,name="sitter_delete"),
    
    #baby payment_views
    path('payments/', views.payment, name='payments'),
    path('payment_reg/', views.create_payment, name='payment_reg'),
    path('<int:id>', views.view_payment, name='view_payment'),
    path('payment_delete/<int:id>', views.payment_delete,name="payment_delete"),
    #sitter payments
    path('sitter_status/', views.sitter_payment, name='sitter_status'),
    path('s_paymentadd/', views.addSitter_status, name="s_paymentadd"),
    path('update_payment/<int:id>', views.payment_update, name='update_payment'),
    path('delete_payment/<int:id>', views.payment_delete, name='delete_payment'),
    #procuremnent
    path('procurementhome/', views.procurement_landingpage, name='procurementhome'),
    path('procurement/', views.procurement, name='procurement'),
    path('procurement_reg/', views.create_procurement, name='procurement_reg'),
    path('<int:id>', views.view_procurement, name='procurement_view'),
    path('procurement_edit/<int:id>', views.procurement_update, name='procurement_edit'),
    path('confirm_delete/<int:id>', views.procurement_delete,name="confirm_delete"),

    #dolls
    path('dolls/', views.all_dolls, name='dolls'),
    path('dolls/create/', views.create_doll, name='create_doll'),
    path('<int:id>/', views.view_doll, name='view_doll'),
    path('doll_update/<int:id>/', views.update_doll, name='doll_update'),
    path('doll_delete/<int:id>', views.delete_doll, name='doll_delete'),

    #doll_transactions
    path('transaction/new/', views.make_transaction, name='make_transaction'),
    path('transaction/<int:pk>/', views.transaction_detail, name='transaction_detail'),
    path('transactions/', views.transaction_list, name='transaction_list'),
]
