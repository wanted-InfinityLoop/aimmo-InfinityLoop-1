# 🎊 Wanted X Wecode PreOnBoarding Backend Course | 무한루프-1팀
원티드 1주차 기업 과제 : Aimmo Assignment Project
  ✅ Aimmo 기업 과제입니다.

<br>

# 목차
- ### Project Build & Skills 
- ### How To Implement
- ### How To Execute
- ### API Using Swagger 
- ### 서버 배포

<br>


# ⚒️ Project Build

### Build(AWS EC2)
API Base URL : http://3.36.105.251:8000
API Document URL : http://3.36.105.251:8000/swagger/ (현재 접속시 에러가 나는 현상이 있음)

### Required
- Python3.7🔺
- Django (version 기입)🔺
- MongoDB (version 기입)🔺

### Add setting file
- Project폴더 안에 my_settings.py 파일 생성 후 내용 추가
- **`my_settings.py`** data structure
```py
MY_SECRET_KEY = "<SECRET_KEY>"
MY_DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "<DB NAME>",
        "CLIENT": {
            "host": "mongodb+srv://<username>:<password>@orange.nfaum.mongodb.net/<YourDatabase>?retryWrites=true&w=majority",
            "port": 27017,
            "username": "<username>",
            "password": "<password>",
            "authSource": "admin",
            "authMechanism": "SCRAM-SHA-1",
        },
    }
}
```

### Commnads
```shell
python manage.py makemigration
python manage.py migrate
python manage.py runserver
```

<br>

### Directory
```
.
├── CONVENTION.md
├── PULL_REQUEST_TEMPLATE.md
├── README.md
├── config
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── utils.py
│   └── views.py
├── manage.py
├── my_settings.py
├── postings
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializer.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
└── users
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializer.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

# 🔖 Skills

### Backend
- Python3
- Djagno
- Django ORM

### Devops
- MongoDB
- AWS(EC2)

### Cowork
- Git, Github Project
- Swagger2.0 (For API Document)
- Slack
- Google Meeting

<br>


# 🧑‍🎨 How To Implement 

- DB에 미리 게시글 카테고리에 대한 데이터를 넣어 글 작성시 카테고리를 선택해 작성할 수 있도록 구현하였습니다.     
  ↪️ 글 작성과 동시에 카테고리가 추가되면 태그의 기능이 강해보여 카테고리에 대한 모델을 만들어 데이터를 추가해주었습니다.   

<br>

- Q객체와 __ icontains키워드를 사용해 카테고리, 작성자, 제목을 기준으로 검색기능을 구현하였습니다.     
   ↪️ 유저가 검색옵션과 검색할 데이터를 입력해 요청하면 해당 데이터가 포함되어 있는 글을 LimitOffsetPagination으로 페이징 처리해주었습니다.  

<br>

- Posting model에 특정 글을 읽은 유저를 ManyToMany를 이용해 add했습니다. 글을 처음 읽는 유저라면 hits라는 값을 1증가시킨후 add해주었습니다.     
   ↪️ 글을 읽은 유저를 기억할 수 있는 방법 중 ManyToMany를 선택했습니다. 이후 refactoring을 통해 더 나은 방법을 고려하고 있습니다[(wiki)


<br>

- REST API를 작성하며 집중한 부분은 다음과 같습니다. 아래와 같은 조건을 고려하여 __post메소드 요청으로 게시글 작성하기__, __get메소드 요청으로 게시글을 불러오기__ , __put메소드 요청으로 게시글 수정하기__ , __delete메소드 요청으로 게시글 삭제하기__ 로 설계했습니다.
```  
기능에 맞는 HTTP메소드 선택
가독성 있는 URL네이밍을 위한 규칙
적절한 HTTP 상태코드와 헤더 
```

<br>

- 코드에 대한 버그가 있는지 없는지 체크하기 위한 유닛 테스트를 만들어 문제를 쉽게 해결할 수 있도록 노력했습니다. unit test 구현후 어느 부분에 문제가 있으며 어디를 고쳐야 할지 명확하게 알 수 있었기에 개발 중 미리 문제를 파악하는데 도움이 되었습니다.


<br>

# ⏯️ How To Execute

> Sign Up

**Request**
![스크린샷 2021-11-03 오전 6 38 23](https://user-images.githubusercontent.com/42742076/139955395-f6977354-8f9c-418c-bbae-c8a0a4089127.png)


1. 유저가 입력한 데이터 요청이 서버에 전송된다

2. 데이터를 받은 서버는 데이터에 대한 유효성 검증 후 잘못된 형식의 타입 요청이 들어올 경우 에러를 반환한다


3. 정상적인 데이터의 경우 DB에 유저를 create한다   

**Response**
![스크린샷 2021-11-03 오전 6 39 04](https://user-images.githubusercontent.com/42742076/139955468-491823c9-9a59-4e63-9bc3-487c5aa17e55.png)

<br>

> Sign in

**Request**
![스크린샷 2021-11-03 오전 6 40 35](https://user-images.githubusercontent.com/42742076/139955640-adadd301-43e3-4789-9b02-3f040793e99f.png)

1. 로그인을 위한 요청이 서버에 전송된다


2. 데이터를 받은 서버는 데이터에 대한 유효성 검증 후 잘못된 형식의 타입 요청이 들어올 경우 에러를 반환한다

3. 정상적인 데이터의 경우 로그인한 유저에 대한 토큰을 생성하여 전달한다 

**Response**
![스크린샷 2021-11-03 오전 6 41 03](https://user-images.githubusercontent.com/42742076/139955686-d906e41f-5364-4d6c-afe2-e33edea73a08.png)


<br>

> 게시글 Create

**Request**
![스크린샷 2021-11-03 오전 6 42 43](https://user-images.githubusercontent.com/42742076/139955874-a1bdf2a5-9250-4b4b-a7e1-03740f4f7cd8.png)


1. 로그인 한 유저가 게시글 생성을 위해 서버에 요청한다

2. 요청을 받은 서버는 유저를 인가하기 위해 유저의 토큰을 검증한다(데코레이터 사용)

3. 제목 및 내용을 빈칸으로 두는 경우 등 서버는 데이터에 대한 유효성 검증 후 잘못된 형식의 타입 요청이 들어올 경우 에러를 반환한다

**Response**
![스크린샷 2021-11-03 오전 6 43 50](https://user-images.githubusercontent.com/42742076/139955994-2331a970-d4a9-4316-be25-530a4c0b53e3.png)


<br>

> 게시글 udate

**Request**
![스크린샷 2021-11-03 오전 6 47 21](https://user-images.githubusercontent.com/42742076/139956370-5596c7d3-934e-41f5-b621-7b036ef1d7f0.png)


1. 게시글 수정을 위한 요청이 서버에 전송된다.(제목, 내용, 카테고리 수정 가능)

2. 요청을 받은 서버는 유저를 인가하기 위해 유저의 토큰을 검증한다(데코레이터 사용)

3. 데이터를 받은 서버는 데이터에 대한 유효성 검증 후 잘못된 형식의 타입 요청이 들어올 경우 에러를 반환한다

4. 정상적인 데이터의 경우 글을 수정한 후 success메시지를 전달한다

**Response**
![스크린샷 2021-11-03 오전 6 47 57](https://user-images.githubusercontent.com/42742076/139956426-ee37985b-b8d4-4663-a298-b5cf8b0950c9.png)


<br>

> 게시글 delete

**Request**
![스크린샷 2021-11-03 오전 6 48 41](https://user-images.githubusercontent.com/42742076/139956525-26f48e4c-4522-4fae-8d0e-f38e8a853517.png)

1. 유저가 게시글 삭제를 위해 서버에 요청한다

2. 요청을 받은 서버는 유저를 인가하기 위해 유저의 토큰을 검증한다(데코레이터 사용)

3. 제목 및 내용을 빈칸으로 두는 경우 등 서버는 데이터에 대한 유효성 검증 후 잘못된 형식의 타입 요청이 들어올 경우 에러를 반환한다

**Response**
![스크린샷 2021-11-03 오전 6 49 12](https://user-images.githubusercontent.com/42742076/139956582-4823cf71-45f5-43d0-9de4-2cfab85f6b09.png)


<br>

> 게시글 댓글 작성

**Request**
![스크린샷 2021-11-03 오전 6 56 01](https://user-images.githubusercontent.com/42742076/139957282-e6a17665-695d-443e-935b-af6086233477.png)

1. 유저가 게시글에 댓글을 작성한다.

2. 요청을 받은 서버는 유저를 인가하기 위해 유저의 토큰을 검증한다(데코레이터 사용)

3. 제목 및 내용을 빈칸으로 두는 경우 등 서버는 데이터에 대한 유효성 검증 후 잘못된 형식의 타입 요청이 들어올 경우 에러를 반환한다

**Response**
![스크린샷 2021-11-03 오전 6 57 15](https://user-images.githubusercontent.com/42742076/139957436-7067b62e-b31a-421d-a5de-cd5c5ce7fa20.png)


<br>

> __게시글 카테고리__

1. 미리 생성되어 있던 카테고리를 글 생성시 선택하여 글에 카테고리를 부여한다 
```bash
{
   "title" : "축구",
   "text" : "축구는 재밌어 ! !"
   "category" : "스포츠"
}
```

2. 유저를 인가하기 위한 토큰을 검증 후 유저에 대한 post를 create한다

```python
category = Category.objects.get(name=data["category"])

posting = Posting.objects.create(
    title=data["title"],
    text=data["text"],
    author=user,
    category=category,
)
```

3. 글 수정시 수정 할 데이터를 서버에 요청한다 (제목, 글, 카테고리)
```bash
{
   "text" : "축구는 재밌어 ! !"
   "category" : "스포츠"
}
```

4. 유저를 인가하기 위한 토큰을 검증 후 글을 udate한다
```python
posting = Posting.objects.get(id=posting_id)
category = Category.objects.get(name=data["category"])

if request.user.id != posting.author_id:
    return JsonResponse({"message": "FORBIDDEN"}, status=403)

posting.text = data["text"] 

if data["category"] != posting.category.name:
    posting.category_id = category.id
```

<br>

> __게시글 검색__

1. 작성자, 제목, 카테고리 옵션을 선택해 검색할 데이터를 서버에 요청한다 

```bash
http://3.36.105.251:8000/posting?title="축구"&offset=2&limit=1
```

2. Q객체와 icontains를 사용하여 옵션에 맞는 게시글 목록을 필터한다

```python
OFFSET = int(request.GET.get("offset", 0))
LIMIT = int(request.GET.get("limit", 10))
CATEGORY = request.GET.get("category", None)
TITLE = request.GET.get("title", None)
USER_NAME = request.GET.get("username", None)

q = Q()

if CATEGORY:
    q &= Q(category__name = CATEGORY)

if TITLE:
    q &= Q(title__icontains = TITLE)

if USER_NAME:
    q &= Q(author__name__icontains = USER_NAME)
)
```

3. 검색된 데이터 목록을 페이지네이션 처리하여 전달한다
```bash
postings = Posting.objects.filter(q).order_by("-created_time")[
    OFFSET : OFFSET + LIMIT]
```

<br>

> __게시글 조회수__

1. 글 조회에 대한 요청이 서버에 전달된다

2. 글을 선택한 유저를 인가하기 위해 토큰을 검증한다

3. 글에 대한 유무를 검증한다

4. 인가된 유저가 게시글을 읽었는지 확인 후 게시글에 대한 조회수를 증가시킨다
```python
posting = Posting.objects.get(id=posting_id)

if user not in posting.readers.all():
    posting.readers.add(user)
    posting.hits += 1
    posting.save()
```

<br>

# 🍎 API Using Swagger

Swagger를 사용하여 API 테스트를 진행했습니다   

1. Swagger를 사용하기 위해 drf설치를 진행했습니다
```bash
pip install djangorestframework==3.12.4
pip install drf-yasg==1.20.0
```

2. swagger, redoc 접속을 위해 url을 설정했습니다
```python
schema_view_v1 = get_schema_view(
    openapi.Info(
        title="AIMMO Assignment API",
        default_version="v1",
        description="에이모 기업과제 API Document",
        terms_of_service="https://policies.google.com/terms",
    ),
    validators=["flex"],
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_patterns,
)

urlpatterns = [
    path("users", include("users.urls")),
    path("postings", include("postings.urls")),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

2. serializer를 작성했습니다
```python
from .models import Posting
from rest_framework import serializers


class PostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting
        fields = ["title", "text"]
```

3. 각 기능에서 API를 확인하고 테스트 할 수 있도록 데코레이터를 활용했습니다
```python
# 게시글 호출 예시

parameter_token = openapi.Parameter(
    "Authorization",
    openapi.IN_HEADER,
    description = "access_token",
    type = openapi.TYPE_STRING
)

@swagger_auto_schema(request_body = PostingSerializer, manual_parameters = [parameter_token])
 @login_decorator
    def get(self, request, posting_id):
        if not Posting.objects.filter(id=posting_id).exists():
            return JsonResponse(
                {"message": f"POSTING_{posting_id}_NOT_FOUND"}, status=404
            )
            ...
            ...
```

<br>

### 유저 회원가입

- Method : POST

```bash
http://3.36.105.251:8000/users/signup
```

- parameter : request_body
```bash
{
   "name" : "test1",
   "email" : "email.server.com",
   "password" : "qwerty1234"
}
```

<br>

### 유저 로그인

- Method : POST

```bash
http://3.36.105.251:8000/users/signin
```

- parameter : request_body
```bash
{
   "email" : "email.server.com",
   "password" : "qwerty1234"
}
```
<br>

### 게시글 조회

- Method : GET 

```bash
http://3.36.105.251:8000/posting/list?offset=2&limit=1
```

- parameter : query_parameter

<br>

### 게시글 검색

- Method : GET

```bash
http://3.36.105.251:8000/posting?title="축구"&offset=2&limit=1
```

- parameter : query_parameter


### 게시글 수정

- Method : PUT

```bash
http://3.36.105.251:8000/postings/1
```

- parameter : path_parameter


<br>


### 게시글 삭제

- Method : DELETE

```bash
http://3.36.105.251:8000/postings/1
```

- parameter : path_parameter


