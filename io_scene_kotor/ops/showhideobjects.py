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

import bpy

from ..constants import MeshType
from ..utils import (
    is_null,
    is_not_null,
    is_char_dummy,
    is_char_bone,
    is_mesh_type,
    is_aabb_mesh,
)


class KB_OT_hide_walkmeshes(bpy.types.Operator):
    bl_idname = "kb.hide_walkmeshes"
    bl_label = "Hide Walkmeshes"
    bl_description = "Hides all walkmeshes in the scene"

    def execute(self, context):
        bpy.ops.object.select_all(action="DESELECT")

        for obj in bpy.context.scene.objects:
            if is_aabb_mesh(obj):
                obj.hide_viewport = True
                obj.hide_render = True

        return {"FINISHED"}


class KB_OT_hide_untextured(bpy.types.Operator):
    bl_idname = "kb.hide_untextured"
    bl_label = "Hide Untextured"
    bl_description = "Hides all untextured trimeshes in the scene"

    def execute(self, context):
        bpy.ops.object.select_all(action="DESELECT")

        for obj in bpy.context.scene.objects:
            if (
                is_mesh_type(obj, MeshType.TRIMESH)
                and is_null(obj.kb.bitmap)
                and is_null(obj.kb.bitmap2)
            ):
                obj.hide_viewport = True
                obj.hide_render = True

        return {"FINISHED"}


class KB_OT_hide_unlightmapped(bpy.types.Operator):
    bl_idname = "kb.hide_unlightmapped"
    bl_label = "Hide Unlightmapped"
    bl_description = "Hides all unlightmapped meshes in the scene"

    def execute(self, context):
        bpy.ops.object.select_all(action="DESELECT")

        for obj in bpy.context.scene.objects:
            if obj.type == "MESH" and (
                not obj.kb.lightmapped or is_null(obj.kb.bitmap2)
            ):
                obj.hide_viewport = True
                obj.hide_render = True

        return {"FINISHED"}


class KB_OT_hide_lights(bpy.types.Operator):
    bl_idname = "kb.hide_lights"
    bl_label = "Hide Lights"
    bl_description = "Hides all lights in the scene"

    def execute(self, context):
        bpy.ops.object.select_all(action="DESELECT")

        for obj in bpy.context.scene.objects:
            if obj.type == "LIGHT":
                obj.hide_viewport = True
                obj.hide_render = True

        return {"FINISHED"}


class KB_OT_hide_emitters(bpy.types.Operator):
    bl_idname = "kb.hide_emitters"
    bl_label = "Hide Emitters"
    bl_description = "Hides all emitters in the scene"

    def execute(self, context):
        bpy.ops.object.select_all(action="DESELECT")

        for obj in bpy.context.scene.objects:
            if is_mesh_type(obj, MeshType.EMITTER):
                obj.hide_viewport = True
                obj.hide_render = True

        return {"FINISHED"}


class KB_OT_hide_char_bones(bpy.types.Operator):
    bl_idname = "kb.hide_char_bones"
    bl_label = "Hide Character Bones"
    bl_description = "Hides all humanoid rig bones in the scene"

    def execute(self, context):
        bpy.ops.object.select_all(action="DESELECT")

        for obj in bpy.context.scene.objects:
            if is_char_bone(obj):
                obj.hide_viewport = True
                obj.hide_render = True

        return {"FINISHED"}


class KB_OT_hide_char_dummies(bpy.types.Operator):
    bl_idname = "kb.hide_char_dummies"
    bl_label = "Hide Character Dummies"
    bl_description = "Hides all humanoid rig dummy/null objects in the scene"

    def execute(self, context):
        bpy.ops.object.select_all(action="DESELECT")

        for obj in bpy.context.scene.objects:
            if is_char_dummy(obj):
                obj.hide_viewport = True
                obj.hide_render = True

        return {"FINISHED"}


class KB_OT_show_walkmeshes(bpy.types.Operator):
    bl_idname = "kb.show_walkmeshes"
    bl_label = "Show Walkmeshes"
    bl_description = "Reveals all walkmeshes in the scene"

    def execute(self, context):
        bpy.ops.object.select_all(action="DESELECT")

        for obj in bpy.context.scene.objects:
            if is_aabb_mesh(obj):
                obj.hide_viewport = False
                obj.hide_render = False

        return {"FINISHED"}


class KB_OT_show_untextured(bpy.types.Operator):
    bl_idname = "kb.show_untextured"
    bl_label = "Show Untextured"
    bl_description = "Reveals all untextured trimeshes in the scene"

    def execute(self, context):
        bpy.ops.object.select_all(action="DESELECT")

        for obj in bpy.context.scene.objects:
            if (
                is_mesh_type(obj, MeshType.TRIMESH)
                and is_null(obj.kb.bitmap)
                and is_null(obj.kb.bitmap2)
            ):
                obj.hide_viewport = False
                obj.hide_render = False

        return {"FINISHED"}


class KB_OT_show_unlightmapped(bpy.types.Operator):
    bl_idname = "kb.show_unlightmapped"
    bl_label = "Show Unlightmapped"
    bl_description = "Reveals all unlightmapped meshes in the scene"

    def execute(self, context):
        bpy.ops.object.select_all(action="DESELECT")

        for obj in bpy.context.scene.objects:
            if obj.type == "MESH" and (
                not obj.kb.lightmapped or is_null(obj.kb.bitmap2)
            ):
                obj.hide_viewport = False
                obj.hide_render = False

        return {"FINISHED"}


class KB_OT_show_lights(bpy.types.Operator):
    bl_idname = "kb.show_lights"
    bl_label = "Show Lights"
    bl_description = "Reveals all lights in the scene"

    def execute(self, context):
        bpy.ops.object.select_all(action="DESELECT")

        for obj in bpy.context.scene.objects:
            if obj.type == "LIGHT":
                obj.hide_viewport = False
                obj.hide_render = False

        return {"FINISHED"}


class KB_OT_show_emitters(bpy.types.Operator):
    bl_idname = "kb.show_emitters"
    bl_label = "Show Emitters"
    bl_description = "Reveals all emitters in the scene"

    def execute(self, context):
        bpy.ops.object.select_all(action="DESELECT")

        for obj in bpy.context.scene.objects:
            if is_mesh_type(obj, MeshType.EMITTER):
                obj.hide_viewport = False
                obj.hide_render = False

        return {"FINISHED"}


class KB_OT_show_char_bones(bpy.types.Operator):
    bl_idname = "kb.show_char_bones"
    bl_label = "Show Character Bones"
    bl_description = "Reveals all humanoid rig bones in the scene"

    def execute(self, context):
        bpy.ops.object.select_all(action="DESELECT")

        for obj in bpy.context.scene.objects:
            if is_char_bone(obj):
                obj.hide_viewport = False
                obj.hide_render = False

        return {"FINISHED"}


class KB_OT_show_char_dummies(bpy.types.Operator):
    bl_idname = "kb.show_char_dummies"
    bl_label = "Show Character Dummies"
    bl_description = "Reveals all humanoid rig dummy/null objects in the scene"

    def execute(self, context):
        bpy.ops.object.select_all(action="DESELECT")

        for obj in bpy.context.scene.objects:
            if is_char_dummy(obj):
                obj.hide_viewport = False
                obj.hide_render = False

        return {"FINISHED"}
