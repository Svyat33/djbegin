from django.shortcuts import render


def main_news(request):
    from djbegin.settings import SECRET_KEY
    return render(request, "news/news.html", {"secret": SECRET_KEY})