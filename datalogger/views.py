from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from datalogger.models import UploadFileForm

def handle_uploaded_file(f):
  destination = open('log', 'wb+')
  for chunk in f.chunks():
    destination.write(chunk)
  destination.close()

@csrf_protect
def upload_file(request, phone_id):
  if request.method == 'POST':
    ufile = '/home/lsm5/log'
    form = UploadFileForm(request.POST, ufile)
    if form.is_valid():
      handle_uploaded_file(ufile)
      return HttpResponse("success")
  else:
    form = UploadFileForm()
    return render_to_response('datalogger.html', {'form': form}, context_instance=RequestContext(request))
