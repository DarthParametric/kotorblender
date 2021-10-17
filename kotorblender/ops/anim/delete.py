import bpy

from ... import kb_utils


class KB_OT_anim_delete(bpy.types.Operator):
    """Delete the selected animation and its keyframes"""

    bl_idname = "kb.anim_delete"
    bl_label = "Delete an animation"

    @classmethod
    def poll(self, context):
        """Prevent execution if animation list is empty."""
        mdl_base = kb_utils.get_mdl_root_from_object(context.object)
        if mdl_base is not None:
            return (len(mdl_base.nvb.animList) > 0)
        return False

    def delete_frames(self, obj, frame_start, frame_end):
        """Delete the animation's keyframes."""
        if obj.animation_data and obj.animation_data.action:
            for fcu in obj.animation_data.action.fcurves:
                dp = fcu.data_path
                frames = [p.co[0] for p in fcu.keyframe_points
                          if frame_start <= p.co[0] <= frame_end]
                for f in frames:
                    obj.keyframe_delete(dp, frame=f)
                fcu.update()

    def execute(self, context):
        """Delete the animation."""
        mdl_base = kb_utils.get_mdl_root_from_object(context.object)
        anim_list = mdl_base.nvb.animList
        anim_list_idx = mdl_base.nvb.animListIdx
        anim = anim_list[anim_list_idx]
        # Grab some data for speed
        frame_start = anim.frameStart
        frame_end = anim.frameEnd
        # Remove keyframes
        obj_list = [mdl_base]
        kb_utils.get_children_recursive(mdl_base, obj_list)
        for obj in obj_list:
            # Objects animation
            self.delete_frames(obj, frame_start, frame_end)
            # Material animation
            if obj.active_material:
                self.delete_frames(obj.active_material, frame_start, frame_end)
            # Emitter animation
            part_sys = obj.particle_systems.active
            if part_sys:
                self.delete_frames(part_sys.settings, frame_start, frame_end)
        # Remove animation from List
        anim_list.remove(anim_list_idx)
        if anim_list_idx > 0:
            mdl_base.nvb.animListIdx = anim_list_idx - 1
        return {'FINISHED'}