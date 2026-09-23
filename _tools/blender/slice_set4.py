# -*- coding: utf-8 -*-
"""BOLO 24 · Gate 3 · the vertical slice — Set 4 scene scaffold (COA A: MPFB2 + Cycles + free HDRI).

Run headless:
  blender --background --python _tools/blender/slice_set4.py -- [--smoke] [--still S4-01] [--out Q:/fun/_BOLO24/renders]

What it builds (one .blend per still, five stills, the warm low-key single-light "intimate" set):
  · the subject: an MPFB2 base human if the extension is installed, else a placeholder body (the chain still proves out)
  · the NOIR warm low-key rig: one warm key (area, 3000 K) low and to the side, HDRI fill at low strength, a faint cool rim
  · five cameras, one per still, 85 mm at f/2, focus on the subject
  · Cycles on OptiX (RTX 3090), AgX, 4:5 at 2048×2560, OptiX denoise
  · --smoke renders S4-01 at 25 % / 32 samples to prove the pipeline end to end

Nothing here names the persona or the studio; the persona internals stay under _PRIVATE/.
"""
import bpy, sys, os, math, argparse

# ---- args after "--"
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
ap = argparse.ArgumentParser()
ap.add_argument("--smoke", action="store_true")
ap.add_argument("--render", action="store_true", help="render the chosen still (or S4-01) at full settings")
ap.add_argument("--still", default=None)
ap.add_argument("--out", default=r"Q:/fun/_BOLO24/renders")
ap.add_argument("--hdri", default=r"Q:/fun/_BOLO24/hdri/studio_small_09_2k.hdr")
ap.add_argument("--samples", type=int, default=256)
ap.add_argument("--no-face", action="store_true", help="build the stand-in without the ruled face targets")
ap.add_argument("--facecheck", action="store_true", help="also render a tight head framing for judging the sculpt (face_check.png)")
ap.add_argument("--stop", type=float, default=2.8, help="camera f-stop")
A = ap.parse_args(argv)
os.makedirs(A.out, exist_ok=True)
os.makedirs(os.path.join(A.out, "blend"), exist_ok=True)

# ---- the five stills of Set 4 (beat 5, shooting: intimate) · SFW 1 / suggestive 2 / explicit 2
STILLS = [
    # id, label, band, camera distance (m), camera height (m), yaw (deg), lens, notes
    ("S4-01", "face, the look back", "SFW",        1.05, 1.50, 25,  85, "close-up; the Gate 3 skin test frame; eyes to lens"),
    ("S4-02", "waist, sitting up",   "suggestive", 1.70, 1.25, 35,  85, "sheet held, shoulder light; key wraps the collarbone"),
    ("S4-03", "detail, the hand",    "suggestive", 0.90, 1.05, 60, 100, "hand on hip, skin texture under the key; no face"),
    ("S4-04", "three-quarter, on the bed", "explicit", 2.10, 1.30, 45, 85, "full low-key; the key at 1/4 ratio to the HDRI"),
    ("S4-05", "waist, turned away",  "explicit",   1.60, 1.20, 140, 85, "rear three-quarter; rim light carries the edge"),
]

def clear_scene():
    # never read_factory_settings here: it resets preferences and disables the MPFB2 extension for the session
    bpy.ops.object.select_all(action="SELECT"); bpy.ops.object.delete(use_global=False)
    for coll in (bpy.data.meshes, bpy.data.materials, bpy.data.lights, bpy.data.cameras, bpy.data.images, bpy.data.worlds):
        for x in list(coll):
            if x.users == 0: coll.remove(x)

MPFB_DATA = os.path.join(os.environ.get("APPDATA", ""), "Blender Foundation", "Blender", "4.5", "extensions", ".user", "user_default", "mpfb", "data")
MPFB_SKIN = os.path.join(MPFB_DATA, "skins", "young_caucasian_female", "young_caucasian_female.mhmat")
# MakeHuman macro sliders: gender 0 = female · age 0.42 ≈ 21 years (0.1875 = 11, 0.5 = 25) · the rest provisional, Chief sculpts
MACRO = {"gender": 0.0, "age": 0.42, "muscle": 0.55, "weight": 0.58, "proportions": 0.70, "height": 0.55,
         "cupsize": 0.65, "firmness": 0.7, "race": {"asian": 0.0, "caucasian": 1.0, "african": 0.0}}
# RULED 2026-09-23 (Chief, "take the 12"): SPEC-SUBJECT.md §2. age stays 0.42 = canon 21 and never moves.

# The face, SPEC-SUBJECT.md §8 — verified MPFB2 target names, applied BEFORE any mhclo asset is added
# (assets fit to the mesh as it stands at the moment they are added, so sculpt first or the hair sits wrong).
FACE = {
    "head-oval": 0.25,                # pass 4: was 0.75 — the oval was the Impost
    "forehead-scale-vert-decr": 0.35,
    "l-cheek-bones-incr": 0.75,  "r-cheek-bones-incr": 0.75,
    "l-cheek-volume-incr": 0.45, "r-cheek-volume-incr": 0.45,
    "chin-bones-incr": 0.55,          # pass 4: REVERSED — G1 wants a sharp gonial angle
    "chin-width-decr": 0.15,          # pass 4: was 0.40, a Transom keeps jaw width
    "l-eye-scale-incr": 0.70,    "r-eye-scale-incr": 0.70,
    "l-eye-height2-incr": 0.35,  "r-eye-height2-incr": 0.35,   # pass 3: 0.50 read startled
    "l-eye-corner2-up": 0.50,    "r-eye-corner2-up": 0.50,
    "eyebrows-angle-up": 0.40,
    "nose-scale-horiz-decr": 0.45,
    "nose-point-width-decr": 0.50,
    "nose-hump-decr": 0.35,
    "mouth-upperlip-volume-incr": 0.65,
    "mouth-lowerlip-volume-incr": 0.60,
    "mouth-cupidsbow-incr": 0.45,
    # pass 2, 9/23 ("push it"): the first render read older and more neutral than canon 21
    "chin-height-decr": 0.30,        # shortens the lower third
    "eyebrows-trans-down": 0.30,     # the brows sat high and light
    "head-age-decr": 0.20,           # youth on the cranial read; the age macro stays 0.42
    # pass 4, 9/23: aiming THE TRANSOM (FI3·G1·E3) per _CANON_NODES/L2b-morphology-face.md §4 —
    # wide short face · sharp gonial angle despite the width · wide-set eyes. The horizontal band read.
    "head-square": 0.35,             # FI3, the wide flat cranial read
    "head-scale-horiz-incr": 0.40,   # FI3 width
    "head-scale-vert-decr": 0.30,    # FI3 shortness
    "chin-prognathism-incr": 0.25,   # forward chin sets the direct read
    "l-eye-trans-out": 0.35, "r-eye-trans-out": 0.35,   # E3, wide-set
}

def apply_face(human):
    """Load and weight each face target. Returns (applied, skipped)."""
    try:
        try:
            from bl_ext.user_default.mpfb.services.targetservice import TargetService
        except ImportError:
            from mpfb.services.targetservice import TargetService
    except Exception as e:
        print("face targets skipped, TargetService unavailable:", e); return 0, len(FACE)
    ok = bad = 0
    for name, weight in FACE.items():
        try:
            path = TargetService.target_full_path(name)
            if path:
                TargetService.load_target(human, path, weight=weight)
            else:
                TargetService.set_target_value(human, name, weight, delete_target_on_zero=False)
            ok += 1
        except Exception as e:
            print("  target failed:", name, e); bad += 1
    print(f"face: {ok} target(s) applied, {bad} failed")
    return ok, bad

# The skin, pass 5 (9/23) — the banding fix.
# The CC0 material ships pore detail at strength 0.2 and radius scale 0.1, which is invisible at
# 85-105 mm, so the denoiser had a texture-less surface and quantised it into flat patches.
# Give it signal to hold onto, and widen the subsurface so gradients roll instead of stepping.
SKIN = {
    "Pore strength": 0.26,      # 0.20 banded, 0.62 read photoreal and fought the stylized ruling;
                                # the banding lever is the subsurface below, not the pores
    "Pore scale": 1100.0,       # was 2500 — finer than this vanishes at portrait framing
    "Pore detail": 3.0,         # was 2.0
    "Pore distortion": 1.4,     # was 1.0 — breaks the regularity so it does not read as a grid
    "Roughness": 0.38,          # was 0.45 — a touch more sheen for the register
    "SSS strength": 0.42,       # was 0.20
    "SSS radius scale": 0.32,   # was 0.10 — the main anti-banding lever: wider scatter, softer falloff
    "Clearcoat": 0.06,          # was 0.10 — less plastic
}

def tune_skin(values=None):
    """Drive the CC0 body material's node group. Returns the number of sockets set."""
    values = values or SKIN
    hit = 0
    for m in bpy.data.materials:
        if not m.use_nodes: continue
        for n in m.node_tree.nodes:
            if n.bl_idname != "ShaderNodeGroup" or not n.node_tree: continue
            if not n.node_tree.name.endswith("body"): continue
            for socket, val in values.items():
                if socket in n.inputs:
                    n.inputs[socket].default_value = val; hit += 1
    print(f"skin: {hit} socket(s) set")
    return hit

IRIS_MAJOR = (0.38, 0.40, 0.16, 1.0)   # hazel-green, RULED 9/23 call 4
IRIS_MINOR = (0.16, 0.12, 0.05, 1.0)   # the warm brown inner ring that makes it read hazel, not green

def set_iris(colour_major=IRIS_MAJOR, colour_minor=IRIS_MINOR):
    """MPFB's EnhancedEye group defaults to blue. Drive it to the ruled colour."""
    hit = 0
    for m in bpy.data.materials:
        if not m.use_nodes: continue
        for n in m.node_tree.nodes:
            if n.bl_idname == "ShaderNodeGroup" and n.node_tree and n.node_tree.name == "EnhancedEye":
                for socket, val in (("IrisMajorColor", colour_major), ("IrisMinorColor", colour_minor)):
                    if socket in n.inputs:
                        n.inputs[socket].default_value = val; hit += 1
    print(f"iris: {hit} socket(s) set")
    return hit

def make_subject():
    """MPFB2 human if available; else a placeholder that stands where she will."""
    try:
        try:
            from bl_ext.user_default.mpfb.services.humanservice import HumanService  # MPFB2 as a Blender 4.2+ extension
        except ImportError:
            from mpfb.services.humanservice import HumanService  # legacy addon path
        human = HumanService.create_human(mask_helpers=True, detailed_helpers=False, extra_vertex_groups=False,
                                          feet_on_ground=True, scale=0.1, macro_detail_dict=MACRO)
        human.name = "subject"
        if not A.no_face:
            apply_face(human)   # sculpt BEFORE the assets below, per the mhclo fitting order
        # the free CC0 skin with enhanced SSS: this is the surface the Gate 3 skin test judges
        try:
            if os.path.exists(MPFB_SKIN):
                HumanService.set_character_skin(MPFB_SKIN, human, skin_type="ENHANCED_SSS")
            else:
                print("skin .mhmat not found:", MPFB_SKIN)
        except Exception as e:
            print("mpfb skin skipped:", e)
        # body parts from the CC0 pack: eyes · brows · lashes · a placeholder hair (Chief picks the real look in the Gate 3 evenings)
        for sub, atype, mtype in (("eyes/high-poly/high-poly.mhclo", "Eyes", "PROCEDURAL_EYES"),
                                  ("eyebrows/eyebrow001/eyebrow001.mhclo", "Eyebrows", "MAKESKIN"),
                                  ("eyelashes/eyelashes01/eyelashes01.mhclo", "Eyelashes", "MAKESKIN"),
                                  ("hair/long01/long01.mhclo", "Hair", "MAKESKIN")):
            f = os.path.join(MPFB_DATA, *sub.split("/"))
            if not os.path.exists(f):
                print("asset missing:", f); continue
            try:
                HumanService.add_mhclo_asset(f, human, asset_type=atype, subdiv_levels=1, material_type=mtype, set_up_rigging=False)
            except Exception as e:
                try:
                    HumanService.add_mhclo_asset(f, human, asset_type=atype, subdiv_levels=1, material_type="MAKESKIN", set_up_rigging=False)
                except Exception as e2:
                    print("asset skipped:", sub, e2)
        tune_skin()
        set_iris()
        bpy.ops.object.select_all(action="DESELECT"); human.select_set(True); bpy.context.view_layer.objects.active = human
        bpy.ops.object.shade_smooth()
        return human, "mpfb"
    except Exception as e:
        print("MPFB2 not available, placeholder body:", e)
    # placeholder: a capsule body + sphere head, matte skin-toned
    bpy.ops.mesh.primitive_cylinder_add(radius=0.18, depth=1.25, location=(0, 0, 0.9))
    body = bpy.context.active_object; body.name = "subject"
    bpy.ops.object.shade_smooth()
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.11, location=(0, 0, 1.68), segments=64, ring_count=32)
    head = bpy.context.active_object; head.name = "subject_head"; bpy.ops.object.shade_smooth()
    mat = bpy.data.materials.new("placeholder_skin"); mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (0.80, 0.55, 0.45, 1)
    bsdf.inputs["Roughness"].default_value = 0.55
    bsdf.inputs["Subsurface Weight"].default_value = 0.25
    bsdf.inputs["Subsurface Radius"].default_value = (1.0, 0.2, 0.1)
    for o in (body, head): o.data.materials.append(mat)
    head.parent = body
    return body, "placeholder"

def make_bed():
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.3, 0.25))
    bed = bpy.context.active_object; bed.name = "bed"; bed.scale = (1.0, 1.1, 0.25)
    m = bpy.data.materials.new("linen"); m.use_nodes = True
    m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.38, 0.35, 0.31, 1)   # pass 3: was 0.62, the linen was a second fill
    m.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.9
    bed.data.materials.append(m)
    bpy.ops.mesh.primitive_plane_add(size=8, location=(0, 0, 0))
    floor = bpy.context.active_object; floor.name = "floor"
    # pass 3 (9/23): the floor had NO material, so it rendered at Blender's default 0.8 grey and was
    # the real fill in passes 1 and 2 — dropping the world strength never touched it.
    fm = bpy.data.materials.new("floor_dark"); fm.use_nodes = True
    fm.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.055, 0.05, 0.048, 1)
    fm.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.85
    floor.data.materials.append(fm)
    bpy.ops.mesh.primitive_plane_add(size=6, location=(0, 2.2, 1.5), rotation=(math.radians(90), 0, 0))
    wall = bpy.context.active_object; wall.name = "wall"
    wm = bpy.data.materials.new("wall_paint"); wm.use_nodes = True
    wm.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.10, 0.09, 0.088, 1)   # pass 3: was 0.35
    wm.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.95
    wall.data.materials.append(wm)

def make_lights(hdri_path):
    # world: the HDRI as fill, low
    w = bpy.data.worlds.new("world_set4"); bpy.context.scene.world = w; w.use_nodes = True
    nt = w.node_tree; nt.nodes.clear()
    env = nt.nodes.new("ShaderNodeTexEnvironment")
    if os.path.exists(hdri_path):
        env.image = bpy.data.images.load(hdri_path)
    bg = nt.nodes.new("ShaderNodeBackground"); bg.inputs["Strength"].default_value = 0.05   # pass 2: was 0.12, the fill was drowning the key
    out = nt.nodes.new("ShaderNodeOutputWorld")
    nt.links.new(env.outputs["Color"], bg.inputs["Color"]); nt.links.new(bg.outputs["Background"], out.inputs["Surface"])
    # the warm key: one area light, low and to camera-left, 3000 K
    bpy.ops.object.light_add(type="AREA", location=(-0.85, -0.62, 1.45))   # pass 3: pulled in from (-1.4,-0.9,1.35) for falloff
    key = bpy.context.active_object; key.name = "key_warm"
    # pass 2 (9/23): key was 45, the face was not being carved
    key.data.energy = 55; key.data.size = 0.75; key.data.shape = "RECTANGLE"; key.data.size_y = 1.2
    key.data.use_temperature = True if hasattr(key.data, "use_temperature") else False
    if hasattr(key.data, "temperature"): key.data.temperature = 3000
    else: key.data.color = (1.0, 0.72, 0.48)
    key.rotation_euler = (math.radians(70), 0, math.radians(-55))
    # the cool rim, behind and opposite the key.
    # pass 6 (9/23): it sat at (1.6,1.4,1.9) on a hand-set euler — 2.5 m out, small, and aimed by
    # rotation, so inverse square ate it and it never landed on the jaw. Pulled in, and aimed with a
    # constraint at the head instead of by rotation, so it cannot drift when anything else moves.
    rim_aim = bpy.data.objects.new("rim_aim", None); rim_aim.location = (0, 0, 1.50)
    bpy.context.scene.collection.objects.link(rim_aim)
    bpy.ops.object.light_add(type="AREA", location=(1.02, 0.88, 1.76))
    rim = bpy.context.active_object; rim.name = "rim_cool"
    rim.data.energy = 58; rim.data.size = 0.30; rim.data.color = (0.68, 0.80, 1.0)
    rc = rim.constraints.new("TRACK_TO"); rc.target = rim_aim
    rc.track_axis = "TRACK_NEGATIVE_Z"; rc.up_axis = "UP_Y"

def make_camera(still, subject_z=1.35):
    sid, label, band, dist, height, yaw, lens, notes = still
    yaw_r = math.radians(yaw)
    loc = (dist * math.sin(yaw_r) * -1, dist * math.cos(yaw_r) * -1, height)
    cam_data = bpy.data.cameras.new(sid); cam = bpy.data.objects.new(sid, cam_data)
    bpy.context.scene.collection.objects.link(cam)
    cam.location = loc
    # aim at the subject
    target = bpy.data.objects.new(sid + "_aim", None); target.location = (0, 0, 1.47 if "face" in label else (1.15 if "waist" in label else 1.0))
    if "face" in label:  # focus on the eye plane, not the head's center
        target.location = (-0.04 * math.sin(yaw_r), -0.10 * math.cos(yaw_r) * -1 * -1, 1.47)
    bpy.context.scene.collection.objects.link(target)
    c = cam.constraints.new("TRACK_TO"); c.target = target; c.track_axis = "TRACK_NEGATIVE_Z"; c.up_axis = "UP_Y"
    cam_data.lens = lens; cam_data.sensor_width = 36
    cam_data.dof.use_dof = True; cam_data.dof.focus_object = target; cam_data.dof.aperture_fstop = 2.8
    cam["still"] = sid; cam["band"] = band; cam["notes"] = notes
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
    s.render.resolution_x, s.render.resolution_y = 2048, 2560   # 4:5, the platform portrait crop
    s.render.resolution_percentage = 25 if smoke else 100
    s.render.image_settings.file_format = "PNG"; s.render.image_settings.color_depth = "16"
    s.view_settings.view_transform = "AgX"; s.view_settings.look = "AgX - Medium High Contrast"
    s.view_settings.exposure = -0.4
    s.render.film_transparent = False

def build(still, smoke):
    clear_scene()
    subject, kind = make_subject()
    make_bed(); make_lights(A.hdri)
    cam = make_camera(still); bpy.context.scene.camera = cam
    render_settings(smoke)
    sid = still[0]
    blend = os.path.join(A.out, "blend", f"set4_{sid}.blend")
    bpy.ops.wm.save_as_mainfile(filepath=blend)
    print(f"[{sid}] {still[1]} · {still[2]} · subject={kind} · saved {blend}")
    return blend

FACECHECK = ("FACE", "face, the sculpt check", "SFW", 1.00, 1.52, 12, 105,
             "tight head framing for judging the sculpt; not a Set 4 still")

if __name__ == "__main__":
    todo = [s for s in STILLS if (A.still is None or s[0] == A.still)]
    for st in todo:
        build(st, A.smoke)
        if (A.smoke or A.render) and st[0] == (A.still or "S4-01"):
            out = os.path.join(A.out, f"{'smoke' if A.smoke else 'full'}_{st[0]}.png")
            bpy.context.scene.render.filepath = out
            bpy.ops.render.render(write_still=True)
            print("SMOKE RENDER", out)
        if A.facecheck and st[0] == (A.still or "S4-01"):
            cam2 = make_camera(FACECHECK); bpy.context.scene.camera = cam2
            bpy.context.scene.render.resolution_x, bpy.context.scene.render.resolution_y = 1600, 2000
            out2 = os.path.join(A.out, "face_check.png")
            bpy.context.scene.render.filepath = out2
            bpy.ops.render.render(write_still=True)
            print("FACE CHECK", out2)
            if A.still is None and A.smoke: break
