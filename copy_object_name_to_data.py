import bpy
from bpy.types import Operator


class OBJECT_OT_copy_object_name_to_data(Operator):
    """Rename the object data of each selected object to match the object name"""

    bl_idname = "object.copy_object_name_to_data"
    bl_label = "Copy Object Name to Data"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        for object in bpy.context.selected_ids:
            # Get the object data if it exists (collections, and empty objects have no data).
            data = getattr(object, "data", None)

            if not data:
                continue

            data.name = object.name

        return {"FINISHED"}


def draw(self, context):
    """Draw the operator as an option on a menu."""
    layout = self.layout
    layout.operator(OBJECT_OT_copy_object_name_to_data.bl_idname)


def register():
    bpy.utils.register_class(OBJECT_OT_copy_object_name_to_data)
    bpy.types.OUTLINER_MT_object.append(draw)
    bpy.types.VIEW3D_MT_object_context_menu.append(draw)
    bpy.types.VIEW3D_MT_object.append(draw)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_copy_object_name_to_data)
    bpy.types.OUTLINER_MT_object.remove(draw)
    bpy.types.VIEW3D_MT_object_context_menu.remove(draw)
    bpy.types.VIEW3D_MT_object.remove(draw)
