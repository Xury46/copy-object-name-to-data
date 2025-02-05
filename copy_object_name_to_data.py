from typing import cast

import bpy
from bpy.types import Context, Object, Operator
from bpy.props import BoolProperty


class OBJECT_OT_copy_object_name_to_data(Operator):
    """Rename the object data of each selected object to match the object name"""

    bl_idname = "object.copy_object_name_to_data"
    bl_label = "Copy Object Name to Data"
    bl_options = {"REGISTER", "UNDO"}

    invert: BoolProperty(
        name="Invert",
        description="Copy the name in the inverted direction: 'data -> object' instead of 'object -> data'",
        default=False,
    )

    def execute(self, context: Context) -> set[str]:
        # Get the valid object IDs from the Outliner selection.
        objects: list[Object] = [cast(Object, id) for id in context.selected_ids if id.id_type == "OBJECT"]

        if self.invert:
            self.copy_data_name_to_object(objects)
        else:
            self.copy_object_name_to_data(objects)

        return {"FINISHED"}

    def copy_object_name_to_data(self, objects: list[Object]) -> None:
        for object in objects:
            data = getattr(object, "data", None)
            if data:
                data.name = object.name

    def copy_data_name_to_object(self, objects: list[Object]) -> None:
        for object in objects:
            data = getattr(object, "data", None)
            if data:
                object.name = data.name


def draw(self, context: Context) -> None:
    """Draw the operator as an option on a menu."""
    layout = self.layout
    # Main option
    object_to_data = layout.operator(
        OBJECT_OT_copy_object_name_to_data.bl_idname,
    )
    object_to_data.invert = False
    # Inverted option
    data_to_object = layout.operator(
        OBJECT_OT_copy_object_name_to_data.bl_idname,
        text="Copy Data Name to Object",
    )
    data_to_object.invert = True


def register():
    bpy.utils.register_class(OBJECT_OT_copy_object_name_to_data)
    bpy.types.OUTLINER_MT_object.append(draw)
    bpy.types.VIEW3D_MT_object.append(draw)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_copy_object_name_to_data)
    bpy.types.OUTLINER_MT_object.remove(draw)
    bpy.types.VIEW3D_MT_object.remove(draw)
