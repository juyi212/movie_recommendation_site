# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_pjt.settings')

# import django
# django.setup()

# import requests
# import json
from collections import OrderedDict
# from movies.models import Genre, Movie



# class URLMaker():

#     url = 'https://api.themoviedb.org/3/movie/'
#     # url = 'https://api.themoviedb.org/3/movie/popular?api_key=9518a3d444838dfc19bd751bcc3df303'

#     # page 설정
#     def __init__(self,page):
#         self.page = page

#     # 기본 url 설정
#     def get_url(self):
#         return f'{self.url}{self.page}?api_key=9518a3d444838dfc19bd751bcc3df303&language=ko-KR'
# # {self.query}


# def movieInfo(query):

#     # 인스턴스 생성
#     url_maker = URLMaker(query)
    
#     # url 설정
#     url = url_maker.get_url()
#     # print(url)

#     # 데이터 요청후 json파일로 변환
#     movies_dict = requests.get(urlparse(url).geturl(),headers={'Authorization':'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMmQ3NWVjMjdlMWZjMGU3YjNjZjA3YmEwMmJjYjFkNSIsInN1YiI6IjVmYjcxMGVlZDNkMzg3MDA0MWQ2NjMyMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.6C2J2vrpLZS8_p2YPsppIbH04RpX3Mt3cqVOQhX2m1I','Content-Type':'application/json;charset=utf-8'})
#     movies = movies_dict.json()
#     return movies['results']



# if __name__=='__main__':
#     movieData = []
    

#     for i in range(0,10):
#         x = movieInfo(i)
#         for j in range(20):
#             data = {}
#             try:
#                 video_url = "https://api.themoviedb.org/3/movie/{}/videos?api_key=9518a3d444838dfc19bd751bcc3df303".format(j)
#                 video_i = requests.get(video_url)
#                 video_data = json.loads(video_i.text)
#                 video_id = video_data["results"][-1]["key"]

#                 if video_id and x[j]['backdrop_path'] and x[j]['release_date']:
#                     data["model"] = "movies.movie"
#                     data["fields"] = x[j]
#                     data['fields']['video'] =video_id
#                     movieData.append(data)
#             except:
#                 pass

#     with open('moviess.json','w',encoding="utf-8") as make_file:
#         json.dump(movieData,make_file,ensure_ascii=False,indent="\t")


# lang = 'ko-KR'
# page = 1
# region = 'KR'

# genre_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={apikey}&language={lang}'
# genre_response = requests.get(genre_url).json().get('genres')


# for name in genre_response:
#     genre = Genre()
#     genre.id = name['id']
#     genre.name = name['name']
#     genre.save()

apikey = '9518a3d444838dfc19bd751bcc3df303'

import requests
from urllib.parse import urlparse
import json



movie_list = range(100, 500)
movielist=[]

for n in movie_list:
    try:
        file_data = OrderedDict()
        url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=ko-kr".format(n,apikey)
        r = requests.get(url)
        data = json.loads(r.text)


        video_url = "https://api.themoviedb.org/3/movie/{}/videos?api_key={}".format(n, apikey)
        video_i = requests.get(video_url)
        video_data = json.loads(video_i.text)
        video_id = video_data["results"][-1]["key"]


        file_d ={}
        file_data["model"] = "movies.movie"
        if len(data["overview"]) > 10 and data["poster_path"] and data["release_date"]:
            file_d["title"] = data["title"]
            file_d["genres"] = []

            for genre in data["genres"]:
                file_d["genres"].append(genre['id'])

            file_d['popularity'] =  data['popularity']
            file_d["original_title"] = data["original_title"]
            file_d["original_language"] = data["original_language"]
            file_d["overview"] = data["overview"]
            file_d["adult"] = data["adult"]
            file_d['vote_count'] = data['vote_count']
            file_d["poster_path"] = data["poster_path"]
            file_d["release_date"] = data["release_date"]
            file_d["vote_average"] = data["vote_average"]           
            file_d["video"] = video_id
            file_data['fields'] = file_d
            movielist.append(file_data)
    except:
        pass

    with open('moviess.json','w',encoding="utf-8") as make_file:
        json.dump(movielist,make_file,ensure_ascii=False,indent="\t")
