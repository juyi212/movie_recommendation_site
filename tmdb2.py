# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_pjt.settings')

# import django
# django.setup()

# import requests
# import json
# from collections import OrderedDict
# from movies.models import Genre, Movie


# apikey = '9518a3d444838dfc19bd751bcc3df303'



import requests
from urllib.parse import urlparse
import json

class URLMaker():
    
    url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=9518a3d444838dfc19bd751bcc3df303'


    # 기본 url 설정
    def get_url(self):
        return f'{self.url}&language=ko-KR'


def movieInfo():

    # 인스턴스 생성
    url_maker = URLMaker()
    
    # url 설정
    url = url_maker.get_url()
    # print(url)

    # 데이터 요청후 json파일로 변환
    movies_dict = requests.get(urlparse(url).geturl(),headers={'Authorization':'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMmQ3NWVjMjdlMWZjMGU3YjNjZjA3YmEwMmJjYjFkNSIsInN1YiI6IjVmYjcxMGVlZDNkMzg3MDA0MWQ2NjMyMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.6C2J2vrpLZS8_p2YPsppIbH04RpX3Mt3cqVOQhX2m1I','Content-Type':'application/json;charset=utf-8'})
    movies = movies_dict.json()
    return movies['genres']



if __name__=='__main__':
    movieData=[]

    x = movieInfo()
    data = {}
    data["model"] = "movies.genre"
    data['fields'] = x
    movieData.append(data)

        # for j in range(20):
        #     try:
        #         video_url = "https://api.themoviedb.org/3/movie/{}/videos?api_key=9518a3d444838dfc19bd751bcc3df303".format(j)
        #         video_i = requests.get(video_url)
        #         video_data = json.loads(video_i.text)
        #         if video_data['results'] and x[j]['backdrop_path']:
        #             video_id = video_data["results"][-1]["key"]
        #             data["fields"] = x[j]
        #             data['fields']['video'] =video_id
        #             movieData.append(data)
        #     except:
        #         pass

    with open('genre_info.json','w',encoding="utf-8") as make_file:
        json.dump(movieData,make_file,ensure_ascii=False,indent="\t")


