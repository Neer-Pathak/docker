from django import urls
from oktest.views import serve_html


urlpatterns = [
    urls.path(
        "try/",
        serve_html,
        name="ok"
    )
    
]
