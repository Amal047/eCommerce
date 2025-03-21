from django.urls import path
from admindash import views


app_name='admindash'

urlpatterns = [
    
    path('dashboard',views.dashboard,name='dashboard'),
    path('admin_products_list',views.admin_products_list,name='admin_products_list'),
    path('admin_products_details/<str:pid>/',views.admin_products_details,name='admin_products_details'),
    path('block_unblock_products/<str:pid>/',views.block_unblock_products,name='block_unblock_products'),
    path('admin_add_product/',views.add_product,name='admin_add_product'),
    path('admin_delete_product/<str:pid>',views.delete_product,name='admin_delete_product'),
    path('admin_category_list',views.admin_category_list,name='admin_category_list'),
    path('admin_add_category',views.admin_add_category,name='admin_add_category'),
    path('admin_category_edit/<str:cid>/',views.admin_category_edit,name='admin_category_edit'),
    
    path('admin_delete_category/<str:cid>/',views.delete_category,name='admin_delete_category'),
    path('block_unblock_category/<str:cid>/',views.available_category,name='block_unblock_category'),
    
    
     path('order-list/',views.order_list,name='order-list'),
     
     path('admin-order-detail/<int:id>',views.admin_order_detail,name='admin-order-detail'),
     
     path('admin-cancel-order/<int:id>',views.admin_cancel_order,name='admin-cancel-order'),
     
    #  coupon
    path('admin-coupon/',views.admin_coupon, name='admin-coupon'),
    
    path('create-coupon/',views.create_coupon, name='create-coupon'),
    
    path('edit-coupon/<int:id>/',views.edit_coupon, name='edit-coupon'),
    
    path('delete-coupon/<int:id>/',views.delete_coupon, name='delete-coupon'),
    
    path('update-product-status/<int:id>/', views.update_product_status, name='update-product-status'),
    
    # offers for product
    
    
    path('product-offers/',views.product_offers, name='product-offers'),
    
    path('edit-product-offers/<int:id>',views.edit_product_offers, name='edit-product-offers'),
     
    path('create-product-offer/',views.create_product_offer, name='create-product-offer'),
     
    path('delete-product-offer/<int:id>/',views.delete_product_offer, name='delete-product-offer'),
    
    
    # category offers
    
    path('category-offers/',views.category_offers, name='category-offers'),
    
    path('edit-category-offers/<int:id>',views.edit_category_offers, name='edit-category-offers'),
    
    path('create-category-offer/',views.create_category_offer, name='create-category-offer'),
    
    path('delete-category-offer/<int:id>/',views.delete_category_offer, name='delete-category-offer'),
    
    path('sales_report',views.sales_report,name='sales_report')
     
]