from django.http import JsonResponse, request
from django.shortcuts import render
from django.template import loader

from kosu.models import Man_Hours, Position_Master, Project_Master

# Create your views here.


def index(request):

    context = dict()
    project_id = request.GET["projectId"]
    context["projectId"] = project_id
    project_data = list()
    projects = Project_Master.objects.all()
    for project in projects:
        # project_data.append(kosu.user.user.username + " " + str(kosu.hour))
        project_data.append(project.__dict__)
        print(project.__dict__)

    project = Project_Master.objects.get(pk=project_id)
    project_info = dict()
    project_info["name"] = project.name
    project_info["order"] = project.order
    project_info["amount"] = project.order_amount
    project_info["start"] = project.start
    project_info["end"] = project.end
    context["projectInfo"] = project_info

    project_kosu = Man_Hours.objects.filter(project_id=project_id)
    context["kosu"] = project_kosu

    position_data = list()
    positions = Position_Master.objects.all()
    for position in positions:
        print(position.position)
        position_data.append(position.position + " " + str(position.unit_price))

    template = loader.get_template("kosu/index.html")
    # return JsonResponse({"kosu": project_data, "position": position_data})
    context["hoge"] = "hoge"
    context["project_data"] = project_data
    context["positions"] = position_data
    return render(request, "kosu/index.html", context)
    # return HttpResponse({"kosu": kosu_data, "position": position_data})
