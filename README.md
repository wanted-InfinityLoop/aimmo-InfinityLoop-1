# π Wanted X Wecode PreOnBoarding Backend Course | λ¬΄νλ£¨ν-1ν
μν°λ 1μ£Όμ°¨ κΈ°μ κ³Όμ  : Aimmo Assignment Project
  β Aimmo κΈ°μ κ³Όμ μλλ€.

<br>

# λͺ©μ°¨
- ### Project Build & Skills 
- ### How To Implement
- ### How To Execute
- ### API Using Swagger 
- ### μλ² λ°°ν¬

<br>


# βοΈ Project Build

### Build(AWS EC2)
API Base URL : http://3.36.105.251:8000
<br>

API Document URL : http://3.36.105.251:8000/swagger/

### Required
- Python3.7πΊ
- Django (version κΈ°μ)πΊ
- MongoDB (version κΈ°μ)πΊ

### Add setting file
- Projectν΄λ μμ my_settings.py νμΌ μμ± ν λ΄μ© μΆκ°
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
βββ CONVENTION.md
βββ PULL_REQUEST_TEMPLATE.md
βββ README.md
βββ config
βΒ Β  βββ asgi.py
βΒ Β  βββ settings.py
βΒ Β  βββ urls.py
βΒ Β  βββ wsgi.py
βββ core
βΒ Β  βββ admin.py
βΒ Β  βββ apps.py
βΒ Β  βββ models.py
βΒ Β  βββ tests.py
βΒ Β  βββ utils.py
βΒ Β  βββ views.py
βββ manage.py
βββ my_settings.py
βββ postings
βΒ Β  βββ admin.py
βΒ Β  βββ apps.py
βΒ Β  βββ models.py
βΒ Β  βββ serializer.py
βΒ Β  βββ tests.py
βΒ Β  βββ urls.py
βΒ Β  βββ views.py
βββ requirements.txt
βββ users
    βββ admin.py
    βββ apps.py
    βββ models.py
    βββ serializer.py
    βββ tests.py
    βββ urls.py
    βββ views.py
```

# π Skills

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


# π§βπ¨ How To Implement 

- DBμ λ―Έλ¦¬ κ²μκΈ μΉ΄νκ³ λ¦¬μ λν λ°μ΄ν°λ₯Ό λ£μ΄ κΈ μμ±μ μΉ΄νκ³ λ¦¬λ₯Ό μ νν΄ μμ±ν  μ μλλ‘ κ΅¬ννμμ΅λλ€.     
  βͺοΈ κΈ μμ±κ³Ό λμμ μΉ΄νκ³ λ¦¬κ° μΆκ°λλ©΄ νκ·Έμ κΈ°λ₯μ΄ κ°ν΄λ³΄μ¬ μΉ΄νκ³ λ¦¬μ λν λͺ¨λΈμ λ§λ€μ΄ λ°μ΄ν°λ₯Ό μΆκ°ν΄μ£Όμμ΅λλ€.   

<br>

- Qκ°μ²΄μ __ icontainsν€μλλ₯Ό μ¬μ©ν΄ μΉ΄νκ³ λ¦¬, μμ±μ, μ λͺ©μ κΈ°μ€μΌλ‘ κ²μκΈ°λ₯μ κ΅¬ννμμ΅λλ€.     
   βͺοΈ μ μ κ° κ²μμ΅μκ³Ό κ²μν  λ°μ΄ν°λ₯Ό μλ ₯ν΄ μμ²­νλ©΄ ν΄λΉ λ°μ΄ν°κ° ν¬ν¨λμ΄ μλ κΈμ LimitOffsetPaginationμΌλ‘ νμ΄μ§ μ²λ¦¬ν΄μ£Όμμ΅λλ€.  

<br>

- Posting modelμ νΉμ  κΈμ μ½μ μ μ λ₯Ό ManyToManyλ₯Ό μ΄μ©ν΄ addνμ΅λλ€. κΈμ μ²μ μ½λ μ μ λΌλ©΄ hitsλΌλ κ°μ 1μ¦κ°μν¨ν addν΄μ£Όμμ΅λλ€.     
   βͺοΈ κΈμ μ½μ μ μ λ₯Ό κΈ°μ΅ν  μ μλ λ°©λ² μ€ ManyToManyλ₯Ό μ ννμ΅λλ€. μ΄ν refactoringμ ν΅ν΄ λ λμ λ°©λ²μ κ³ λ €νκ³  μμ΅λλ€[(wiki)


<br>

- REST APIλ₯Ό μμ±νλ©° μ§μ€ν λΆλΆμ λ€μκ³Ό κ°μ΅λλ€. μλμ κ°μ μ‘°κ±΄μ κ³ λ €νμ¬ __postλ©μλ μμ²­μΌλ‘ κ²μκΈ μμ±νκΈ°__, __getλ©μλ μμ²­μΌλ‘ κ²μκΈμ λΆλ¬μ€κΈ°__ , __putλ©μλ μμ²­μΌλ‘ κ²μκΈ μμ νκΈ°__ , __deleteλ©μλ μμ²­μΌλ‘ κ²μκΈ μ­μ νκΈ°__ λ‘ μ€κ³νμ΅λλ€.
```  
κΈ°λ₯μ λ§λ HTTPλ©μλ μ ν
κ°λμ± μλ URLλ€μ΄λ°μ μν κ·μΉ
μ μ ν HTTP μνμ½λμ ν€λ 
```

<br>

- μ½λμ λν λ²κ·Έκ° μλμ§ μλμ§ μ²΄ν¬νκΈ° μν μ λ νμ€νΈλ₯Ό λ§λ€μ΄ λ¬Έμ λ₯Ό μ½κ² ν΄κ²°ν  μ μλλ‘ λΈλ ₯νμ΅λλ€. unit test κ΅¬νν μ΄λ λΆλΆμ λ¬Έμ κ° μμΌλ©° μ΄λλ₯Ό κ³ μ³μΌ ν μ§ λͺννκ² μ μ μμκΈ°μ κ°λ° μ€ λ―Έλ¦¬ λ¬Έμ λ₯Ό νμνλλ° λμμ΄ λμμ΅λλ€.


<br>

# β―οΈ How To Execute

> Sign Up

**Request**
![αα³αα³αα΅α«αα£αΊ 2021-11-03 αα©αα₯α« 6 38 23](https://user-images.githubusercontent.com/42742076/139955395-f6977354-8f9c-418c-bbae-c8a0a4089127.png)


1. μ μ κ° μλ ₯ν λ°μ΄ν° μμ²­μ΄ μλ²μ μ μ‘λλ€

2. λ°μ΄ν°λ₯Ό λ°μ μλ²λ λ°μ΄ν°μ λν μ ν¨μ± κ²μ¦ ν μλͺ»λ νμμ νμ μμ²­μ΄ λ€μ΄μ¬ κ²½μ° μλ¬λ₯Ό λ°ννλ€


3. μ μμ μΈ λ°μ΄ν°μ κ²½μ° DBμ μ μ λ₯Ό createνλ€   

**Response**
![αα³αα³αα΅α«αα£αΊ 2021-11-03 αα©αα₯α« 6 39 04](https://user-images.githubusercontent.com/42742076/139955468-491823c9-9a59-4e63-9bc3-487c5aa17e55.png)

<br>

> Sign in

**Request**
![αα³αα³αα΅α«αα£αΊ 2021-11-03 αα©αα₯α« 6 40 35](https://user-images.githubusercontent.com/42742076/139955640-adadd301-43e3-4789-9b02-3f040793e99f.png)

1. λ‘κ·ΈμΈμ μν μμ²­μ΄ μλ²μ μ μ‘λλ€


2. λ°μ΄ν°λ₯Ό λ°μ μλ²λ λ°μ΄ν°μ λν μ ν¨μ± κ²μ¦ ν μλͺ»λ νμμ νμ μμ²­μ΄ λ€μ΄μ¬ κ²½μ° μλ¬λ₯Ό λ°ννλ€

3. μ μμ μΈ λ°μ΄ν°μ κ²½μ° λ‘κ·ΈμΈν μ μ μ λν ν ν°μ μμ±νμ¬ μ λ¬νλ€ 

**Response**
![αα³αα³αα΅α«αα£αΊ 2021-11-03 αα©αα₯α« 6 41 03](https://user-images.githubusercontent.com/42742076/139955686-d906e41f-5364-4d6c-afe2-e33edea73a08.png)


<br>

> κ²μκΈ Create

**Request**
![αα³αα³αα΅α«αα£αΊ 2021-11-03 αα©αα₯α« 6 42 43](https://user-images.githubusercontent.com/42742076/139955874-a1bdf2a5-9250-4b4b-a7e1-03740f4f7cd8.png)


1. λ‘κ·ΈμΈ ν μ μ κ° κ²μκΈ μμ±μ μν΄ μλ²μ μμ²­νλ€

2. μμ²­μ λ°μ μλ²λ μ μ λ₯Ό μΈκ°νκΈ° μν΄ μ μ μ ν ν°μ κ²μ¦νλ€(λ°μ½λ μ΄ν° μ¬μ©)

3. μ λͺ© λ° λ΄μ©μ λΉμΉΈμΌλ‘ λλ κ²½μ° λ± μλ²λ λ°μ΄ν°μ λν μ ν¨μ± κ²μ¦ ν μλͺ»λ νμμ νμ μμ²­μ΄ λ€μ΄μ¬ κ²½μ° μλ¬λ₯Ό λ°ννλ€

**Response**
![αα³αα³αα΅α«αα£αΊ 2021-11-03 αα©αα₯α« 6 43 50](https://user-images.githubusercontent.com/42742076/139955994-2331a970-d4a9-4316-be25-530a4c0b53e3.png)


<br>

> κ²μκΈ udate

**Request**
![αα³αα³αα΅α«αα£αΊ 2021-11-03 αα©αα₯α« 6 47 21](https://user-images.githubusercontent.com/42742076/139956370-5596c7d3-934e-41f5-b621-7b036ef1d7f0.png)


1. κ²μκΈ μμ μ μν μμ²­μ΄ μλ²μ μ μ‘λλ€.(μ λͺ©, λ΄μ©, μΉ΄νκ³ λ¦¬ μμ  κ°λ₯)

2. μμ²­μ λ°μ μλ²λ μ μ λ₯Ό μΈκ°νκΈ° μν΄ μ μ μ ν ν°μ κ²μ¦νλ€(λ°μ½λ μ΄ν° μ¬μ©)

3. λ°μ΄ν°λ₯Ό λ°μ μλ²λ λ°μ΄ν°μ λν μ ν¨μ± κ²μ¦ ν μλͺ»λ νμμ νμ μμ²­μ΄ λ€μ΄μ¬ κ²½μ° μλ¬λ₯Ό λ°ννλ€

4. μ μμ μΈ λ°μ΄ν°μ κ²½μ° κΈμ μμ ν ν successλ©μμ§λ₯Ό μ λ¬νλ€

**Response**
![αα³αα³αα΅α«αα£αΊ 2021-11-03 αα©αα₯α« 6 47 57](https://user-images.githubusercontent.com/42742076/139956426-ee37985b-b8d4-4663-a298-b5cf8b0950c9.png)


<br>

> κ²μκΈ delete

**Request**
![αα³αα³αα΅α«αα£αΊ 2021-11-03 αα©αα₯α« 6 48 41](https://user-images.githubusercontent.com/42742076/139956525-26f48e4c-4522-4fae-8d0e-f38e8a853517.png)

1. μ μ κ° κ²μκΈ μ­μ λ₯Ό μν΄ μλ²μ μμ²­νλ€

2. μμ²­μ λ°μ μλ²λ μ μ λ₯Ό μΈκ°νκΈ° μν΄ μ μ μ ν ν°μ κ²μ¦νλ€(λ°μ½λ μ΄ν° μ¬μ©)

3. μ λͺ© λ° λ΄μ©μ λΉμΉΈμΌλ‘ λλ κ²½μ° λ± μλ²λ λ°μ΄ν°μ λν μ ν¨μ± κ²μ¦ ν μλͺ»λ νμμ νμ μμ²­μ΄ λ€μ΄μ¬ κ²½μ° μλ¬λ₯Ό λ°ννλ€

**Response**
![αα³αα³αα΅α«αα£αΊ 2021-11-03 αα©αα₯α« 6 49 12](https://user-images.githubusercontent.com/42742076/139956582-4823cf71-45f5-43d0-9de4-2cfab85f6b09.png)


<br>

> κ²μκΈ λκΈ μμ±

**Request**
![αα³αα³αα΅α«αα£αΊ 2021-11-03 αα©αα₯α« 6 56 01](https://user-images.githubusercontent.com/42742076/139957282-e6a17665-695d-443e-935b-af6086233477.png)

1. μ μ κ° κ²μκΈμ λκΈμ μμ±νλ€.

2. μμ²­μ λ°μ μλ²λ μ μ λ₯Ό μΈκ°νκΈ° μν΄ μ μ μ ν ν°μ κ²μ¦νλ€(λ°μ½λ μ΄ν° μ¬μ©)

3. μ λͺ© λ° λ΄μ©μ λΉμΉΈμΌλ‘ λλ κ²½μ° λ± μλ²λ λ°μ΄ν°μ λν μ ν¨μ± κ²μ¦ ν μλͺ»λ νμμ νμ μμ²­μ΄ λ€μ΄μ¬ κ²½μ° μλ¬λ₯Ό λ°ννλ€

**Response**
![αα³αα³αα΅α«αα£αΊ 2021-11-03 αα©αα₯α« 6 57 15](https://user-images.githubusercontent.com/42742076/139957436-7067b62e-b31a-421d-a5de-cd5c5ce7fa20.png)


<br>

> __κ²μκΈ μΉ΄νκ³ λ¦¬__

1. λ―Έλ¦¬ μμ±λμ΄ μλ μΉ΄νκ³ λ¦¬λ₯Ό κΈ μμ±μ μ ννμ¬ κΈμ μΉ΄νκ³ λ¦¬λ₯Ό λΆμ¬νλ€ 
```bash
{
   "title" : "μΆκ΅¬",
   "text" : "μΆκ΅¬λ μ¬λ°μ΄ ! !"
   "category" : "μ€ν¬μΈ "
}
```

2. μ μ λ₯Ό μΈκ°νκΈ° μν ν ν°μ κ²μ¦ ν μ μ μ λν postλ₯Ό createνλ€

```python
category = Category.objects.get(name=data["category"])

posting = Posting.objects.create(
    title=data["title"],
    text=data["text"],
    author=user,
    category=category,
)
```

3. κΈ μμ μ μμ  ν  λ°μ΄ν°λ₯Ό μλ²μ μμ²­νλ€ (μ λͺ©, κΈ, μΉ΄νκ³ λ¦¬)
```bash
{
   "text" : "μΆκ΅¬λ μ¬λ°μ΄ ! !"
   "category" : "μ€ν¬μΈ "
}
```

4. μ μ λ₯Ό μΈκ°νκΈ° μν ν ν°μ κ²μ¦ ν κΈμ udateνλ€
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

> __κ²μκΈ κ²μ__

1. μμ±μ, μ λͺ©, μΉ΄νκ³ λ¦¬ μ΅μμ μ νν΄ κ²μν  λ°μ΄ν°λ₯Ό μλ²μ μμ²­νλ€ 

```bash
http://3.36.105.251:8000/posting?title="μΆκ΅¬"&offset=2&limit=1
```

2. Qκ°μ²΄μ icontainsλ₯Ό μ¬μ©νμ¬ μ΅μμ λ§λ κ²μκΈ λͺ©λ‘μ νν°νλ€

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

3. κ²μλ λ°μ΄ν° λͺ©λ‘μ νμ΄μ§λ€μ΄μ μ²λ¦¬νμ¬ μ λ¬νλ€
```bash
postings = Posting.objects.filter(q).order_by("-created_time")[
    OFFSET : OFFSET + LIMIT]
```

<br>

> __κ²μκΈ μ‘°νμ__

1. κΈ μ‘°νμ λν μμ²­μ΄ μλ²μ μ λ¬λλ€

2. κΈμ μ νν μ μ λ₯Ό μΈκ°νκΈ° μν΄ ν ν°μ κ²μ¦νλ€

3. κΈμ λν μ λ¬΄λ₯Ό κ²μ¦νλ€

4. μΈκ°λ μ μ κ° κ²μκΈμ μ½μλμ§ νμΈ ν κ²μκΈμ λν μ‘°νμλ₯Ό μ¦κ°μν¨λ€
```python
posting = Posting.objects.get(id=posting_id)

if user not in posting.readers.all():
    posting.readers.add(user)
    posting.hits += 1
    posting.save()
```

<br>

# π API Using Swagger

Swaggerλ₯Ό μ¬μ©νμ¬ API νμ€νΈλ₯Ό μ§ννμ΅λλ€   

1. Swaggerλ₯Ό μ¬μ©νκΈ° μν΄ drfμ€μΉλ₯Ό μ§ννμ΅λλ€
```bash
pip install djangorestframework==3.12.4
pip install drf-yasg==1.20.0
```

2. swagger, redoc μ μμ μν΄ urlμ μ€μ νμ΅λλ€
```python
schema_view_v1 = get_schema_view(
    openapi.Info(
        title="AIMMO Assignment API",
        default_version="v1",
        description="μμ΄λͺ¨ κΈ°μκ³Όμ  API Document",
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

2. serializerλ₯Ό μμ±νμ΅λλ€
```python
from .models import Posting
from rest_framework import serializers


class PostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting
        fields = ["title", "text"]
```

3. κ° κΈ°λ₯μμ APIλ₯Ό νμΈνκ³  νμ€νΈ ν  μ μλλ‘ λ°μ½λ μ΄ν°λ₯Ό νμ©νμ΅λλ€
```python
# κ²μκΈ νΈμΆ μμ

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

### μ μ  νμκ°μ

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

### μ μ  λ‘κ·ΈμΈ

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

### κ²μκΈ μ‘°ν

- Method : GET 

```bash
http://3.36.105.251:8000/posting/list?offset=2&limit=1
```

- parameter : query_parameter

<br>

### κ²μκΈ κ²μ

- Method : GET

```bash
http://3.36.105.251:8000/posting?title="μΆκ΅¬"&offset=2&limit=1
```

- parameter : query_parameter


### κ²μκΈ μμ 

- Method : PUT

```bash
http://3.36.105.251:8000/postings/1
```

- parameter : path_parameter


<br>


### κ²μκΈ μ­μ 

- Method : DELETE

```bash
http://3.36.105.251:8000/postings/1
```

- parameter : path_parameter

