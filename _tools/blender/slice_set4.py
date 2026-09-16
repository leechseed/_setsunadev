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
# MakeHuman macro sliders: gender 0 = female · age 0.42 ≈ 21 years (0.1875 = 11, 0.5 = 25) · the rest provisional, Papi sculpts
MACRO = {"gender": 0.0, "age": 0.42, "muscle": 0.5, "weight": 0.5, "proportions": 0.6, "height": 0.5,
         "cupsize": 0.6, "firmness": 0.7, "race": {"asian": 0.0, "caucasian": 1.0, "african": 0.0}}

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
        # the free CC0 skin with enhanced SSS: this is the surface the Gate 3 skin test judges
        try:
            if os.path.exists(MPFB_SKIN):
                HumanService.set_character_skin(MPFB_SKIN, human, skin_type="ENHANCED_SSS")
            else:
                print("skin .mhmat not found:", MPFB_SKIN)
        except Exception as e:
            print("mpfb skin skipped:", e)
        # body parts from the CC0 pack: eyes · brows · lashes · a placeholder hair (Papi picks the real look in the Gate 3 evenings)
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
    m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.62, 0.58, 0.52, 1)
    m.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.9
    bed.data.materials.append(m)
    bpy.ops.mesh.primitive_plane_add(size=8, location=(0, 0, 0))
    bpy.context.active_object.name = "floor"
    bpy.ops.mesh.primitive_plane_add(size=6, location=(0, 2.2, 1.5), rotation=(math.radians(90), 0, 0))
    wall = bpy.context.active_object; wall.name = "wall"
    wm = bpy.data.materials.new("wall_paint"); wm.use_nodes = True
    wm.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.35, 0.30, 0.28, 1)
    wall.data.materials.append(wm)

def make_lights(hdri_path):
    # world: the HDRI as fill, low
    w = bpy.data.worlds.new("world_set4"); bpy.context.scene.world = w; w.use_nodes = True
    nt = w.node_tree; nt.nodes.clear()
    env = nt.nodes.new("ShaderNodeTexEnvironment")
    if os.path.exists(hdri_path):
        env.image = bpy.data.images.load(hdri_path)
    bg = nt.nodes.new("ShaderNodeBackground"); bg.inputs["Strength"].default_value = 0.12
    out = nt.nodes.new("ShaderNodeOutputWorld")
    nt.links.new(env.outputs["Color"], bg.inputs["Color"]); nt.links.new(bg.outputs["Background"], out.inputs["Surface"])
    # the warm key: one area light, low and to camera-left, 3000 K
    bpy.ops.object.light_add(type="AREA", location=(-1.4, -0.9, 1.35))
    key = bpy.context.active_object; key.name = "key_warm"
    key.data.energy = 45; key.data.size = 0.9; key.data.shape = "RECTANGLE"; key.data.size_y = 1.2
    key.data.use_temperature = True if hasattr(key.data, "use_temperature") else False
    if hasattr(key.data, "temperature"): key.data.temperature = 3000
    else: key.data.color = (1.0, 0.72, 0.48)
    key.rotation_euler = (math.radians(70), 0, math.radians(-55))
    # the faint cool rim, behind and opposite
    bpy.ops.object.light_add(type="AREA", location=(1.6, 1.4, 1.9))
    rim = bpy.context.active_object; rim.name = "rim_cool"
    rim.data.energy = 25; rim.data.size = 0.4; rim.data.color = (0.75, 0.85, 1.0)
    rim.rotation_euler = (math.radians(60), 0, math.radians(135))

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

if __name__ == "__main__":
    todo = [s for s in STILLS if (A.still is None or s[0] == A.still)]
    for st in todo:
        build(st, A.smoke)
        if (A.smoke or A.render) and st[0] == (A.still or "S4-01"):
            out = os.path.join(A.out, f"{'smoke' if A.smoke else 'full'}_{st[0]}.png")
            bpy.context.scene.render.filepath = out
            bpy.ops.render.render(write_still=True)
            print("SMOKE RENDER", out)
            if A.still is None and A.smoke: break
