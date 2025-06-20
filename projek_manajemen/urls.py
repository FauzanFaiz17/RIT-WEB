from django.urls import path
from . import views

urlpatterns = [
    path('projek/', views.daftar_project, name='daftar_projek'),
    path('buat/', views.buat_project, name='buat_projek'),
    path('projek/<int:project_id>/proses/', views.projek_proses, name='projek_proses'),
    path('projek/<int:project_id>/edit/', views.edit_projek, name='edit_projek'),
    path('projek/<int:project_id>/hapus/', views.hapus_projek, name='hapus_projek'),
    path('projek/<int:project_id>/buat-task/', views.buat_task, name='buat_task'),
    path('projek/<int:project_id>/edit-task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('projek/<int:project_id>/hapus-task/<int:task_id>/', views.hapus_task, name='hapus_task'),
    path('projek/<int:project_id>/buat-subtask/<int:task_id>/', views.buat_subtask, name='buat_subtask'),
    path('projek/<int:project_id>/task/<int:task_id>/edit-subtask/<int:subtask_id>/', views.edit_subtask, name='edit_subtask'),
    path('projek/<int:project_id>/task/<int:task_id>/hapus-subtask/<int:subtask_id>/', views.hapus_subtask, name='hapus_subtask'),
    path('projek/<int:project_id>/export-pdf/', views.export_pdf_projek, name='export_pdf_projek'),
]
