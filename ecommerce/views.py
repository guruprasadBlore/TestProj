from .models import post
from django.db.models import Q
from django.http import HttpResponse
from .forms import LoginForm,PostForm
from comments.forms import CommentForm
from comments.models import Comments
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from pagination import MyCustomPagination,CustomPagePaginator

# from django.urls import reverse_lazy
from django.core.urlresolvers import reverse_lazy
from ecommerce.api.MySerializer import PostSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required
#############################################################
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from django.core import serializers
import json

import pdb
# Create your views here.

#######################Class Based Views#######################
class PostListView(ListView):
    queryset = post.objects.all()
    template_name = 'cbv.html'

class PostDetailView(DetailView):
    model = post
    template_name = "cbvdetail.html"

class PostCreateView(CreateView):
    # pdb.set_trace()
    queryset = post.objects.all()
    template_name = 'post_form.html'
    form_class = PostForm

class PostUpdateView(UpdateView):
    queryset = post.objects.all()
    template_name = 'post_form.html'
    form_class = PostForm

    def get_object(self):
        slug = self.kwargs['slug']
        return get_object_or_404(post,slug=slug)

class PostDeleteView(DeleteView):
    template_name = 'post_form.html'
    success_url = reverse_lazy('cbv')
    def get_object(self):
        slug = self.kwargs['slug']
        return get_object_or_404(post, slug=slug)

##########################################################################



def welcome(request):
    msg = "WelCome!!!!"
    form  = LoginForm(request.POST)
    next = ""
    if request.GET:
        next = request.GET["next"]
    if request.method == 'POST':
      if form.is_valid():
        username = form.cleaned_data.get("Userid")
        password = form.cleaned_data.get('Password')
        user = authenticate(username=username, password=password)
        login(request, user)
        #pdb.set_trace()
        if next == "":
            #return redirect(request.META.get( 'HTTP_REFERER' ))
            return redirect('/')
        else:
            return redirect( next )
            #return redirect(request.META.get( 'HTTP_REFERER' ))
    else:
        form = LoginForm()
    return render(request,'welcome.html',{ 'form':form,'next':next })

@login_required( login_url='/login/' )
def post_create(request):
    #pdb.set_trace()O
    form = PostForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return  HttpResponse("Post Created Successfully")
    return render(request,'post_form.html',{'form':form})

def post_list(request):
    #instance = get_object_or_404(post)
    # pdb.set_trace()
    if not request.is_ajax():
        query_set = post.objects.all()
        query = request.GET.get('q')
        if query:
            query_set = query_set.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)
            ).distinct()
        paginator = Paginator(query_set,2)
        page_request_var = "page"
        page = request.GET.get(page_request_var)
        try:
            query_set = paginator.page(page)
        except PageNotAnInteger:
            #pdb.set_trace()
            query_set = paginator.page(1)
        except EmptyPage:
            query_set = paginator.page(paginator.num_pages)

        context = {'result':query_set,"page_request_var": page_request_var}
        return render(request,'post_list.html',context )
    else:
        query_set = post.objects.all()
        query = request.GET.get('q')
        if query:
            query_set = query_set.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        # paginator = Paginator(query_set, 2)
        # page_request_var = "page"
        # page = request.GET.get(page_request_var)
        # try:
        #     query_set = paginator.page(page)
        # except PageNotAnInteger:
        #     # pdb.set_trace()
        #     query_set = paginator.page(1)
        # except EmptyPage:
        #     query_set = paginator.page(paginator.num_pages)

        # context = {'result': query_set, "page_request_var": page_request_var}
        qs_json = serializers.serialize('json', query_set)
        # qs_json = []
        # for blog in query_set:
        #     qs_json.append({'Name':blog.title,'Content':blog.content})
        #     qs_json = json.dumps(qs_json)
        return HttpResponse(qs_json, content_type='application/json')


def post_detail( request, slug ):
    #pdb.set_trace()
    instance = get_object_or_404( post, slug=slug )
    #form = CommentForm(request.POST or None)
    if request.method == 'POST':
        comments_data = request.POST[ 'comments' ]
        new_comment,created = Comments.objects.get_or_create(
            user = request.user,
            content = comments_data,
            post = instance )

    context = {
        "title": instance.title,
        "instance": instance,

        #"comments":ur_comments,
    }
    # print instance.comments.get(id=1)
    response = render(request, 'post_detail.html', context)
    #visits = int(request.COOKIES.get('visits', '0'))
    #response.set_cookie('visits', visits + 1)
    visits = request.session.get('visits', 0)
    request.session['visits'] = visits + 1
    return response

@permission_required("ecommerce.Can_Modify")
#@login_required(login_url='/login/')
def post_update( request, slug=None ):
    newpost = get_object_or_404( post, slug=slug )
    form = PostForm( request.POST or None, instance=newpost )
    if form.is_valid():
        form.save()
        return redirect(newpost.get_absolute_url())
    context = {'title':newpost.title,
               'instance':newpost,
               'form':form}
    return render(request,'post_form.html',context)

def logout_view(request):
    logout(request)
    return redirect('/')

def post_delete(request,slug=None):
    pass

@csrf_exempt
@api_view(['GET','POST'])
def post_api_view(request):
    pdb.set_trace()
    if request.method == 'GET':
        qs = post.objects.all()
        slzr = PostSerializer(qs,many=True)

        return Response(slzr.data)
    else:
        pdb.set_trace()
        if request.method == 'POST':
            slzr = PostSerializer(data=request.data)
            if slzr.is_valid():
                slzr.save()
                return Response(slzr.data,status=status.HTTP_201_CREATED)
            return Response(slzr.errors,status=status.HTTP_400_BAD_REQUEST)






