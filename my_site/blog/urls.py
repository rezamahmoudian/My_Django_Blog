from django.urls import path, include
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.homeView, name='home'),
    path('<int:page_number>', views.homeView, name='home'),
    path('about', views.aboutView, name='about'),
    path('contact', views.contactView, name='contact'),
    path('post/<slug:slug>', views.postView, name='post'),
    path('category/<slug:slug>',views.CategoryListView.as_view(), name='category'),
    path('category/<slug:slug>/<int:page>', views.CategoryListView.as_view(), name='category'),
    path('author/<slug:username>',views.AuthorListView.as_view(), name='author'),
    path('author/<slug:username>/<int:page>', views.AuthorListView.as_view(), name='author'),
    path('preview-post/<int:pk>', views.PreviewPostView.as_view() , name='preview-post'),
]