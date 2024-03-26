from django.shortcuts import render
from django.http import HttpResponse
import json
from django.shortcuts import render


# Create your views here.
def hello_world(request):
    thisset = {"apple", "banana", "cherry"}
    thisdict = {
        "brand": "Porsche",
        "model": "911",
        "year": 1963
    }
    json_str = json.dumps(thisdict)
    # return HttpResponse("Hello, World!!!!")
    # html_content = """
    # <!DOCTYPE html>
    # <html>
    # <head>
    #     <title>My Page</title>
    # </head>
    # <body>
    #     <h1>Hello, World!</h1>
    # </body>
    # </html>
    # """
    # return HttpResponse(html_content)

    # 准备要传递给模板的上下文数据
    context = {
        'name': 'John Doe',
        'greeting': 'Hello there!',
        'items': ['apple', 'banana', 'cherry'],
    }

    # 使用 'my_template.html' 模板和上下文数据渲染页面
    return render(request, 'my_template.html', context)

# python manage.py runserver

