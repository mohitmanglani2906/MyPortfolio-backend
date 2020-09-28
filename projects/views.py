from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class UserProjects(APIView):
    def get(self, request):
        #https://api.github.com/users/mohitmanglani2906/repos
        output_json = {}
        output_list = []
        import requests
        import json
        r = requests.get("https://api.github.com/users/mohitmanglani2906/repos")
        projectsRepo = json.loads(r.text)
        for project in projectsRepo:
            if "name" in project and project["name"] and project["name"] not in ["Android-Samples","NPTEl-material-for-programming-data-structure-and-algoritham",
                                                                                 "OOPC-programmes-for-beginners",
                                                                                  "scf-config-repository" , "TeluskoLiveProject", "Women_Security"]:
                output_json["name"] = project["name"]

                if "description" in project and project["description"]:
                    output_json["description"] = project["description"]
                else:
                    output_json["description"] = ""

                if "html_url" in project and project["html_url"]:
                    output_json["html_url"] = project["html_url"]
                print(output_json)
                output_list.append(output_json)
                output_json = {}


        return Response({"success":True, "data": output_list})


