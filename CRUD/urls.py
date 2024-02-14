from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.BlogCreateView.as_view(),name='blog.create'),
    path('',views.BlogListView.as_view(),name="blogs.list"),
    path('blogs/<int:pk>/update/',views.BlogUpdateView.as_view(),name="blogs.update"),
    path('blogs/<int:pk>/delete/',views.BlogDeleteView.as_view(),name="blogs.delete"),
    path('blogs/<int:pk>/detail/',views.BlogDetailView.as_view(),name="blogs.detail")
]
