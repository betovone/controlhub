FIBONACCI REST APPLICATION

Developed in Django 

Install dependences:
pip install -r requeriments.txt

Endpoint:
/api/fibonacci/<int:index>/

Running Django Test:
python manage.py test

Running Django App:
python manage.py runserver


Future optimizations:
-   Save the results in cache with json format. 
    Example: {'index': 'result', 'other_index': 'result', ... }
-   When the user makes the request, the application must first 
    consult the cache and if the index is not there, perform 
    the Fibonacci function and cache the index and result.

