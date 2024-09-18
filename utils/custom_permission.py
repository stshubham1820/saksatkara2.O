# from rest_framework import permissions
# from utils.custom_response_handler import CustomResponseHandler
# from meeting.models import Meeting_Role
# import json

# class MeetingEDPermission(permissions.BasePermission):

#     def has_object_permission(self, request, obj):
        
#         if obj.organizer == request.user or request.user.is_superuser:
#             return True
#         return False
    
# class MeetingParticipantsPermission(permissions.BasePermission):

#     def has_object_permission(self, request, obj):
#         if obj.organizer == request.user or request.user.is_superuser or request.user in obj.sharing_list.all():
#             return True
#         return False
    
# class MeetingDetailsPermission(permissions.BasePermission):

#     def has_object_permission(self, request, obj):
#         if obj.organizer == request.user or request.user.is_superuser or request.user in obj.sharing_list.all():
#             return True
#         return False
    
# class MeetingSharingPermission(permissions.BasePermission):

#     def has_object_permission(self, request, obj):
#         if obj.organizer == request.user or request.user.is_superuser or request.user in obj.sharing_list.all():
#             return True
#         return False
    

# class MeetingObjectPermission(permissions.BasePermission):

#     def has_object_permission(self, request,view,obj):
#         if obj.organizer == request.user or request.user.is_superuser :
#             return True
#         elif request.user in obj.sharing_list.all():
#             data = Meeting_Role.objects.get(meeting_id=obj,user_id=request.user)
#             if data.role == "editor" or data.role == "viewer":
#                 return True
#             else :
#                 data = json.loads(data.permission)
#                 if view == 'meeting_summary' and (data.get('summary').get('view') or data.get('summary').get('edit')):
#                     return True
#                 if view == 'meeting_transcription' and (data.get('transcript').get('view') or data.get('transcript').get('edit')):
#                     return True
#                 if view == 'meeting_decision' and (data.get('discussion').get('view') or data.get('discussion').get('edit')):
#                     return True
#                 if view == 'recording' and (data.get('recording').get('view') or data.get('recording').get('edit')):
#                     return True
#                 if view == 'meeting_actionitem' and (data.get('action_item').get('view') or data.get('action_item').get('edit')):
#                     return True
#                 if view == 'meeting_attachment' and (data.get('attachment').get('view') or data.get('attachment').get('edit')):
#                     return True
#                 if view == 'meeting_notes' and (data.get('notes').get('view') or data.get('notes').get('edit')):
#                     return True
#                 if view == 'meeting_recap' and (data.get('recap').get('view') or data.get('recap').get('edit')):
#                     return True
#                 if view == 'meeting_analytics' and (data.get('analytics').get('view') or data.get('analytics').get('edit')):
#                     return True
#                 return False       
#         return False

# class UserPermission(permissions.BasePermission):
#     def has_object_permission(self, request,pk):
#         if request.user.is_superuser or request.user.id == int(pk):
#             return True
#         return False
    

# class SuperUserPermission(permissions.BasePermission):
#     def has_object_permission(self, request):
#         if request.user.is_superuser:
#             return True
#         return False