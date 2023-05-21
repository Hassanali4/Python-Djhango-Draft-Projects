#I have craeted this File - Hassan
from django.http import HttpResponse
from django.shortcuts import render

#Video 6 & 7 Personal Nevigator Code Practice
# def index(request):
#     s = '''<h1>Nevigation Bar<br></h1><a target="blank" href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9"> Django With Harry Bhai</a><br>
#             <a target="blank" href="https://fmovies.to/home"> Fmovies</a><br>
#             <a target="blank" href="https://www.behance.net/"> Behance</a><br>
#             <a target="blank" href="https://getintopc.com/"> GetintoPC</a><br>'''
#     return HttpResponse(s)
#
# def about(request):
#     return HttpResponse("About Hassan Bhai")

def index(request):
         d = {'name':"Hassan Ali",'place':'Pakistan'}
         return render(request,'index.html', d)
         #return HttpResponse('''<h1>Home</h1><br> <a href="http://127.0.0.1:8000/removepunc"> removepunc</a><br> <a href="http://127.0.0.1:8000/capitalizefirst"> capitalizefirst</a><br> <a href="http://127.0.0.1:8000/newlineremove"> newlineremove</a><br> <a href="http://127.0.0.1:8000/spaceremove"> spaceremove</a><br> <a href="http://127.0.0.1:8000/charcount"> charcount</a><br>''')

def removepunc(request):
    return HttpResponse('''<h1>removepunc</h1><a href="http://127.0.0.1:8000/"> Back</a><br>''')

def capfirst(request):
    return HttpResponse('''<h1>capitalizefirst</h1><a href="http://127.0.0.1:8000/"> Back</a><br>''')

def newlineremove(request):
    return HttpResponse('''<h1>newlineremove</h1><a href="http://127.0.0.1:8000/"> Back</a><br>''')

def spaceremove(request):
    return HttpResponse('''<h1>spaceremove</h1><a href="http://127.0.0.1:8000/"> Back</a><br>''')

def charcount(request):
    return HttpResponse('''<h1>charcount</h1><a href="http://127.0.0.1:8000/"> Back</a><br>''')