from django.shortcuts import render,get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Movie, Review, Genre
from .forms import ReviewForm
from django.db.models import Q
from .genre_info import GENRE
import datetime


def first(request):
    movies = Movie.objects.order_by('-pk')
    movies_audience = Movie.objects.order_by('-popularity')
    movies_rank = Movie.objects.order_by('-vote_average')
    movies_release_date = Movie.objects.order_by('-release_date')
    context = {
        'movies': movies,
        'movies_audience': movies_audience,
        'movies_rank': movies_rank,
        'movies_release_date': movies_release_date,
    }
    return render(request, 'movies/first.html', context)



def movie_list (request):
    movies = Movie.objects.order_by('-pk')
    genre_date = request.GET.getlist('genre_list')
    pick_date = request.GET.getlist('date_list')

    if genre_date:
        for ge in GENRE:
            if ge['name'] == genre_date[0]:
                genre_i = ge['id']
        movies = movies.filter(genres__icontains=genre_i)


    if pick_date:
        p_date = pick_date[0]
        if p_date == '80-90년대':
            movies = movies.filter(release_date__lte=datetime.date(1999, 12, 31))
        elif p_date == '2000년대':
            movies = movies.filter(release_date__gte=datetime.date(2000, 1, 1)).filter(release_date__lte=datetime.date(2009, 12, 31))
        elif p_date == '2010년대 이후':
            movies = movies.filter(release_date__gte=datetime.date(2009, 12, 31))
    
    genres = []
    for gn in GENRE:
        genres.append(gn['name'])



    dates = ['80-90년대','2000년대', '2010년대 이후']
    context = {
        'movies': movies,
        'genres': genres,
        'dates': dates,
    }
    return render(request, 'movies/index.html', context)


def movie_mbti(request):

    return render(request, 'movies/movie_mbti.html')


@require_GET
def movie_mbti_search(request):
    movies = Movie.objects.order_by('-pk')
    make_mbti = []
    first = request.GET.get('first_value')
    second = request.GET.get('second_value')
    third = request.GET.get('third_value')
    fourth = request.GET.get('fourth_value')
    make_mbti.append(first)
    make_mbti.append(second)
    make_mbti.append(third)
    make_mbti.append(fourth)
    
#  User.objects.filter(Q(first_name__startswith='R')|Q(last_name__startswith='D'))

    if make_mbti == ['짬뽕','찍먹','비냉','밀떡'] :
        movies = movies.filter(Q(genres__icontains=12) | Q (genres__icontains=14))
        ment = '당신은 주정부리식 ISTJ 소금형 사람입니다.'

    elif make_mbti == ['짬뽕','찍먹','물냉','밀떡']:
        movies = movies.exclude(genres__icontains =14)
        ment = '당신은 주정부리식 ESTJ 사업가형 사람입니다.'

    elif make_mbti == ['짜장','부먹','물냉','쌀떡']:
        movies = movies.filter(Q(genres__icontains=37) | Q (genres__icontains=36))
        ment = '당신은 주정부리식 ISFJ 권력형 사람입니다.'

    elif make_mbti == ['짬뽕','부먹','물냉','밀떡']:
        movies = movies.filter(Q(genres__icontains=27) | Q (genres__icontains=53))
        ment = '당신은 주정부리식 ENFP 스파크형 사람입니다.'
    
    elif make_mbti == ['짜장','부먹','물냉','밀떡']:
        movies =  movies.filter(Q(genres__icontains=10751) | Q (genres__icontains=18) | Q(popularity__gte=52))
        ment = '당신은 주정부리식 ESFJ 친선도모형 사람입니다.'

    elif make_mbti == ['짜장','찍먹','물냉','쌀떡']:
        movies = movies.filter(Q(genres__icontains=10402) | Q (genres__icontains=99))
        ment = '당신은 주정부리식 INFP 잔다르크형 사람입니다.'

    elif make_mbti == ['짬뽕','부먹','비냉','쌀떡']:
        movies = movies.filter(Q(genres__icontains=10751) | Q (genres__icontains=10749))
        ment = '당신은 주정부리식 ISFP 성인군자형 사람입니다.'

    elif make_mbti == ['짜장','부먹','비냉','쌀떡']:
        movies = movies.filter(Q(genres__icontains=878))
        ment = '당신은 주정부리식 INTJ 과학자형 사람입니다.'

    elif make_mbti == ['짬뽕','찍먹','물냉','쌀떡']:
        movies = movies.filter(Q(popularity__gte=52)| Q(vote_average__gte=7.0))
        ment = '당신은 주정부리식 ESFP 사교형 사람입니다.'

    elif make_mbti == ['짜장','부먹','비냉','밀떡']:
        movies = movies.filter(Q(genres__icontains=9648)| Q(vote_average__gte=7.0))
        ment = '당신은 주정부리식 ISTP 백과사전형 사람입니다.'

    elif make_mbti == ['짬뽕','부먹','비냉','밀떡']:
        movies = movies.filter(Q(popularity__gte=52)| Q(release_date__lte=datetime.date(1999, 12, 31)))
        ment = '당신은 주정부리식 ISTP 백과사전형 사람입니다.'

    elif make_mbti == ['짜장','찍먹','물냉','밀떡']:
        movies = movies.all()
        ment = '당신은 주정부리식 ESTP 활동가형 사람입니다.'

    elif make_mbti == ['짜장','찍먹','비냉','밀떡']:
        movies = movies.filter(Q(genres__icontains=28)| Q(genres__icontains=10752))
        ment = '당신은 주정부리식 INTP 아이디어형 사람입니다.'

    elif make_mbti == ['짬뽕','부먹','물냉','쌀떡']:
        movies = movies.filter(Q(genres__icontains=28)| Q(genres__icontains=14))
        ment = '당신은 주정부리식 ENTJ 지도자형 사람입니다.'

    elif make_mbti == ['짬뽕','찍먹','비냉','쌀떡']:
        movies = movies.filter(Q(genres__icontains=14)| Q(genres__icontains=878))
        ment = '당신은 주정부리식 ENTP 발명가형 사람입니다.'

    elif make_mbti == ['짜장','찍먹','비냉','쌀떡']:
        movies = movies.filter(Q(genres__icontains=10752)| Q(genres__icontains=35))
        ment = '당신은 주정부리식 ENFJ 언변능숙형 사람입니다.'
    
    context = {
        'movies': movies,
        'ment': ment
    }
    return render(request, 'movies/index.html', context)






def movie_search(request):
    search_movies=None
    query=None

    if 'q' in request.GET:
        query =request.GET.get('q')
        movies = Movie.objects.all().filter(Q(title__contains=query) | Q(overview__contains=query))
    return render(request, 'movies/index.html', {'query':query, 'movies': movies})






def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genre_name = []


    for gen in GENRE:
        if str(gen['id']) in movie.genres:
            genre_name.append(gen['name'])

    reviews = movie.review_set.all()
    review_form = ReviewForm()
    N=range(5)
    context= {
        'genre_name': genre_name,
        'movie': movie,
        'review_form': review_form,
        'reviews' : reviews,
        'video': 'https://www.youtube.com/embed/' + movie.video,
        'N': N,
    }
    return render(request, 'movies/detail.html', context)



@require_POST
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.movie = movie
        review.user = request.user
        review.save()
        return redirect('movies:movie_detail', movie.pk)
    context = {
        'review_form': review_form,
        'movie': movie,
        'reviews': movie.review_set.all(),
    }
    return render(request, 'movies/detail.html', context)



@require_POST
def reviews_delete(request, movie_pk, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if request.user == review.user:
            review.delete()
    return redirect('movies:movie_detail', movie_pk)



@require_POST
def like(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        if movie.like_users.filter(pk=user.pk).exists():
        # if user in article.like_users.all():
            movie.like_users.remove(user)
            liked = False
        else:
            movie.like_users.add(user)
            liked = True

        like_status = {
            'liked': liked,
            'count': movie.like_users.count(),
        }
        print(like_status)
        return JsonResponse(like_status)
        # return redirect('articles:index')
    return redirect('accounts:login')


