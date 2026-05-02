from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
nav = """
    <nav>
        <a href='/'>Home</a> |
        <a href='/about/'>About</a> |
        <a href='/skills/'>Skills</a> |
        <a href='/hobbies/'>Hobbies</a>
    </nav>
    <hr>
"""

def home(request):
    user_name = "Buddy"
    lesson_num = 18
    progress = 95.5
    content = f"""
        <h1>Home Page</h1>
        <h1>Welcome to Class</h1>
        <p>This is the first page of our Django assignment.</p>
        <ul>
            <li>User: {user_name}<li>
            <li>Class: {lesson_num}<li>
            <li>Progress: {progress}%<li>
        </ul>
    """
    return HttpResponse(nav + content)

def about(request):
    my_list = ["Django", 2024, True, 3.14, "ComIT", "Success"]
    items = "".join([f"<li>Item: {x}</li>" for x in my_list])
    content = f"""
        <h1>About Page</h1>
        <h2>Learning List</h2>
        <p>Here is a mixed-type list of length 6.</p>
        <ol>{items}</o1>
    """
    return HttpResponse(nav + content)

def skills(request):
    my_dict = {"Language": "Python", "Framework": "Django", "Level": 1, "Status": "Learning", "Fun": True}
    items = "".join([f"<li>{k}: {v}</li>" for k, v in my_dict.items()])
    content = f"""
        <h1>Skills Page</h1>
        <h2>Current Skills</h2>
        <p>A dictionary showing 5 key-value pairs.</p>
        <ul>{items}</ul>
    """
    return HttpResponse(nav + content)

def hobbies(request):
    content = """
        <h1>Hobbies Page</h1>
        <h2>What I do for fun</h2>
        <p>Coding and learning new frameworks with my Buddy!</p>
    """
    return HttpResponse(nav + content)
