# Introduction

Mindful Rise is a platform to look up and deepen in mindfulness, self development and methods for reach a significant and higher self.
Its´s a place where you can reach loke minded and new friends from comments view.
You can see the post likes on indexpage, so you can choose the ost interesting blogs.
You can sign in as a member and get full access to everything.

### Live web site: https://mindfulrise-f0e0db837715.herokuapp.com/

## Content

* Project Set Up
* User stories
* Mindmap
* ERD
* Wireframes
* CRUD
* Features
* Homepage
* Blog Page
* Courses
* Nav Bar
* Footer
* 404-page
* Favicon 
* Register section
* Setting up workspace
* Design
* Testing
* Bugs
* Technologies
* Packages
* Deployment
* Media
* Images
* Font
* Database
* Framework
* Media
* Icons
* Images
* Acknowledgements


## Project Set Up

I Started this project with an idea to create a blog with posts only for me.
And to ad more exclusive content, I choosed to make a page eith Courses, to deep down with the development of yourself.

I started with a mindmap to brainstorm and draw wireframes of content and look of the site.
I started making a project in GitHub, there I created user stories.

After that, I created an ERD to plan how to build the project.

In Gitpod, I decided to only have one app, because Blog and Courses are mixed, but filtered on their pages.
I created different templates, to make it easy to work with.

## User Stories

There is a project in GitHub, linked to Mindful_Rise repository
https://github.com/users/Christina5P/projects/5/views/1

In the backlog I worked with different stories/task and moved them in steps until they where done.

I created user stories with acceptance critera to get MVP.


I also made some tasks



## Mindmap
![Screenshot of Mindmap](static/img_readme/mindmap.png)


link to my mindmap: https://miro.com/app/board/uXjVK1IKqsk=/

## Relationship diagram ERD
![Screenshot of ERD](static/img_readme/erd.png)

Link: https://drive.google.com/file/d/1SYwaMzGs6PuOuEuA6Yi4T2Q0p8dvmSvd/view?usp=sharing

## Wireframes

Wireframe is created in https://balsamiq.cloud/srvezeo/phn02iw/r3EBE
Home page:
![Screenshot of Home](static/img_readme/wireframehome.png)

Blog page:
![Screenshot of Blog](static/img_readme/wireframeblog.png)

Courses:
![Screenshot of Courses](static/img_readme/wireframecourses.png)

Blogpost:
![Screenshot of Post](static/img_readme/wireframedetail.png)

## CRUD 

In use the operation CRUD :

Create - Users can create comments and like posts
       - User can register an account
Read - Users can read the homepage, blogpost and Course material
Update- Users can edit their own comments or unlike their likes if they have created an account and are logged in.
Delete - Users can delete their own comments if  they have created an account and are logged in.

# Features

## Home Page

Homepage is the first impression and decides if you can catch the users interest.
My Homepage includes halfcarousel with pictures for people who is interested to invest in yourself.
Under  the pictures, I have a short resume of myself to get close to users and  build confiedence.
I also put in a picture of myself to strengthen the connection between me and interested users.

## Blog Page
Blog page is for all visitors and if you havn´t signed up, you can use it for readable.
In blog page, I would like to have a clean and calm style.
You would be able to choose a category you are interested in and you should see on the buttons which choice you have done.
I made that with a calm headlight color.
It also starts with "All Categories" button, so its clear and easy too navigate.
I also implemented a free text search bar (check of containing letters ) for a blog by category. And you have a clear button to quickly navigate to all posts and get easy to make searches.
When you open  a post, you see a button to quickly come back to the index again.

If you find an interersting post, you have an option to share it in social media below the posts.

You have to be loggedd in to like or comment a post, in a easy way.
As an admin, it should be easy to approve comments, so you have a filter choice and can approve multiple comments at same time.
You are also able to edit or delete your comment and receive alerts of update or a flag if you are sure that you want to delete a post.
There is also a vounter of likes and comments.

If there´s no post in a category, you get a message,so you understand that there is no published posts.

## Courses
There is also a page for courses.
I want that page to be more exclusive and is only for members.
When you enter this page as logged in, you welcome with a message.
You also have the course material under the picture with the message.

If you´re not signed in, you´ll se a form in the center of the page with links to log in or sign up form.
The course material will not be able for unauthorized users and you will not see them.
 

## Nav Bar

There is a navbar on top of page.
Its the same information, but it changes color when you move to another page, too keep the contrast.
At right you can see if you are logged in or not.
If you are logged in, you have a "Logout" option and if you are not logged in, there is a "Register" and "Login" option instead.
It´s too keep you informed of your status.

## Footer

There is links to social media in footer and a copyright text

![Screenshot of footer](static/img_readme/footer.png)

## Register section

I have a register section from Django allauth, there you can register with a username and password.
The sign up button is styled with MDB.

## 404 error
I have included an 404-page for more personal interaction and more clear you still are in Mindful Rise community, but there is an error. From this page, its easy to go back with a link.  

![Screenshot of footer](static/img_readme/404error.png)

## Favicon
I created a favicon that is a logo in head, customized to my blogsite

![Screenshot of footer](static/img_readme/favicon.png)

## Setting up workspace

* Run this command to install django:
 pip3 install 'django<4'  

* Next, install these libraries: 
pip3 install dj_database_url psycopg2
pip3 install dj3-cloudinary-storage

* Create a requirements.txt file to save all the installed libraries:
pip3 freeze --local > requirements.txt

* You need to create a project and add my apps:
django-admin startproject mindfulgrowth
python3 manage.py startapp blog
Remember to add your apps in to the 'INSTALLED_APPS' in setting.py

* Add your DB and CLoudinary library to your project:
 Copy the DATABASE_URL
 create a new file manual with name: env.py
 This file need to be placed in the project cataloge
 Import the os library:
 import os
Set environment variables:
os.environ.setdefault(
    "DATABASE_URL", "postgres://uottaphddte:1ZsY6k60KNPN@ep-gentle-mountain-a23bxz6h.eu-central-1.aws.neon.tech/vocal_moan_poem_31644")
 
os.environ.setdefault(
    "SECRET_KEY", "django-insecure-%s0!8rr$!pbkcomh1bmeybs4nldjtws=8n%pffttkm%(-nrrma")    

os.environ.setdefault(
    "CLOUDINARY_URL", "cloudinary://618768418781469:Q8KVKcOdIzeC4kCaKocmseNCHmM@dvh69l0yv")

os.environ["SECRET_KEY"] = "mysecretkey"

Add the env.py-file to the setting.py file with commando in the file:
import env

You also need to put this in the setting.py file under :

ALLOWED_HOSTS = ['rise-f0e0db837715.herokuapp.com',
    '8000-christina5p-mindfulrise-hzzi4mxch9a.ws.codeinstitute-ide.net',
    '8080-christina5p-mindfulrise-hzzi4mxch9a.ws.codeinstitute-ide.net']

CSRF_TRUSTED_ORIGINS = [
    "https://*8000-christina5p-mindfulrise-hzzi4mxch9a.ws.codeinstitute-ide.net",
    "https://*mindfulrise-hzzi4mxch9a.herokuapp.com" 
]

Dont forget to add apps and libraries in 

INSTALLED_APPS = []

Before deploying on heroku make sure: DEBUG = False

* Create 3 new folders on the root directory: media, static, templates

* Create Procfile (needed for Heroku) on the root directory and inside the file type:
web: gunicorn basic_mind.wsgi
hint: It´s important to spell Procfile with a capital

## Design

I have used MBD for design and a carousel of pictures at home page.
I want it to be clean and calm too read and use and buttons is indicatuve.
Blogpage for unauthorized users and courses for signed up users are separated, to make it clean.

I didnt install anything from MDB since I used CDN installment. It is the easiest way, since you only need to add MDB:s link tap in <head> in your base.html 

## Testing
* Validating Test
* Python Test
* Manual Test

I have tested "forgot password" by add a backend email in settings.
## Bugs

### Fixed Bugs

* I struggle with the post views on blogsite. 
I wanted to have a blogcard with header and the first 100 letters to show and a "Read"button to open the full view.
When I used syntax "Slice" it showed the first syntax signs instead of the content.
With tutorhelp, I changed it to "safe" but then I only could see the header.
I try to solve it by going through the HTML, models, views and url files.
Unfortunaly I changed posts to post in view function and the result was that I losed the blogcontent and could only see the text 
No published posts.

I fixed it and tried to back the other changes I tried out on the way.
I skip the function with slice, since I got told it need more filter for that and take it as a feature scoop.

* Buttons for edit and delete posts are inactive.
I thought I missed something in the model och views, so I changed thr relationships between files, created separate edit-template 
and read tutorials, looked at walk through, asked for help from GPR monica.im.
After a while, I realized from inspection in browswer, that it was something with my js that didn´t worked.
I had missed to refer to static/comment.js in base.html and that was a problemsolver. 

* You could only see the navbar on home page 
I tried to inspect the navbar onother pages and check so I had block page on right spot
I also tried to put in a navbar on the other pages, but you couldn`t see anything.
Then I realized it was a stylingproblem, wich came from bootstrap:
<nav class="navbar navbar-expand-lg navbar-dark d-none d-lg-block" style="z-index: 2000;">
I had only carousel on Home page, so it just showed on that page.
I resolved it by make a rule to use it if the page had carousel or not:
  <nav class="navbar navbar-expand-lg {% if has_carousel %}navbar-dark{% else %}navbar-light{% endif %} d-none d-lg-block" style="z-index: 2000;">

* Next problem with navbar was the text "Welcome..." was dark, even if the rest of the navbar was white and the arrows to turn over where multiple
At first I fixed it by my own styling i style.css, but later on I found out that I had missed to put in 
 .navbar .nav-link {
      color: #fff !important;
    } in the template.
To fix the muliple arrows, I found out that it doesn´t work wih both bootstrap and MDB, so I had to remove all the bootstrap links.
Then I was back to the "Welcome-issue" and resolved it by an own styleshhet for home.html

* I tried to style register and login page, but result was that I couldn´t access them.
My tries to resolve it, I got through every file and url. I compared my reqirements with other works and installed missing auth compenents, whitenoise.
I moved the account folder to the root template.
I created an account/base.html to structure the codes, so you don´t have to repeat the codes in every template.
What I missed was that I used  block content in onte template and block page_content in another, so they didn´t match.
I got help from tutor to find out, so when I chenged, everything was working well.

* Problem with migration of category model 
I add and changed the logic of categories and search in models. When I migrated, I got an error because of existing posts without category slug. Step 1 was to try to make a migrationfile to change. When it didn´t work, I deleted the last file and tried to migrate again. Mu third tried was to delete the new category model and to prevent the clash and migrate again.
When nothing of that worked, I got tutorhelp, but the only suggestion was to delete the db and recover with a new.
I wasn´t happy with that suggestion, since I worked with the db in several weeks.
In the end, it appeared that it was a general db problem, so when that was resolved, I could reach my db, erase all the categories of posts and migrate my new function and everything worked!

* Coursematerial was shown in blog index.
Since I have the same database for blogpost and coursematerial, I made a tag "is_course_material" so I could manipulate with an exclude to get those posts be filtered out and just shown in the Courses page.
It didn´t work and I guess it had something to "ManytoMany" relationship.
I made a walkaround by get a new category=coursemateral and tagged those post with that category as well.
Then I could do a filter of that category to exklude them in category list and search.

### Unfixed Bugs

* I get an errormessage in browser/inspect 
It has been there through the project and I think it has something with the MDB modal to do.
It doesn´t effect any functions and I tried to ger rid of it by mark out different functions, but can´t diagnos how to solve it.
What I tried:
- mark out different functions to see if I still get error.
- check compatiblebetween different versions
- Tutorhelp

It still a unfixed bug, since it doesn´t effect something in my project.

![Screenshot of Bug](static/img_readme/bug.png)

* Showing course material in blog post when choosing category 
I have make a filter function that blog index should never view post "is course_material" and it works with all blog posts, but if you filter of one category, it views anyway.



## Technologies
*Python - Language of this project
* Javascript
* JQuery
* HTML
* CSS
* Django - 
* Cloudinary (for external image management)
* Code Institute Postgres Database server for PostgreSQL 
* MDB
* Github - Save the project in a repository
* Heroku - Deploy it to a public website

### Package
* Whitenoise
* Summernote
* Cloudinary

# Deployment

For deploying, I use the Heroku app.
At first, you commit everything to GitHub.
In Heroku, you set up an app for the project and deploy the changes you make to the public site.



## Heroku
You connect the app to your repository in GitHub with the same name.
I chose to make a manual deployment, so I can see that everything goes ok and have control of my project.

You need to create an app for your project in Heroku.
In settings you also need to fill in the URL:s in Config Var
![Screenshot of settings](static/img_readme/herokusettings.png)

![Screenshot of deployment1](static/img_readme/configvars.png)

After that you go to Herokus deployment section 
![Screenshot of deployment1](static/img_readme/herokudeploy1.png)

Scroll down to the bottom and click the "deploy button

![Screenshot of deployment1](static/img_readme/herokudeploy.png)

On the top at right hand side, you can click "open app" to see public site.
If there is any error, you can find the logs if you click "more" button.

![Screenshot of app](static/img_readme/herokuapp.png)

## Git Hub / Gitpod
I created a repository in Git Hub and connected a project to the repository.
In the project, I worked with the canban and created the user stories there.
From Gitpod, I pushed my changes to GitHub with the commands 

When I add, deleated or changed anything, I committed them back to GitHub using the following commands in the codespace terminal: Git add .
Git commit -m"text"
Git push

To run a backend application in Gitpods terminal,
type: python3 manage.py runserver 

To see and implement changes in Django, type:
python3 manage.py makemigrations
pyhton3 manage.py migrate

## How to Fork
To fork this repository, click the "Fork" button at the top right corner of the main repository page. On the "Create a Fork" page, you can change the name of the repo if desired. Check the box if you want to copy the main branch or multiple branches (main is selected by default). Then, create the fork.

## How to Clone (An alternative to fork)
To clone the repository, you create a copy in your repository (with all files and history).
This creates a remote link to the original repo, allowing you to work in your copy and push changes back to the original.
Open your repo and click the green "Code" button on the right-hand side. The easiest way is to open it with GitHub Desktop.

You can read more information on cloning at the GitHub : https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

## Font
* Roboto

## Databas
CI Database https://dbs.ci-dbs.net/

## Framework 
* Django

## Icons

* https://www.flaticon.com/free-icons/author
* https://www.flaticon.com/free-icon/philosophy_4576683?term=mindfulness&page=1&position=3&origin=tag&related_id=4576683


# Media

* https://www.youtube.com/watch?v=et55Kc_G-1o
* https://deepeddypsychotherapy.com/self-esteem/
* https://www.verywellhealth.com/what-is-self-esteem-5205044
* https://www.yin-yoga.se/yinyoga/
* https://www.masterclass.com/articles/how-to-value-yourself
* https://www.shutterstock.com/



## Images
* https://deepeddypsychotherapy.com/self-esteem/
* https://www.wfla.com/bloom-tampa-bay/unlocking-your-inner-confidence-the-power-of-self-esteem/
* https://www.yin-yoga.se/yinyoga/
* https://www.psychalive.org/self-worth/


# Acknowledgement

### for tutoring Django:
* https://youtube.com/playlist?list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&si=9t7TdLJVAM9BM9Ga
* https://realpython.com/build-a-blog-from-scratch-django/#set-up-the-development-environment 
* https://www.youtube.com/watch?v=ZUiTiUj-tZw
* https://www.youtube.com/watch?v=PXqRPqDjDgc
* https://dev.to/radualexandrub/how-to-add-like-unlike-button-to-your-django-blog-5gkg
* https://medium.com/@peter.bulyaki/ho-to-edit-or-delete-your-comments-responses-on-medium-com-in-2019-2a87eb8da79b
* https://www.youtube.com/watch?app=desktop&v=PXqRPqDjDgc* 'monica.im GPT chat to help explain where to put url and meaning of django functions.
* ChatGPT.com to help me with adding category search button and clear search button with MDB style,
Suggestion to create excerpt automatically sav
* https://www.w3schools.com/howto/howto_website_static.asp

### Inspiration of blogs and teaching equpment
* https://www.progressme.se/sv
* https://www.everydayhealth.com/mindfulness/

### Tutoring help
### Help and discusses with mu studyfellow Josefin Dahlquist

