from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProjectForm, TaskForm, SubtaskForm
from .models import Project, Task, Subtask
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def daftar_project(request):
    projek = Project.objects.all()
    return render(request, 'projek_manajemen/daftar_projek.html', {
        'projek': projek
    })

def buat_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Projek berhasil dibuat.")
            return redirect('daftar_projek')  # Nanti kita buat halaman ini
    else:
        form = ProjectForm()

    return render(request, 'projek_manajemen/buat_projek.html', {
        'form': form
    })

def edit_projek(request, project_id):
    projek = Project.objects.get(id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=projek)
        if form.is_valid():
            form.save()
            messages.success(request, "Projek berhasil diperbarui.")
            return redirect('daftar_projek')
    else:
        form = ProjectForm(instance=projek)

    return render(request, 'projek_manajemen/edit_projek.html', {
        'form': form,
    })

def hapus_projek(request, project_id):
    projek = Project.objects.get(id=project_id)
    if request.method == 'POST':
        projek.delete()
        messages.success(request, "Projek berhasil dihapus.")
        return redirect('daftar_projek')

    return render(request, 'projek_manajemen/konfirmasi_hapus.html', {
        'projek': projek
    })

def projek_proses(request, project_id):
    projek = Project.objects.get(id=project_id)
    tasks = Task.objects.filter(project=projek).prefetch_related('subtasks')
    return render(request, 'projek_manajemen/projek_proses.html', {
        'projek': projek,
        'tasks': tasks,
    })


def buat_task(request, project_id):
    projek = Project.objects.get(id=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = projek
            task.save()
            messages.success(request, "Tugas berhasil dibuat.")
            return redirect('projek_proses', project_id=project_id)
    else:
        form = TaskForm()

    return render(request, 'projek_manajemen/buat_task.html', {
        'form': form,
        'projek': projek
    })

def edit_task(request, project_id, task_id):
    projek = Project.objects.get(id=project_id)
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Tugas berhasil diperbarui.")
            return redirect('projek_proses', project_id=project_id)
    else:
        form = TaskForm(instance=task)

    return render(request, 'projek_manajemen/edit_task.html', {
        'form': form,
        'projek': projek,
        'task': task
    })

def hapus_task(request, project_id, task_id):
    projek = Project.objects.get(id=project_id)
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        messages.success(request, "Tugas berhasil dihapus.")
        return redirect('projek_proses', project_id=project_id)

    return render(request, 'projek_manajemen/projek_proses.html', {
        'projek': projek,
        'task': task
    })

def buat_subtask(request, project_id, task_id):
    projek = Project.objects.get(id=project_id)
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = SubtaskForm(request.POST)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.task = task  # Assuming you have a field for parent task
            subtask.project = projek
            subtask.save()
            messages.success(request, "Subtask berhasil dibuat.")
            return redirect('projek_proses', project_id=project_id)
    else:
        form = SubtaskForm()

    return render(request, 'projek_manajemen/buat_subtask.html', {
        'form': form,
        'projek': projek,
        'task': task
    })

def edit_subtask(request, project_id, task_id, subtask_id):
    projek = Project.objects.get(id=project_id)
    task = Task.objects.get(id=task_id)
    subtask = Subtask.objects.get(id=subtask_id)
    if request.method == 'POST':
        form = SubtaskForm(request.POST, instance=subtask)
        if form.is_valid():
            form.save()
            messages.success(request, "Subtask berhasil diperbarui.")
            return redirect('projek_proses', project_id=project_id)
    else:
        form = SubtaskForm(instance=subtask)

    return render(request, 'projek_manajemen/edit_subtask.html', {
        'form': form,
        'projek': projek,
        'task': task,
        'subtask': subtask
    })

def hapus_subtask(request, project_id, task_id, subtask_id):
    projek = Project.objects.get(id=project_id)
    task = Task.objects.get(id=task_id)
    subtask = Subtask.objects.get(id=subtask_id)
    if request.method == 'POST':
        subtask.delete()
        messages.success(request, "Subtask berhasil dihapus.")
        return redirect('projek_proses', project_id=project_id)

    return render(request, 'projek_manajemen/konfirmasi_hapus_subtask.html', {
        'projek': projek,
        'task': task,
        'subtask': subtask
    })

def export_pdf_projek(request, project_id):
    projek = get_object_or_404(Project, id=project_id)
    tasks = Task.objects.filter(project=projek).prefetch_related('subtasks')

    template_path = 'projek_manajemen/export_pdf.html'
    context = {'projek': projek, 'tasks': tasks}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="projek_{projek.nama}.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Terjadi kesalahan saat generate PDF')
    return response
