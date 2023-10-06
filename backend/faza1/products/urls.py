from django.urls import path

from .views import (
    ProductListCV,
    ProductDetailCV,
    ProductRUDCV,
    ProductCRCV,
    CategoryListCV,
    BrandListCV,
    OneCategoryListCV,
    OneBrandListCV,
    ProductFilterCV,
    ProductSearchCV,
    # ReviewCV,
    AddToCartAV,
    
     )


urlpatterns = [
    path('',ProductListCV.as_view()),
    path('filter/',ProductFilterCV.as_view()), #http://127.0.0.1:8000/products/?low=200&high=1000
    path('search/',ProductSearchCV.as_view()),
    path('categories/',CategoryListCV.as_view()),
    path('additems/',AddToCartAV.as_view()),
    path('categories/<slug:slug>/',OneCategoryListCV.as_view()),
    path('brands/',BrandListCV.as_view()),
    path('brands/<slug:slug>/',OneBrandListCV.as_view()),
    path('admin/',ProductCRCV.as_view()),
    path('admin/<slug:slug>/',ProductRUDCV.as_view()),
    path('<slug:slug>/',ProductDetailCV.as_view()),
    # path('<slug:slug>/review',ReviewCV.as_view()),
]
    
    
    
    
    
    
 
    
  
