from django.urls import path, include

urlpatterns =[
    path('tasks/', include('task.urls')),
    path('accounts/', include('accounts.urls')),
    path('requests/', include('request.urls'))
]