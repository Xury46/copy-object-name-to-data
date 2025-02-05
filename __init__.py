bl_info = {
    "name": "Copy Object Name to Data",
    "author": "Xury Greer",
    "version": (1, 1, 1),
    "blender": (4, 2, 0),
    "location": "Outliner > Context Menu",
    "description": "Rename object data name to match object name",
    "warning": "",
    "doc_url": "",
    "category": "Utility",
}

# Import / reload local modules (Required when using the "Reload Scripts" (bpy.ops.scripts.reload()) operator in Blender
if "bpy" in locals():
    import importlib

    importlib.reload(copy_object_name_to_data)
else:
    from . import copy_object_name_to_data

import bpy


def register():
    copy_object_name_to_data.register()


def unregister():
    copy_object_name_to_data.unregister()
