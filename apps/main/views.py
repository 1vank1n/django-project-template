# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
# from django.core import serializers
# from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseNotFound
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.core.mail import send_mail, EmailMessage

# from .models import Example
# from .forms import ExampleForm

def index(request, template):
    return render(request, template, locals())

# def sendemail(topic, content):
#     subject, from_email = topic, 'noreply@il-studio.ru'
#     to = ['ivan@il-studio.ru',]
#     msg = EmailMessage(subject, content, from_email, to)
#     msg.content_subtype = "html"  # Main content is now text/html
#     msg.send()
#     return True


# def example(request, template):
#     example_list = Example.objects.filter(status=True).order_by('?')[:3]
#     example_list_json = serializers.serialize("json", example_list, fields=('author', 'text', 'id', 'link'))

#     if request.method == 'POST':
#         form = ExampleForm(request.POST or None)

#         if form.is_valid():
#             i = form.save(commit=False)
#             i.save()

#             topic = u'Topic, №%i' % i.id
#             content = u"""
#             <!DOCTYPE HTML>
#             <html>
#                 <head></head>
#                 <body>
#                     <table>
#                         <tr><td>Example:</td><td>%s</td></tr>
#                     </table>
#                 </body>
#             </html>
#             """ % (i.example)
#             sendemail(topic, content)

#     paginator = Paginator(example_list, 8)
#     page = request.GET.get('page')

#     try:
#         example_list = paginator.page(page)

#     except PageNotAnInteger:
#         example_list = paginator.page(1)

#     except EmptyPage:
#         example_list = paginator.page(paginator.num_pages)

#     paginator.pages_range = range(1,int(paginator.num_pages)+1)

#     return render(request, template, locals())
