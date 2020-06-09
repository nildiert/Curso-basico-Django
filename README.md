# Curso Básico Django

* Crear el entorno
    ```python3 -m venv .env``` 
* Activar el entorno
    ```source .env/bin/activate```
* Desactivar el entorno
    ```deactivate```

* Crear proyecto
    ``` django-admin startproject platzigram . ```

* Correr servidor
    ```python3 manage.py runserver```

* Importar y ejecutar debugger
    ```import pdb; pdb.set_trace()```

    * Headers: ```request.META```
    * Metodo: ```request.method```
    * Continuar ejecución: ```c```
    * Imprimir GET: ```request.GET['numbers']```
        * ```localhost:8000/hi/?numbers=10,2,4,50```
* Retornar JSON:
    * ```python
        from django.http import HttpResponse
        import json

        data = {
            'status': 'ok',
            'numbers': [1,2,3],
            'message': 'Cool!',
        }
        return HttpResponse(json.dumps(data, indent=4)  content_type='application/json')
        ```
* Datos desde una URL
    ```python
    # url.py

    path('hi/<str:name>/<int:age>', views.say_hi),

    # views.py

    def say_hi(request, name, age):
        return HttpResponse('Hi {} you have {} years old'.forma(name, age))

    # URL
    http://127.0.0.1:8000/hi/nildiert/27
    ```
* Crear app
    ``` python
    # Crear app
    python3 manage.py startapp name_app

    # settings.py

    INSTALLED_APPS = [
        ...

        'name_app'
    ]

    # urls.py
    from name_app import views as posts_views

    path('name_app/', posts_views.name_function)

    # posts.views.py

    def name_function:
        pass

    ```
* Crear html desde el back
    ```python
    posts = [
    {
        'name': 'Mont Black',
        'user': 'Yessica',
        'timestamp': datetime.now(),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name': 'Bogota',
        'user': 'Nildiert',
        'timestamp': datetime.now(),
        'picture': 'https://picsum.photos/200/200/?image=1037',
    },
    {
        'name': 'Otro',
        'user': 'Gilberto',
        'timestamp': datetime.now(),
        'picture': 'https://picsum.photos/200/200/?image=1038',
    },
    ]


    def list_posts(request):
    content = []
    for post in posts:
        content.append("""
                       <p><strong>{name}</strong></p>
                       <p><small>{user} - <i>{timestamp}</i></small></p>
                       <figure><img src="{picture}"></figure>
                       """.format(**post))
    return HttpResponse('<br>'.join(content))
    ```
* Render template
    ```python
    # views.py
    from django.shortcuts import render

    posts = [
        {
            'title': 'Mont Blanc',
            'user': {
                'name': 'Yésica Cortés',
                'picture': 'https://picsum.photos/60/60/?image=1027'
            },
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'photo': 'https://picsum.photos/800/600?image=1036',
        },
        {
            'title': 'Via Láctea',
            'user': {
                'name': 'Christian Van der Henst',
                'picture': 'https://picsum.photos/60/60/?image=1005'
            },
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'photo': 'https://picsum.photos/800/800/?image=903',
        },
        {
            'title': 'Nuevo auditorio',
            'user': {
                'name': 'Uriel (thespianartist)',
                'picture': 'https://picsum.photos/60/60/?image=883'
            },
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'photo': 'https://picsum.photos/500/700/?image=1076',
        }
    ]

    def list_posts(request):
        return render(request, 'feed.html', {'posts': posts})

    # feed.html

    {% for post in posts %}
        <div class="col-lg-4 offset-lg-4">
            <div class="media">
                <img src="{{ post.user.picture }}" alt="{{ post.user.name }}" class="mr-3 rounded-circle">
                <div class="media-body">
                    <h5 class="mt-0">{{ post.user.name }}</h5> 
                    {{ post.timestamp }}
                </div>
            </div>
            <img src="{{ post.photo }}" alt="{{ post.title }}" class="img-fluid mt-3 border rounder">
            <h6 class="ml-1 mt-1">{{ post.title }}</h6>
        </div>
    {% endfor %}
    ```

## ORM 

* Migraciones
    ```shell
    python3 manage.py migrate
    ```
* Crear modelo
    ```python
    # models.py

    from django.db import models


    class User(models.Model):

        email = models.EmailField(unique=True)
        password = models.CharField(max_length=100)

        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)

        bio = models.CharField(blank=True, max_length=100)

        birthdate = models.DateTimeField(blank=True, null=True)
    
        created = models.DateTimeField(auto_now_add=True)
        modified = models.DateTimeField(auto_now=True)
    
    
    ```

* Realizar cambios en las migraciones
    ```bash
    python3 manage.py makemigrations
    ```

* Cargar shell Django y agregar datos
    ```bash
    python3 manage.py shell
    ```

    ```shell
    (InteractiveConsole)
    >>> from posts.models import User
    >>> pablo = User.objects.create(
    ...     email='hola@gmail.com',
    ...     password='1234567',
    ...     first_name='Pablo',
    ...     last_name='Trinidad'
    ... )
    >>> pablo.email
    'hola@gmail.com'
    >>> pablo.pk
    1
    >>> pablo.email = 'pablo@gmail.com'
    >>> pablo.save()
    >>> pablo.created
    datetime.datetime(2020, 6, 9, 7, 42, 18, 32304, tzinfo=<UTC>)
    >>> pablo.modified
    datetime.datetime(2020, 6, 9, 7, 44, 49, 551718, tzinfo=<UTC>)
    >>> 

    ```
* Otra forma de agregar datos
    ```shell
    >>> arturo = User()
    >>> arturo.pk
    >>> arturo.email = 'arturo@platzi.com'
    >>> arturo.first_name = 'Arturo'
    >>> arturo.last_name = 'Martínez'
    >>> arturo.password = 'MSIComputer'
    >>> arturo.is_admin = True
    >>> arturo.save()

    # Borrar datos
    >>> arturo.delete()
    (1, {'posts.User': 1})

    ```

* Agregar varios datos
    ```python

    from datetime import date

    users = [
        {
            'email': 'cvander@platzi.com',
            'first_name': 'Christian',
            'last_name': 'Van der Henst',
            'password': '1234567',
            'is_admin': True
        },
        {
            'email': 'freddier@platzi.com',
            'first_name': 'Freddy',
            'last_name': 'Vega',
            'password': '987654321'
        },
        {
            'email': 'yesica@platzi.com',
            'first_name': 'Yésica',
            'last_name': 'Cortés',
            'password': 'qwerty',
            'birthdate': date(1990, 12,19)
        },
        {
            'email': 'arturo@platzi.com',
            'first_name': 'Arturo',
            'last_name': 'Martínez',
            'password': 'msicomputer',
            'is_admin': True,
            'birthdate': date(1981, 11, 6),
            'bio': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        }
    ]

    from posts.models import User

    for user in users:
        obj = User(**user)
        obj.save()
        print(obj.pk)
    ```
    ```shell
    >>> from posts.models import User
    >>> user = User.objects.get(email='freddier@platzi.com')
    >>> user
    <User: User object (4)>
    >>> type(user)
    <class 'posts.models.User'>
    >>> user.pk
    4
    >>> user.first_name
    'Freddy'
    >>> user.password
    '987654321'

    # Traer todos los usuarios de platzi
    >>> platzi_users = User.objects.filter(email__endswith='@platzi.com')
    >>> platzi_users
    <QuerySet [<User: User object (3)>, <User: User object (4)>, <User: User object (5)>, <User: User object (6)>]>

    ```
*  *Para retornar el string en vez del id*

    ```python
    

    # models.py
    # Agregamos el metodo

    def __str__(self):
        return self.email
    ```

    ```shell
    >>> from posts.models import User
    >>> platzi_users = User.objects.filter(email__endswith='@platzi.com')
    >>> platzi_users
    <QuerySet [<User: cvander@platzi.com>, <User: freddier@platzi.com>, <User: yesica@platzi.com>, <User: arturo@platzi.com>]>
    ```
* Traer todos los usuarios
    ```shell
    >>> users = User.objects.all()
    >>> users
    <QuerySet [<User: pablo@gmail.com>, <User: cvander@platzi.com>, <User: freddier@platzi.com>, <User: yesica@platzi.com>, <User: arturo@platzi.com>]>
    ```
* Actualizar todos unos valores pedidos
    ```shell
    >>> platzi_users = User.objects.filter(email__endswith='@platzi.com')
    >>> for u in platzi_users:
    ...    print(u.email, ':', u.is_admin)
    ...
    cvander@platzi.com : True
    freddier@platzi.com : False
    yesica@platzi.com : False
    arturo@platzi.com : True

    # Aquí actualizamos datos
    >>> platzi_users = User.objects.filter(email__endswith='@platzi.com').update(is_admin=True)

    >>> platzi_users = User.objects.filter(email__endswith='@platzi.com')
    >>> for u in platzi_users:
    ...     print(u.email, ':', u.is_admin)
    ... 
    cvander@platzi.com : True
    freddier@platzi.com : True
    yesica@platzi.com : True
    arturo@platzi.com : True
    ```

    [Django Queries](https://docs.djangoproject.com/en/3.0/topics/db/queries/)

* Crear usuario
    ```shell
    python3 manage.py shell
    ```
    ```shell
    >>> from django.contrib.auth.models import User
    >>> u = User.objects.create_user(username='yesika', password='admin123')
    >>> u
    <User: yesika>
    >>> u.pk
    1
    >>> u.username
    'yesika'
    >>> u.password
    'pbkdf2_sha256$180000$OEKjaHZCpDQi$FkyLQnFevfqc3VOD+ehBkWKhy9ZhUQa7NTW7ffH2DEk='
    >>> 

* Crear super usuario
    ```shell
    (.env) ➜  Platzi-gram python3 manage.py createsuperuser 

    Username (leave blank to use 'mrbizarro'): pablo
    Email address: p@gmail.com
    Password: 
    Password (again): 
    Superuser created successfully.

    ```
    * Registrar url admin
        ```python
        # urls.py
        from django.contrib import admin

        urlpatters = [
            path('admin/', admin.site.urls)
        ]

        ```

