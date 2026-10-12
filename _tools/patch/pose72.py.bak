# -*- coding: utf-8 -*-
"""BOLO 72 · the pose reference — comp 01 THE MARIONETTE, stood up in the Blender studio (BOLO 24's rig).

Run headless:
  blender --background --python _tools/patch/pose72.py -- [--smoke] [--render] [--comp 01] [--out Q:/fun/_BOLO24/renders/patch72]

What it builds (one .blend, one square frame for the paint-over):
  · the subject: the MPFB2 base human with the sliders pushed thick and strong (muscle · weight · proportions),
    standing at the origin UNPOSED — the pose is Chief's hand: MPFB2 → Rigging → add a rig, then snap the IK
    targets to the T_* empties this script places (wrists · elbows · shoulders · head · hips · knees · ankles)
  · the Hand: the giant white glove from primitives (palm · five fingers · cuff), scaled so the Hand is φ × her
    height, entering from the top-right with the fingers pointing down-left at her
  · the strings: two thin cylinders, fingertip to wrist, straight down
  · the field: a rose backdrop (BVX ROSE 700) so the value read matches the patch
  · the light: one hard key upper-left to cut the muscle, a cool rim to lift her off the field, HDRI fill low
  · the camera: 50 mm, square 2048², the golden section drawn by where the Hand sits
  · --smoke renders at 25 % / 32 samples to prove the chain

The brief that goes with this is POSE-72.md beside it.
"""
import bpy, sys, os, math, argparse

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
ap = argparse.ArgumentParser()
ap.add_argument("--smoke", action="store_true")
ap.add_argument("--render", action="store_true")
ap.add_argument("--comp", default="01")
ap.add_argument("--out", default=r"Q:/fun/_BOLO24/renders/patch72")
ap.add_argument("--hdri", default=r"Q:/fun/_BOLO24/hdri/studio_small_09_2k.hdr")
ap.add_argument("--samples", type=int, default=256)
A = ap.parse_args(argv)
os.makedirs(A.out, exist_ok=True)

ROSE = (0.256, 0.014, 0.055, 1)      # #8A1F44 in linear
HER_HEIGHT = 1.70
PHI = 1.618
HAND_LEN = HER_HEIGHT * PHI          # cuff to middle fingertip, metres

# ---- comp 01 THE MARIONETTE · joint targets in metres (x right · y away from camera · z up) ----
# She hangs from two strings by the fists, arms up, back arched, head thrown back, legs kicked up behind.
TARGETS = {
    "T_wrist_L":    (0.06, 0.05, 2.05),
    "T_wrist_R":    (0.22, -0.02, 2.02),
    "T_elbow_L":    (-0.02, 0.06, 1.78),
    "T_elbow_R":    (0.30, -0.02, 1.76),
    "T_shoulder_L": (0.02, 0.02, 1.52),
    "T_shoulder_R": (0.26, -0.04, 1.50),
    "T_head":       (0.02, -0.16, 1.44),   # thrown back toward camera, chin up
    "T_hips":       (0.14, 0.00, 1.05),
    "T_knee_L":     (0.28, 0.18, 0.86),
    "T_knee_R":     (0.36, 0.14, 0.92),
    "T_ankle_L":    (0.40, 0.30, 1.16),    # feet up behind
    "T_ankle_R":    (0.48, 0.26, 1.22),
}
STRINGS = (("index", "T_wrist_L"), ("middle", "T_wrist_R"))


def clear_scene():
    bpy.ops.object.select_all(action="SELECT"); bpy.ops.object.delete(use_global=False)
    for coll in (bpy.data.meshes, bpy.data.materials, bpy.data.lights, bpy.data.cameras, bpy.data.images, bpy.data.worlds, bpy.data.curves):
        for x in list(coll):
            if x.users == 0: coll.remove(x)


def mat(name, rgba, rough=0.5, sss=0.0):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = rgba; b.inputs["Roughness"].default_value = rough
    if sss: b.inputs["Subsurface Weight"].default_value = sss
    return m


# ---- the subject ---------------------------------------------------------------------------
MPFB_DATA = os.path.join(os.environ.get("APPDATA", ""), "Blender Foundation", "Blender", "4.5", "extensions", ".user", "user_default", "mpfb", "data")
MPFB_SKIN = os.path.join(MPFB_DATA, "skins", "young_caucasian_female", "young_caucasian_female.mhmat")
# thick and strong: muscle high, weight above centre, proportions toward the ideal, height a touch up
MACRO = {"gender": 0.0, "age": 0.45, "muscle": 0.85, "weight": 0.62, "proportions": 0.7, "height": 0.55,
         "cupsize": 0.55, "firmness": 0.85, "race": {"asian": 0.0, "caucasian": 1.0, "african": 0.0}}


def make_subject():
    try:
        try:
            from bl_ext.user_default.mpfb.services.humanservice import HumanService
        except ImportError:
            from mpfb.services.humanservice import HumanService
        human = HumanService.create_human(mask_helpers=True, detailed_helpers=False, extra_vertex_groups=False,
                                          feet_on_ground=True, scale=0.1, macro_detail_dict=MACRO)
        human.name = "subject"
        try:
            if os.path.exists(MPFB_SKIN):
                HumanService.set_character_skin(MPFB_SKIN, human, skin_type="ENHANCED_SSS")
        except Exception as e:
            print("mpfb skin skipped:", e)
        bpy.ops.object.select_all(action="DESELECT"); human.select_set(True); bpy.context.view_layer.objects.active = human
        bpy.ops.object.shade_smooth()
        return human, "mpfb"
    except Exception as e:
        print("MPFB2 not available, placeholder body:", e)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.19, depth=1.25, location=(0, 0, 0.9))
    body = bpy.context.active_object; body.name = "subject"; bpy.ops.object.shade_smooth()
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.11, location=(0, 0, 1.68), segments=64, ring_count=32)
    head = bpy.context.active_object; head.name = "subject_head"; bpy.ops.object.shade_smooth()
    m = mat("placeholder_skin", (0.80, 0.55, 0.45, 1), 0.55, 0.25)
    for o in (body, head): o.data.materials.append(m)
    head.parent = body
    return body, "placeholder"


def make_targets():
    coll = bpy.data.collections.new("pose_targets"); bpy.context.scene.collection.children.link(coll)
    for name, loc in TARGETS.items():
        e = bpy.data.objects.new(name, None); e.empty_display_type = "SPHERE"; e.empty_display_size = 0.05
        e.location = loc; coll.objects.link(e)
    return coll


# ---- the Hand ------------------------------------------------------------------------------
def make_hand():
    """A cartoon glove from primitives. Local: palm centre at origin, fingers along -Z (down), back of the hand +Y."""
    glove = mat("glove_white", (0.92, 0.92, 0.92, 1), 0.35)
    parts = []
    s = HAND_LEN / 2.75          # the primitive glove below is ~2.75 units cuff-to-tip; scale to HAND_LEN
    # palm: a rounded box
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
    palm = bpy.context.active_object; palm.name = "hand_palm"; palm.scale = (0.95, 0.32, 0.95)
    bev = palm.modifiers.new("bevel", "BEVEL"); bev.width = 0.14; bev.segments = 6
    palm.modifiers.new("subd", "SUBSURF").levels = 2
    parts.append(palm)
    # fingers: base x, base z, length, radius, splay (deg), curl (deg)
    fingers = {"index": (-0.36, -0.42, 1.05, 0.15, 12, 18), "middle": (-0.12, -0.46, 1.15, 0.155, 4, 22),
               "ring": (0.12, -0.45, 1.08, 0.15, -4, 20), "pinky": (0.36, -0.40, 0.85, 0.13, -14, 16)}
    tips = {}
    for name, (bx, bz, L, r, splay, curl) in fingers.items():
        bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=L, location=(bx, 0, bz - L / 2), vertices=48)
        f = bpy.context.active_object; f.name = "hand_" + name
        # straight, cartoon-style: the paint-over bends them; curl and splay stay in the table for the sculpt pass
        bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=(bx, 0, bz - L), segments=48, ring_count=24)
        tip = bpy.context.active_object; tip.name = "hand_%s_tip" % name
        bpy.ops.mesh.primitive_uv_sphere_add(radius=r * 1.05, location=(bx, 0, bz), segments=48, ring_count=24)
        knuckle = bpy.context.active_object; knuckle.name = "hand_%s_knuckle" % name
        for o in (f, tip, knuckle): bpy.ops.object.shade_smooth(); parts.append(o)
        tips[name] = tip
    # thumb
    # thumb: base at the palm's edge, axis down-left (the cylinder's Z turned -120° about Y)
    tb, tL, tax = (-0.50, 0, -0.15), 0.95, (-0.866, 0, -0.5)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.17, depth=tL, vertices=48,
                                        location=(tb[0] + tax[0] * tL / 2, 0, tb[2] + tax[2] * tL / 2))
    th = bpy.context.active_object; th.name = "hand_thumb"; th.rotation_euler = (0, math.radians(-120), 0); parts.append(th)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.17, location=(tb[0] + tax[0] * tL, 0, tb[2] + tax[2] * tL), segments=48, ring_count=24)
    tt = bpy.context.active_object; tt.name = "hand_thumb_tip"; parts.append(tt)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.19, location=tb, segments=48, ring_count=24)
    tk = bpy.context.active_object; tk.name = "hand_thumb_knuckle"; parts.append(tk)
    # wrist + cuff
    bpy.ops.mesh.primitive_cylinder_add(radius=0.42, depth=0.9, location=(0, 0, 0.9), vertices=64)
    wrist = bpy.context.active_object; wrist.name = "hand_wrist"; parts.append(wrist)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.52, depth=0.22, location=(0, 0, 1.35), vertices=64)
    cuff = bpy.context.active_object; cuff.name = "hand_cuff"; parts.append(cuff)
    for o in parts:
        o.data.materials.append(glove)
        bpy.ops.object.select_all(action="DESELECT"); o.select_set(True); bpy.context.view_layer.objects.active = o
        bpy.ops.object.shade_smooth()
    # parent everything to one empty and place it: top-right, fingers pointing down-left at her
    root = bpy.data.objects.new("HAND", None); root.empty_display_type = "ARROWS"; root.empty_display_size = 0.5
    bpy.context.scene.collection.objects.link(root)
    for o in parts: o.parent = root
    root.scale = (s, s, s)
    root.rotation_euler = (math.radians(-10), math.radians(38), math.radians(8))    # +Y tilt: the fingers rake down-LEFT at her
    root.location = (1.35, 0.35, 3.25)
    bpy.context.view_layer.update()
    tip_world = {n: (t.matrix_world.translation.copy()) for n, t in tips.items()}
    return root, tip_world


def make_strings(tip_world):
    m = mat("string_gold", (0.85, 0.62, 0.12, 1), 0.4)
    for finger, target in STRINGS:
        a = tip_world[finger]; b = bpy.data.objects[target].location
        # the string hangs straight down from the fingertip to the fist's x,y: we move the target under the tip
        bpy.data.objects[target].location = (a.x, a.y, b.z)
        b = bpy.data.objects[target].location
        L = a.z - b.z
        bpy.ops.mesh.primitive_cylinder_add(radius=0.006, depth=L, location=(a.x, a.y, (a.z + b.z) / 2), vertices=12)
        s = bpy.context.active_object; s.name = "string_" + finger; s.data.materials.append(m)


# ---- field · light · camera · render --------------------------------------------------------
def make_field():
    bpy.ops.mesh.primitive_plane_add(size=14, location=(0, 4.0, 2.0), rotation=(math.radians(90), 0, 0))
    field = bpy.context.active_object; field.name = "field_rose"
    field.data.materials.append(mat("rose_700", ROSE, 0.9))
    bpy.ops.mesh.primitive_plane_add(size=14, location=(0, 0, 0))
    floor = bpy.context.active_object; floor.name = "ground_bruise"
    floor.data.materials.append(mat("rose_900", (0.09, 0.005, 0.02, 1), 0.95))


def make_lights(hdri):
    w = bpy.data.worlds.new("world_72"); bpy.context.scene.world = w; w.use_nodes = True
    nt = w.node_tree; nt.nodes.clear()
    env = nt.nodes.new("ShaderNodeTexEnvironment")
    if os.path.exists(hdri): env.image = bpy.data.images.load(hdri)
    bg = nt.nodes.new("ShaderNodeBackground"); bg.inputs["Strength"].default_value = 0.10
    out = nt.nodes.new("ShaderNodeOutputWorld")
    nt.links.new(env.outputs["Color"], bg.inputs["Color"]); nt.links.new(bg.outputs["Background"], out.inputs["Surface"])
    # the hard key: small, high, camera-left — it cuts the muscle
    bpy.ops.object.light_add(type="AREA", location=(-2.6, -2.4, 3.6))
    key = bpy.context.active_object; key.name = "key_hard"
    key.data.energy = 900; key.data.size = 0.35
    if hasattr(key.data, "use_temperature"): key.data.use_temperature = True
    if hasattr(key.data, "temperature"): key.data.temperature = 3400
    key.rotation_euler = (math.radians(52), 0, math.radians(-48))
    # the cool rim, behind and camera-right, lifts her off the rose
    bpy.ops.object.light_add(type="AREA", location=(2.2, 1.8, 2.6))
    rim = bpy.context.active_object; rim.name = "rim_cool"
    rim.data.energy = 300; rim.data.size = 0.5; rim.data.color = (0.75, 0.85, 1.0)
    rim.rotation_euler = (math.radians(62), 0, math.radians(140))


def make_camera():
    cam_data = bpy.data.cameras.new("CAM_72"); cam = bpy.data.objects.new("CAM_72", cam_data)
    bpy.context.scene.collection.objects.link(cam)
    cam.location = (-1.1, -7.2, 2.0)
    aim = bpy.data.objects.new("CAM_72_aim", None); aim.location = (0.45, 0.1, 2.0)
    bpy.context.scene.collection.objects.link(aim)
    c = cam.constraints.new("TRACK_TO"); c.target = aim; c.track_axis = "TRACK_NEGATIVE_Z"; c.up_axis = "UP_Y"
    cam_data.lens = 50; cam_data.sensor_width = 36
    cam_data.dof.use_dof = True; cam_data.dof.focus_object = bpy.data.objects["T_hips"]; cam_data.dof.aperture_fstop = 5.6
    bpy.context.scene.camera = cam
    return cam


def render_settings(smoke):
    s = bpy.context.scene
    s.render.engine = "CYCLES"
    prefs = bpy.context.preferences.addons.get("cycles")
    if prefs:
        cp = prefs.preferences
        try:
            cp.compute_device_type = "OPTIX"; cp.get_devices()
            for d in cp.devices: d.use = (d.type == "OPTIX") or d.type == "CPU"
        except Exception as e:
            print("OptiX not set:", e)
    s.cycles.device = "GPU"
    s.cycles.samples = 32 if smoke else A.samples
    s.cycles.use_denoising = True
    try: s.cycles.denoiser = "OPTIX"
    except Exception: pass
    s.render.resolution_x = s.render.resolution_y = 2048      # the patch is square; the circle is cut in the paint-over
    s.render.resolution_percentage = 25 if smoke else 100
    s.render.image_settings.file_format = "PNG"; s.render.image_settings.color_depth = "16"
    s.view_settings.view_transform = "AgX"; s.view_settings.look = "AgX - Medium High Contrast"
    s.view_settings.exposure = -0.3


def build():
    clear_scene()
    subject, kind = make_subject()
    make_targets()
    root, tips = make_hand()
    make_strings(tips)
    make_field(); make_lights(A.hdri); make_camera(); render_settings(A.smoke)
    blend = os.path.join(A.out, "patch72_comp%s.blend" % A.comp)
    bpy.ops.wm.save_as_mainfile(filepath=blend)
    print("[72] comp %s · subject=%s · hand %.2f m · saved %s" % (A.comp, kind, HAND_LEN, blend))
    return blend


if __name__ == "__main__":
    build()
    if A.smoke or A.render:
        out = os.path.join(A.out, "%s_comp%s.png" % ("smoke" if A.smoke else "full", A.comp))
        bpy.context.scene.render.filepath = out
        bpy.ops.render.render(write_still=True)
        print("RENDER", out)
