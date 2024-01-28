from django.shortcuts import render


def service(request):
    return render(request, 'service.html', context={})


def service_finaly(request):
    return render(request, 'serviceFinally.html', context={})


def popup(request):
    return render(request, 'popup.html', context={})


def profile(request):
    return render(request, 'admin.html', context={})


def notes(request):
    return render(request, 'notes.html', context={})
