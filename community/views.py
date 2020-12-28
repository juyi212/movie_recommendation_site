from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required


def index_search(request):
    qs = Post.objects.all().order_by('-id')

    q = request.GET.get('q', '')
    if q: 
        qs = qs.filter(title__icontains=q)
    paginator = Paginator(qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'articles' : qs,
        'q' : q,
        'page_obj' : page_obj,
    }

    return render(request, 'community/index.html', context)


def pur_index(request, article_pk):
    if int(article_pk) > 3:
        return redirect('community:index')
    articles = Article.objects.filter(purpose=article_pk).order_by('-id')
    paginator = Paginator(articles, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'articles': articles,
        'page_obj': page_obj,
        'article_pk': article_pk,
    }
    return render(request, 'community/index.html', context)


@require_GET
def index(request):
    articles = Article.objects.order_by('-pk')
    paginator = Paginator(articles, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'articles': articles,
        'page_obj': page_obj,
    }

    return render(request, 'community/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) 
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('community:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)

@require_GET
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if request.user == article.user:
            article.delete()
            return redirect('community:index')
    return redirect('community:detail', article.pk)


@require_POST
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('community:detail', article.pk)
    context = {
        'comment_form': comment_form,
        'article': article,
        'comments': article.comment_set.all(),
    }
    return render(request, 'community/detail.html', context)



@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('community:detail', article_pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, article_pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=article_pk)
    # 수정하는 유저와, 게시글 작성 유저가 같은지 ?
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('community:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('community:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'community/update.html', context)


