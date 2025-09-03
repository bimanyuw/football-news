from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406397984',
        'name': 'Febrian Abimanyu Wijanarko',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)

# Create your views here.
