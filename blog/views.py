from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.dates import YearArchiveView	
from .serializers import PostSerializers
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

def index(request):
    return render(request,'blog/index.html')

posts =[{'author': 'Loonycorn',
         'title' : 'Blog Post 1',
         'content' : 'First post content',
         'date_posted' : 'Oct 25,2019'
        },
        {'author': 'Loonycorn2',
         'title' : 'Blog Post 2',
         'content' : 'First post content2',
         'date_posted' : 'Nov 25,2019'
        }]

def business(request):
    context = {'posts': Post.objects.all()}
    return render(request,'blog/business.html',context)

class PostListView(ListView):
      model = Post
      template_name = 'blog/business.html'
      context_object_name = 'posts'
      ordering = ['-date_posted']

class PostDetailView(DetailView):
      model = Post

class PostCreateView(CreateView):
      model = Post
      fields = ['title','content']
      def form_valid(self,form):
          form.instance.author = self.request.user
          return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin,UpdateView):
      model = Post
      fields = ['title','content']
      def form_valid(self,form):
          form.instance.author = self.request.user
          return super().form_valid(form)
      def test_func(self):
          post = self.get_object()
          if(post.author == self.request.user):
             return True
          else:
             return False



class PostDeleteView(UserPassesTestMixin,DeleteView):
      model = Post
      success_url = '/blog/business/'
     
      def test_func(self):
          post = self.get_object()
          if(post.author == self.request.user):
             return True
          else:
             return False

def about(request):
    return render(request,'blog/about.html')

class BlogAPI(APIView):
	def get(self, request):
		posts = Post.objects.all()
		serialize = PostSerializers(posts, many = True)
		return Response(serialize.data)
