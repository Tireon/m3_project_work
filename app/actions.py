import objectpack
from objectpack.actions import ObjectPack
from .controller import observer
from .ui import UserAddWindow
from django.contrib.auth.models import Group, ContentType, Permission, User

class UserPack(ObjectPack):
    model = User
    add_to_menu = True
    add_to_desktop = True
    add_window = edit_window = UserAddWindow

class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_menu = True
    add_to_desktop = True
    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)

class GroupPack(ObjectPack):
    model = Group
    add_to_menu = True
    add_to_desktop = True
    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)

class PermissionPack(ObjectPack):
    model = Permission
    add_to_menu = True
    add_to_desktop = True
    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model, model_register=observer)
