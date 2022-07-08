from django.shortcuts import redirect, render
from novelweb import models


def novel_tsxk(requeest):
    queryset = models.tsxk.objects.all()
    res = {
        "queryset": queryset
    }
    return render(requeest, "novel_txsk.html", res)


def novel_tsxk_page(request, nid):
    obj_queryset = models.tsxk.objects.filter(id=nid).first()
    res = {
        "obj_queryset": obj_queryset
    }

    return render(request, "novel__tsxk_page.html", res)
