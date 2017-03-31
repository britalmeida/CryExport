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
    "description": "Blender Add-on to export to CryEngine's native formats",
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



# Data Structure ##############################################################




# Registry ####################################################################

classes = (
)



def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
