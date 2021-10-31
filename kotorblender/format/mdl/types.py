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

from ...defines import Classification


MODEL_FN_PTR_1_K1_PC = 4273776
MODEL_FN_PTR_1_K2_PC = 4285200
MODEL_FN_PTR_2_K1_PC = 4216096
MODEL_FN_PTR_2_K2_PC = 4216320

CLASS_OTHER = 0x00
CLASS_EFFECT = 0x01
CLASS_TILE = 0x02
CLASS_CHARACTER = 0x04
CLASS_DOOR = 0x08
CLASS_LIGHTSABER = 0x10
CLASS_PLACEABLE = 0x20
CLASS_FLYER = 0x40

CLASS_BY_VALUE = {
    CLASS_OTHER: Classification.UNKNOWN,
    CLASS_EFFECT: Classification.EFFECT,
    CLASS_TILE: Classification.TILE,
    CLASS_CHARACTER: Classification.CHARACTER,
    CLASS_DOOR: Classification.DOOR,
    CLASS_LIGHTSABER: Classification.SABER,
    CLASS_PLACEABLE: Classification.DOOR,
    CLASS_FLYER: Classification.FLYER
}

NODE_BASE = 0x0001
NODE_LIGHT = 0x0002
NODE_EMITTER = 0x0004
NODE_REFERENCE = 0x0010
NODE_MESH = 0x0020
NODE_SKIN = 0x0040
NODE_DANGLY = 0x0100
NODE_AABB = 0x0200
NODE_SABER = 0x0800

CTRL_BASE_POSITION = 8
CTRL_BASE_ORIENTATION = 20
CTRL_BASE_SCALE = 36
CTRL_MESH_SELFILLUMCOLOR = 100
CTRL_MESH_ALPHA = 132
CTRL_LIGHT_COLOR = 76
CTRL_LIGHT_RADIUS = 88
CTRL_LIGHT_SHADOWRADIUS = 96
CTRL_LIGHT_VERTICALDISPLACEMENT = 100
CTRL_LIGHT_MULTIPLIER = 140
CTRL_EMITTER_ALPHAEND = 80
CTRL_EMITTER_ALPHASTART = 84
CTRL_EMITTER_BIRTHRATE = 88
CTRL_EMITTER_BOUNCE_CO = 92
CTRL_EMITTER_COMBINETIME = 96
CTRL_EMITTER_DRAG = 100
CTRL_EMITTER_FPS = 104
CTRL_EMITTER_FRAMEEND = 108
CTRL_EMITTER_FRAMESTART = 112
CTRL_EMITTER_GRAV = 116
CTRL_EMITTER_LIFEEXP = 120
CTRL_EMITTER_MASS = 124
CTRL_EMITTER_P2P_BEZIER2 = 128
CTRL_EMITTER_P2P_BEZIER3 = 132
CTRL_EMITTER_PARTICLEROT = 136
CTRL_EMITTER_RANDVEL = 140
CTRL_EMITTER_SIZESTART = 144
CTRL_EMITTER_SIZEEND = 148
CTRL_EMITTER_SIZESTART_Y = 152
CTRL_EMITTER_SIZEEND_Y = 156
CTRL_EMITTER_SPREAD = 160
CTRL_EMITTER_THRESHOLD = 164
CTRL_EMITTER_VELOCITY = 168
CTRL_EMITTER_XSIZE = 172
CTRL_EMITTER_YSIZE = 176
CTRL_EMITTER_BLURLENGTH = 180
CTRL_EMITTER_LIGHTNINGDELAY = 184
CTRL_EMITTER_LIGHTNINGRADIUS = 188
CTRL_EMITTER_LIGHTNINGSCALE = 192
CTRL_EMITTER_LIGHTNINGSUBDIV = 196
CTRL_EMITTER_LIGHTNINGZIGZAG = 200
CTRL_EMITTER_ALPHAMID = 216
CTRL_EMITTER_PERCENTSTART = 220
CTRL_EMITTER_PERCENTMID = 224
CTRL_EMITTER_PERCENTEND = 228
CTRL_EMITTER_SIZEMID = 232
CTRL_EMITTER_SIZEMID_Y = 236
CTRL_EMITTER_RANDOMBIRTHRATE = 240
CTRL_EMITTER_TARGETSIZE = 252
CTRL_EMITTER_NUMCONTROLPTS = 256
CTRL_EMITTER_CONTROLPTRADIUS = 260
CTRL_EMITTER_CONTROLPTDELAY = 264
CTRL_EMITTER_TANGENTSPREAD = 268
CTRL_EMITTER_TANGENTLENGTH = 272
CTRL_EMITTER_COLORMID = 284
CTRL_EMITTER_COLOREND = 380
CTRL_EMITTER_COLORSTART = 392
CTRL_EMITTER_DETONATE = 502


class ControllerKey:
    def __init__(self, ctrl_type, num_rows, timekeys_start, values_start, num_columns):
        self.ctrl_type = ctrl_type
        self.num_rows = num_rows
        self.timekeys_start = timekeys_start
        self.values_start = values_start
        self.num_columns = num_columns


class ControllerRow:
    def __init__(self, timekey, values):
        self.timekey = timekey
        self.values = values

    def __repr__(self):
        return "{{timekey={}, values={}}}".format(self.timekey, self.values)