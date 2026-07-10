from django.shortcuts import render
from datetime import datetime
# Create your views here.
class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
def home (request):
        context={
            "name":"Laiba Nadeem",
            "age":25,
            "skill":["python","django","React"],
            "user":User("sara",30),
            "blog":{
                "title":"django template intro",
                "author":{
                    "name":"lain"
                },
                "content":"<b> This is bold </b>",
                "created_at": datetime(2025,8,18,10,30)
            },
            "empty_value":None,
        
        }
        return render(request, "blog/base.html", context)
def blog_details(request):
    post={
        "title":"My second template",
        "description":"Dango is a high level language",
        "author":None,
        "created_at":datetime(2026,7,8,6,40),
        "comments_count":5,
        "tags":["Django","php","jquery"],
        "price":100,
        "number":7
    }
    return render(request,"blog/filters.html",{"post":post} )
def  about_details(request):
    blogs=[
        {"title":"Django basics",
        "is_featured":True,
        "author":"John Doe"
        },
         {"title":"Django advance",
        "is_featured":False,
        "author":""
        },
         {"title":"Django Rest Famewwork",
        "is_featured":False,
        "author":"Jane"
        }
    ]
    context={
        "blogs":blogs,
        "today":datetime.now(),
        "html_code":"<h1>Weclome to My blog</h1>",
    }
    return render(request,"blog/conditions.html",context )