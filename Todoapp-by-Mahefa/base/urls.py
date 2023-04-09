from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login_page'),
    path('register/', RegisterPage.as_view(), name='register_page'),
    path('logout/', LogoutView.as_view(next_page='login_page'), name='logout'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('add-new-task/', TaskCreate.as_view(), name='add_task'),
    path('edit-task/<int:pk>', TaskUpdate.as_view(), name='edit_task'),
    path('delete-task/<int:pk>', DeleteView.as_view(), name='delete_task')
]
