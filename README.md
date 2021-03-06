# Tutorial-Django

Belajar Django Framework, sumber referensi tutorial dari channel Youtube Kelas Terbua [Django Kelas Terbuka](https://www.youtube.com/watch?v=hPXNP1NoVNQ&list=PLZS-MHyEIRo6p_RwsWntxMO5QAqIHHHld&index=1)

## `Setup Windows`

1. Download and Install python. Go to [https://www.python.org/](https://www.python.org/).
2. Check python in your computer `$ python --version`.
3. Check pip `$ pip list`. If pip need to upgrade please upgrade first.
4. Create a Virtual Environment `$ python -m venv Env`
5. Activate the Env, type in the terminal `$ D:\Wilden github\Tutorial-Django>Env\Scripts\activate.bat`
6. Check pip list in the (Env). Upgrade if need it `$ python.exe -m pip install --upgrade pip`. Check again
7. Install Django Versi `1.11.*` `$ pip install Django==1.11.*`. Star mean will get the last version off 1.11. django.
8. `$ pip list` to check django already installed or not.
9. Create project `$ django-admin startproject mywebsite`.
10. How to run django server.

- Go to mywebsite directory `$ cd mywebsite`
- Type `$ manage.py runserver` to run the django server
- Open [http://localhost:8000/](http://localhost:8000/) in web browser

## `Pengenalan Project`

1. Type some script in urls.py
2. Test in web browser

- [http://localhost:8000](http://localhost:8000)
- [http://localhost:8000/about](http://localhost:8000/about)

## `Pengenalan Views`

1. Create a file named views.py inside mywebsite directory
2. Cut script from urls.py and paste to views.py then edit little bit

## `Pengenalan Templates`

1. Go to settings.py and find TEMPLATES =[] (line 54)
2. Change `'DIRS': [],` to be `'DIRS': ['templates'],`
3. Create a directory named `templates`
4. Create a file named `index.html` inside templates directory

## `Pengenalan App`

1. Create a new App

- Stop server
- Create an App `$ python manage.py startapp blog`
- Run server `$ python manage.py runserver`

2. Give some script in `veiws.py` file in blog directory
3. Create a file named `blog.html` in templates directory
4. Edit script in urls.py file
5. Test with open the url [http://localhost:8000/blog/](http://localhost:8000/blog/) in web browser

6. Create a new App named About

- Stop server
- Create an App `$ python manage.py startapp about`
- Run server `$ python manage.py runserver`

7. Give some script in `veiws.py` file in blog directory
8. Create a file named `about.html` in templates directory
9. Edit script in urls.py file
10. Test with open the url [http://localhost:8000/about/](http://localhost:8000/about/) in web browser

## `Menggunakan URL pada App`

1. Create a `urls.py` file inside blog directory
2. Create a new def named `def recent:` on views.py inside blog directory

- How to test is open [http://localhost:8000/blog/recent/](http://localhost:8000/blog/recent/)

## `Template pada App`

1. Go to mywebsite directory and open setting.py file
2. Add app blog inside INSTALLED_APPS, see following below

```
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'blog',
]
```

3. Go to blog directory > Create a new directory named `templates` and Create a new directory `blog` inside templates directory
4. Go to mywebsite > templates, and Cut `blog.html`
5. Go to mywebsite > blog > templates > blog, and paste `blog.html` file

- Test, Open [http://localhost:8000/blog/](http://localhost:8000/blog/)
- Change the name `blog.html` to be `index.html`
- Test again, Open [http://localhost:8000/blog/](http://localhost:8000/blog/)

## `Template Variable`

1. Passing the variable from views.py to index.html
2. Edit mywebsite\views.py and tamplates\index.html
3. Test with [http://localhost:8000/](http://localhost:8000/)
4. Passing the variable from blog\views.py to mywebsite\index.html
5. Edit blog\views.py
6. Test with [http://localhost:8000/blog/](http://localhost:8000/blog/)
7. Passing the variable from blog\views.py to blog\templates\blog\index.html
8. Edit blog\views.py
9. Test with [http://localhost:8000/blog/cerita/](http://localhost:8000/blog/cerita/)
10. Passing the variable news from blog\views.py to blog\templates\blog\index.html
11. Edit blog\views.py
12. Test with [http://localhost:8000/blog/news/](http://localhost:8000/blog/news/)

## `Template Tags`

1. Go to mywebsite\mywebsite\views.py
2. Change context in views.py
3. Go to mywebsite\templates\index.html
4. Change some script in index.html

# `Django Static File Add Pictures`

0. Make sure you are in Env mode (Activate the Env, type in the terminal `$ D:\Wilden github\Tutorial-Django>Env\Scripts\activate.bat`)
1. Create project `$ django-admin startproject mywebsite`.
2. Rename the app form `mywebsite` to be `Django_StaticFileAddPictures`
3. How to run django server.

- Go to mywebsite directory `$ cd Django_StaticFileAddPictures`
- Type `$ manage.py runserver` to run the django server
- Open [http://localhost:8000/](http://localhost:8000/) in web browser

4. Creata blog app, type in terminal `$ python manage.py startapp blog`
5. Creata about app, type in terminal `$ python manage.py startapp about`
6. Create a folder named `templates` inside Django_StaticFileAddPicture folder
7. Create a folder named `static\img` inside Django_StaticFileAddPicture folder
8. Setting INSTALLED_APP, TEMPLATES and STATICFILES_DIRS in setting.py

- Open Django_StaticFileAddPicture\mywebsite\settings.py
- Add 'blog', 'about', in INSTALLED_APP
- Edit to be 'DIRS': ['templates'], in TEMPLATES
- Bottom of STATIC_URL='/static/' add script like following below

```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

9. Test pictures

- Move the banner_home.png to folder static\img\banner_home.png
- Open [http://localhost:8000/static/img/banner_home.png](http://localhost:8000/static/img/banner_home.png) in web browser

10. Create folder inside blog app so look like this

- static
  - \blog
    - \img
- templates

11. Create folder inside about app so look like this

- static
  - \about
    - \img
- templates

12. Move `banner_blog.png` to Django_StaticFileAddPictures\blog\static\blog\img
13. Move `banner_about.png` to Django_StaticFileAddPictures\about\static\about\img
14. Create `index.html` file inside Django_StaticFileAddPictures\templates
15. Create `view.py` file inside Django_StaticFileAddPictures\mywebsite
16. Edit `urls.py` file inside Django_StaticFileAddPictures\mywebsite
17. Static file in blog app

- Create `urls.py` file inside Django_StaticFileAddPictures\blog
- Edit `views.py` file inside Django_StaticFileAddPictures\blog
- Create `index.html` file inside Django_StaticFileAddPictures\blog\templates\blog

18. Static file in about app

- Create `urls.py` file inside Django_StaticFileAddPictures\about
- Edit `views.py` file inside Django_StaticFileAddPictures\about
- Create `index.html` file inside Django_StaticFileAddPictures\about\templates\about

# `Django with Bootstrap`

0. Make sure you are in Env mode (Activate the Env, type in the terminal `$ D:\Wilden github\Tutorial-Django>Env\Scripts\activate.bat`)
1. Create project `$ django-admin startproject mywebsite`.
2. Rename the app form `mywebsite` to be `Django_withBootstrap`
3. How to run django server.

- Go to mywebsite directory `$ cd Django_withBootstrap`
- Type `$ python manage.py runserver` to run the django server
- Open [http://localhost:8000/](http://localhost:8000/) in web browser

4. Creata blog and about app

- For Blog app, type in terminal `$ python manage.py startapp blog`
- For Blog app, type in terminal `$ python manage.py startapp about`

5. Create static folder and templates folder
6. Inside static folder create css, img, js and vendor folder
7. Download the assets for project. The link is [https://github.com/kelasterbuka/django1.11_LTS_tutorial/tree/master/13_Static_File_menambah_bootstrap_dan_js/01-Assets](https://github.com/kelasterbuka/django1.11_LTS_tutorial/tree/master/13_Static_File_menambah_bootstrap_dan_js/01-Assets).
8. Save the images from point no 7 to Django_withBootstrap\static\img
9. Bootstrap setup

- Go to [https://getbootstrap.com/docs/4.5/getting-started/download/](https://getbootstrap.com/docs/4.5/getting-started/download/)
- On <b>Compiled CSS and JS</b> click `Download` button.
- Create folder named bootstrap inside Django_withBootstrap\static
- Copy `bootstrap.css` from bootstrap-4.5.2-dist\css folder and Paste to Django_withBootstrap\static\bootstrap folder
- Copy `bootstrap.js` from bootstrap-4.5.2-dist\js folder and Paste to Django_withBootstrap\static\bootstrap folder

10. Setup settings.py, change the script like following below

```
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'blog',
  'about',
]
```

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

and add STATICFILES_DIRS script below STATIC_URL = '/static/'

```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

11. Create a views.py file on Django_withBootstrap\mywebsite
12. Run server `$ python manage.py runserver`

### Template Inheritance and Include

1. Download assets images from [https://github.com/kelasterbuka/django1.11_LTS_tutorial/tree/master/14_Template%20Inheritance%20dan%20Include/01%20-%20Assets](https://github.com/kelasterbuka/django1.11_LTS_tutorial/tree/master/14_Template%20Inheritance%20dan%20Include/01%20-%20Assets)
2. Crete folder static inside Django_withBootstrap\blog

- Create `static` folder inside Django_withBootstrap\blog
- Create folder named `blog` inside Django_withBootstrap\blog\static
- Create 3 folder inside Django_withBootstrap\blog\static\blog namely `css`, `img`, and `js`

3. Crete folder static inside Django_withBootstrap\about

- Create `static` folder inside Django_withBootstrap\about
- Create folder named `about` inside Django_withBootstrap\about\static
- Create 3 folder inside Django_withBootstrap\about\static\about namely `css`, `img`, and `js`

4. Move the `bannerBlog.png` to Django_withBootstrap\blog\static\blog\img
5. Move the `bannerAbout.png` to Django_withBootstrap\about\static\about\img
6. Create a folder named snippets in Django_withBootstrap\templates
8. Done with Include and Inheritance for index.html and base.html
9. Create Inheritance for blog app

- Create ulrs.py inside Django_withBootstrap\blog
- Create templates folder inside Django_withBootstrap\blog

# `Setup MySQL + XAMPP in Windows`
1. Install XAMPP [https://www.apachefriends.org/download.html](https://www.apachefriends.org/download.html)
2. Start Apache and MySQL
3. Access MySQL in the terminal.
- Open terminal
- Type `$ mysql -u root -p`. pw: `` ga pake password, enter aja
4. Go to [https://www.mysql.com/downloads/](https://www.mysql.com/downloads/)
5. Click `MySQL Community (GPL) Downloads »` link. It will going to  [https://dev.mysql.com/downloads/](https://dev.mysql.com/downloads/)
6. Click [MySQL Community Server](https://dev.mysql.com/downloads/mysql/)
7. Click Image [MySQL Installer for Windows](https://dev.mysql.com/downloads/windows/installer/8.0.html)
9. Click `Download` button in <b>Windows (x86, 32-bit), MSI Installer</b>
10. Click `No thanks, just start my download.` link, it will be download the installer of MySQL installer web community
11. Install the MySQL Installer, just install MySQL Connector/C++
12. Install MySQL in the Django Project
- Make sure you are in Env mode (Activate the Env, type in the terminal `$ D:\Wilden github\Tutorial-Django>Env\Scripts\activate.bat`)
- Goto [https://www.lfd.uci.edu/~gohlke/pythonlibs/](https://www.lfd.uci.edu/~gohlke/pythonlibs/) to download Mysqlclient
- Choose `mysqlclient‑1.4.6‑cp38‑cp38‑win32.whl`. Before that please check python version `$ python`. For example if yout python version use 3.8.5 and 32bit so download the myssqlclient `xx-cp38-win32.whl`
- Move the `mysqlclient‑1.4.6‑cp38‑cp38‑win32.whl` file to your folder project `D:\Wilden github\Tutorial-Django`
- Install wheel `$ pip install wheel` for running the .whl file
- Install .whl file `$ pip install mysqlclient‑1.4.6‑cp38‑cp38‑win32.whl`
- To check your mysqlclient already installed type `$ pip list` and if mysqlclient on the list that mean your mysqlclient already installed