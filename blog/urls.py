from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,about, BlogAPI
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from .models import Post


urlpatterns = [
        path('',views.index,name = 'index'),
        path('business/',PostListView.as_view(), name = 'business'),
        path('register/',user_views.register, name = 'register'),
        path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
        path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
        path('profile/',user_views.profile,name='profile'),
        path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
        path('post/new/',PostCreateView.as_view(),name='post-create'),
        path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
        path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
        path('post/archive/',ArchiveIndexView.as_view(model = Post, date_field = "date_posted"), name = 'post_archive'),
        path('post/yeararchive/<int:year>/',YearArchiveView.as_view(queryset = Post.objects.all(), date_field = "date_posted",
              make_object_list = True, allow_future = True),name='post-year'),
        path('about/',about,name='about'),
	path('blogapi/',BlogAPI.as_view(), name = 'BlogAPI')
]
if settings.DEBUG:
    urlpatterns += static('media/',document_root=settings.MEDIA_ROOT)