"""
To render html pages
"""
from django.http import HttpResponse

HTML_STRING = """
<h1> Hello from django 3.2 </h1>
"""

def home(request):
    """
    Return a response
    """
    return HttpResponse(HTML_STRING)