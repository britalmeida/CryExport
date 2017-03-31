# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

# <pep8 compliant>

bl_info = {
    "name": "CryExport",
    "description": "Blender Add-on to export to CryEngine's native formats (.cgf .cdf .chr .skin .caf .mtl)",
    "author": "Inês Almeida, Viktor Ikkes, Ali Helmy",
    "version": (0, 0, 1),
    "blender": (2, 78, 0),
    "location": "todo",
    "warning": "In development",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/"
                "Scripts/Import-Export/-todo-create-new-documentation-page!",
    "tracker_url": "https://github.com/britalmeida/CryExport/issues",
    "support": "COMMUNITY",
    "category": "Import-Export",
}

import time

import bpy
from bpy.types import (
    Operator,
    AddonPreferences,
)

from bpy.props import (
    BoolProperty,
    StringProperty,
)

from bpy_extras.io_utils import (
    ExportHelper,
    #path_reference
    path_reference_mode,
)


# Data Structure ##############################################################


# Operators ###################################################################

def save_file(operator, context, filepath="", use_selection=False, **kwargs):

    print('CryEngine export starting... %r' % filepath)
    start_time = time.process_time()
    try:
        file = open(filepath, "w", encoding="utf8", newline="\n")
    except:
        import traceback
        traceback.print_exc()
        operator.report({'ERROR'}, "Couldn't open file %r" % filepath)
        return {'CANCELLED'}

    fw = file.write

    fw('hello')

    file.close()

    # copy all collected files.
    #bpy_extras.io_utils.path_reference_copy(copy_set)

    print('export finished in %.4f sec.' % (time.process_time() - start_time))
    return {'FINISHED'}


# UI ##########################################################################

class CryExportPreferences(AddonPreferences):
    """Preferences for the add-on with saved properties and UI"""
    bl_idname = __name__

    error_message = StringProperty(
        name='Error Message',
        default='',
        options={'HIDDEN', 'SKIP_SAVE'}
    )
    rc_path = StringProperty(
        name="Resource Compiler (RC)",
        description="todo",
        subtype='FILE_PATH',
    )
    game_path = StringProperty(
        name="Game Folder",
        description="todo",
        subtype='FILE_PATH',
    )

    def draw(self, context):
        layout = self.layout

        layout.prop(self, "rc_path")
        layout.prop(self, "game_path")



class CryExport(Operator, ExportHelper):
    """Export and write the files"""
    bl_idname = "export_scene.cry"
    bl_label = "Export CryEngine Formats"
    bl_options = {'UNDO'} #, 'PRESET'

    filename_ext = ".cry"
    filter_glob = StringProperty(default="*.cry", options={'HIDDEN'})
    check_existing = True
    path_mode = path_reference_mode

    use_selection = BoolProperty(
        name="Selected Objects",
        description="Export only selected objects on visible layers",
        default=False,
    )


    def draw(self, context):
        layout = self.layout

        layout.prop(self, "use_selection")


    def execute(self, context):
        if not self.filepath:
            raise Exception("filepath not set")

        keywords = self.as_keywords(ignore=(
            "check_existing",
            "filter_glob",
        ))

        return save_file(self, context, **keywords)



def menu_func_export(self, context):
    """Menu entry for File > Export"""
    self.layout.operator(CryExport.bl_idname, text="CryEngine (.cgf .cdf .chr ...)")


# Registry ####################################################################

classes = (
    CryExportPreferences,
    CryExport,
)



def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.INFO_MT_file_export.append(menu_func_export)




def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.types.INFO_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()
