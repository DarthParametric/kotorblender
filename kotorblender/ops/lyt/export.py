import bpy
import bpy_extras

from ... import kb_def, kb_utils


class KB_OT_export_lyt(bpy.types.Operator, bpy_extras.io_utils.ExportHelper):
    """Export Odyssey Engine layout (.lyt)"""

    bl_idname = "kb.lytexport"
    bl_label  = "Export Odyssey LYT"

    filename_ext = ".lyt"

    filter_glob : bpy.props.StringProperty(
            default = "*.lyt",
            options = {'HIDDEN'})

    def _describe_object(self, obj):
        parent = kb_utils.get_mdl_root(obj)
        orientation = obj.rotation_euler.to_quaternion()
        return "{} {} {:.7g} {:.7g} {:.7g} {:.7g} {:.7g} {:.7g} {:.7g}".format(parent.name if parent else "NULL", obj.name, *obj.matrix_world.translation, *orientation)

    def execute(self, context):
        with open(self.filepath, "w") as f:
            rooms = []
            doors = []
            others = []

            objects = bpy.context.selected_objects if len(bpy.context.selected_objects) > 0 else bpy.context.collection.objects
            for obj in objects:
                if obj.type == 'EMPTY':
                    if obj.nvb.dummytype == kb_def.Dummytype.MDLROOT:
                        rooms.append(obj)
                    elif obj.name.lower().startswith("door"):
                        doors.append(obj)
                    else:
                        others.append(obj)

            f.write("beginlayout\n")
            f.write("  roomcount {}\n".format(len(rooms)))
            for room in rooms:
                f.write("    {} {:.7g} {:.7g} {:.7g}\n".format(room.name, *room.location))
            f.write("  trackcount 0\n")
            f.write("  obstaclecount 0\n")
            f.write("  doorhookcount {}\n".format(len(doors)))
            for door in doors:
                f.write("    {}\n".format(self._describe_object(door)))
            f.write("  othercount {}\n".format(len(others)))
            for other in others:
                f.write("    {}\n".format(self._describe_object(other)))
            f.write("donelayout\n")

        return {'FINISHED'}