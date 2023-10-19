from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',index, name='index'),
    path('project_page/',project_page,name='project_page'),
    path("comment/<int:comid>/",CommentView, name="comment"),
    path('blog/',blog, name='blog'),
    path('login/',Userlogin, name='login'),
    path('logout/',UserLogout, name='logout'),
    path('sign/',sign, name='sign'),
    path('section/',Sectionview, name='section'),
    path('editprofil/<int:editid>',EditProfilView, name='editprofil'),
    path('bio/',bioView, name='bio'),
    path('sign/',sign, name='sign_up'),
    path('project/<int:prj_id>',projectview, name='project'),
    path('edit_project/<int:edit_id>/',EditProjectView, name='edit_project'),
    path('delete_project/<int:delete_id>/',DeleteProjectView, name='delete_project'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)