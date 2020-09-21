from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest, Http404
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostForm

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # messages.add_message(request, messages.SUCCESS, '새 글이 등록되었습니다')
            messages.success(request, '새 글이 등록되었습니다') # shortcut
            return redirect(post)
    else:
        form = PostForm()

    return render(request, 'instagram/post_form.html', {
        'form': form,
        'post': None,
    })

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        messages.error(request, '작성자만 수정이 가능합니다')
        return redirect(post)

    if request == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post)
    else:
        form = PostForm(instance=post)

    return render(request, 'instagram/post_form.html', {
        'form': form,
        'post': post
    })

# version 2
# @method_decorator(login_required, name='dispatch')
# class PostListView(ListView):
#     model = Post
#     paginate_by = 10


# version 3
# class PostListView(LoginRequiredMixin, ListView):
#     model = Post
#     paginate_by = 10

# post_list = PostListView.as_view()



# post_list = ListView.as_view(model=Post, paginate_by=5)
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


# def post_detail(request: HttpResponse, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#     return render(request, 'instagram/post_detail.html', {'post': post})

# post_detail = DetailView.as_view(
#     model=Post,
#     queryset=Post.objects.filter(is_public=True))


class PostDetailView(DetailView):
    model = Post
    # queryset = Post.objects.filter(is_public=True)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs.filter(is_public=True)
        return qs

post_detail= PostDetailView.as_view()

# def archives_year(request, year):
#     return HttpResponse(f"{year}년 archives")

post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=3)
post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at')