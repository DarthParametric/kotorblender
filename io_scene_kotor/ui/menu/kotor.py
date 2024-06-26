# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

from bpy.types import Menu


class KB_MT_kotor_lightmaps(Menu):
    bl_label = "Lightmaps"

    def draw(self, context):
        layout = self.layout
        layout.operator("kb.bake_lightmaps_auto", text="Bake (auto)")
        layout.operator("kb.bake_lightmaps_manual", text="Bake (manual)")


class KB_MT_kotor_minimap(Menu):
    bl_label = "Mininmap"

    def draw(self, context):
        layout = self.layout
        layout.operator("kb.render_minimap_auto", text="Render (auto)")
        layout.operator("kb.render_minimap_manual", text="Render (manual)")


class KB_MT_kotor_showhide(Menu):
    bl_label = "Show/Hide"

    def draw(self, context):
        layout = self.layout

        layout.operator("kb.show_walkmeshes", icon="MESH_CUBE")
        layout.operator("kb.show_untextured", icon="IMAGE_RGB")
        layout.operator("kb.show_unlightmapped", icon="IMAGE_ALPHA")
        layout.operator("kb.show_lights", icon="OUTLINER_OB_LIGHT")
        layout.operator("kb.show_emitters", icon="PARTICLES")
        layout.operator("kb.show_char_bones", icon="BONE_DATA")
        layout.operator("kb.show_char_dummies", icon="OUTLINER_OB_EMPTY")
        layout.separator()
        layout.operator("kb.hide_walkmeshes", icon="MESH_CUBE")
        layout.operator("kb.hide_untextured", icon="IMAGE_RGB")
        layout.operator("kb.hide_unlightmapped", icon="IMAGE_ALPHA")
        layout.operator("kb.hide_lights", icon="OUTLINER_OB_LIGHT")
        layout.operator("kb.hide_emitters", icon="PARTICLES")
        layout.operator("kb.hide_char_bones", icon="BONE_DATA")
        layout.operator("kb.hide_char_dummies", icon="OUTLINER_OB_EMPTY")


class KB_MT_kotor(Menu):
    bl_label = "KotOR"

    def draw(self, context):
        layout = self.layout
        layout.menu("KB_MT_kotor_lightmaps")
        layout.menu("KB_MT_kotor_minimap")
        layout.menu("KB_MT_kotor_showhide")
