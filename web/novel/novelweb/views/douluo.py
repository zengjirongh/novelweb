from django.shortcuts import redirect, render
from novelweb import models


def novel_cover(request):
    return render(request, "novel_cover.html")


def novel_douluo(requeest):
    queryset = models.douluo.objects.all().order_by("-id")
    res = {
        "queryset": queryset
    }
    return render(requeest, "novel_douluo.html", res)


def novel_douluo_page(request, nid):
    obj_queryset = models.douluo.objects.filter(id=nid).first()
    res = {
        "obj_queryset": obj_queryset
    }

    return render(request, "novel__douluo_page.html", res)
