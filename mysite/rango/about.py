from django.shortcuts import render

from django.http import HttpResponse


def about(request):
    if request.session.test_cookie_worked():
        print("TEST COOKIE WORKED!")
    request.session.delete_test_cookie()

    return render(request, 'rango/about.html')
