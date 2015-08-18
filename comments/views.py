from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from react.render import render_component
import os
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse

comments = []
# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")

    rendered = render_component(
        os.path.join(os.getcwd(), 'static', 'js', 'CommentBox.jsx'),
        {
            'comments': comments,
            'url': '/comments/comment/',
        },
        to_static_markup=True,
    )

    return render_to_response('index.html', {"rendered": rendered})

@csrf_exempt
def comment(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    comments.append({
        'author': request.POST['author'],
        'comment_text': request.POST['comment_text'],
    })
    # return HttpResponseRedirect('/comments')
    return HttpResponseRedirect(reverse('comments:index'));
