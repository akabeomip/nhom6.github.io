from django.contrib import admin

from nguoidung.models import RoomChat, TinNhan, thongtinnguoidung
# Register your models here.
@admin.register(RoomChat)
class RoomChatadmin(admin.ModelAdmin):
    list_display = ('RoomID',)
    
@admin.register(thongtinnguoidung)  
class thongtinnguoidungAdmin(admin.ModelAdmin):
    list_display = ('name', 'tennguoidung', 'nation', 'dateofbirth', 'email', 'gender', )
    search_fields = ('name', 'email',)
    list_filter = ('nation',)

@admin.register(TinNhan)
class TinNhanadmin(admin.ModelAdmin):
    list_display = ('room', 'messenger', 'noidung')