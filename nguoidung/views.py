from django.contrib import auth
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import datetime
# import icecream 
from icecream import ic
#from newdjangoproject4.nguoidung.models import thongtinnguoidung
from nguoidung.forms import DangKy
from django.http import HttpResponse, StreamingHttpResponse
from django.db import IntegrityError, reset_queries
from nguoidung.models import RoomChat, TinNhan
from django.contrib.auth import logout
# Create your views here.

def homepage_view(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        return render(
            request,
            'PreLoginPage.html',
            {
                'now': datetime.datetime.now(),
            }
        )

@login_required(login_url='/dang_nhap/')
def userhomepage_view(request):
    return render(
        request,
        'HomePage.html',
        {
            'now': datetime.datetime.now(),
        }
    )
    
@login_required(login_url='/dang_nhap/')
def dangxuat(request):
    logout(request)
    return redirect('/')
    

def dangky(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method == 'POST':
            form1 = DangKy(request.POST)
            if form1.is_valid():
                form1.save()
                return redirect('/dang_nhap')
        else:
            form1 = DangKy()
        return render(
            request,
            'SignupPage.html',
            {
                'form1': form1,
            }   
        )

def termofservice_view(request):
    return render(request, 'TermsofService.html')

# @login_required(login_url='/dang_nhap/')
# def phongchat(request):
#     return render(request, 'new.html')

# @login_required(login_url='/dang_nhap/')
# def phongchatchinh(request, room_name):
#     #return render(request, 'new1.html', {'room_name': RoomChat.RoomID, 'username': User})
#     username = request.GET.get('username', 'Anonymous')
#     return render(request, 'new1.html', {'room_name': room_name, 'username': username})

@login_required(login_url='/dang_nhap/')
def phongchatchinh(request, room_name):
    room_detail = RoomChat.objects.get(RoomID=room_name)
    # room_detail.RoomIDAPI = request.POST['']
    # room_detail.save();
    return render(request, 'RoomChat.html', {
        'room_name': room_name,
        #'room_detail': room_detail,
    })
    

@login_required(login_url='/dang_nhap/')
def checkview(request):
    room = request.POST['room_name']
    
    current_user = request.user
    
    if RoomChat.objects.filter(RoomID=room):
        return redirect('/'+room+'/?username='+str(current_user))
    else:
        newroom = RoomChat.objects.create(RoomID=room)
        newroom.save()
        return redirect('/'+room+'/?username='+str(current_user))
    
@login_required(login_url='/dang_nhap/')
def send(request):
    message = request.POST['message']
    messager = request.POST['username']
    roomid = request.POST['room_id']
    
    new_message = TinNhan.objects.create(room=roomid, messenger=messager, noidung=message)
    new_message.save()
    return HttpResponse('Tin nhan da duoc gui di!')

@login_required(login_url='/dang_nhap/')
def getMessages(request, room_name):
    messages = TinNhan.objects.filter(room=room_name)
    return JsonResponse({"messages": list(messages.values())})

# @login_required(login_url='/dang_nhap/')
# def Stream(request):
#     cap = cv2.VideoCapture(0) 

#     while True:
#         ret, frame = cap.read()

#         if not ret:
#             print("Error: failed to capture image")
#             break

#         cv2.imwrite('demo.jpg', frame)
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + open('demo.jpg', 'rb').read() + b'\r\n')

# def video_feed(request):
#     return StreamingHttpResponse(Stream(), content_type='multipart/x-mixed-replace; boundary=frame')
