from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, ArchiveIndexView, \
    YearArchiveView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from .models import Post
from .forms import PostForm


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super().form_valid(form)
    
post_new = PostCreateView.as_view()


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    def form_vlaid(self, form):
        messages.success(self.request, '포스트를 수정했습니다.')
        return super().form_valid(form)


post_edit = PostUpdateView.as_view()


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('instagram:post_list')


post_delete = PostDeleteView.as_view()


@login_required
def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    messages.info(request, 'messages 테스트')
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q': q,
    })


class PostDetailView(DetailView):
    model = Post
    # queryset = Post.objects.filter(is_public=True)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs.filter(is_public=True)
        return qs

post_detail= PostDetailView.as_view()

post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=3)
post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at')