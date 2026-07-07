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