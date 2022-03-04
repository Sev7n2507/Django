from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect


from .models import Question
from django.utils import timezone
from .forms import QuestionForm


def index(request):

    return render(request, 'firstApp/index.html')


def create_question(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "firstApp/create_question.html", context)


def list_question(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Question.objects.all()

    return render(request, "firstApp/list_question.html", context)


def detail_question(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = Question.objects.get(id=id)

    return render(request, "firstApp/detail_question.html", context)


def update_question(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Question, id=id)

    # pass the object as instance in form
    form = QuestionForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/firstApp/view/")

    # add form dictionary to context
    context["form"] = form

    return render(request, "firstApp/update_question.html", context)


def delete_question(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Question, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/firstApp/view/")

    return render(request, "firstApp/delete_question.html", context)
