# POSE 72 · the reference brief · comp 01 THE MARIONETTE

BOLO 72 · Bold Venture patch · 2026-09-18 · provisional pick (Chief said "go 72" without a number; 01 was his stated favourite, 03 is the fallback if the patch needs a symmetric read).

## The picture in one line

A giant white glove comes in from the top-right corner. Two strings fall straight down from its index and middle fingers to a thick, strong woman who hangs from them by her fists, back arched, head thrown back, legs kicked up behind her. Who's controlling who.

## The rule of the frame

| Element | Call |
|---|---|
| Frame | square, 2048 × 2048; the patch circle is cut in the paint-over, keep the action inside a circle of radius 0.8 × half-width |
| Proportion | the Hand is φ × her: she is 1.70 m, the Hand is 2.75 m cuff to fingertip |
| Golden section | the Hand owns the top 38 % of the field; she owns the bottom 62 %, offset left |
| Angle | the Hand's axis leans 38° off vertical toward her; her spine arcs the other way; the two axes cross behind the strings |
| Strings | two, straight down, taut; the only thing that connects them |
| The struggle | her fists are closed on the strings; the two fingers that hold her bend back under her weight; the other three are spread wide and rigid |

## Her build (MPFB2 macro sliders, in `pose72.py`)

muscle 0.85 · weight 0.62 · proportions 0.70 · height 0.55 · firmness 0.85. Thick thighs, real glutes, wide lats, delts that read from behind, a small waist. Not lean-fitness; strong. Chief sculpts from there.

## The pose, joint by joint (metres · x right · y away from camera · z up)

| Joint | Target | Note |
|---|---|---|
| wrists | L 0.06, 0.05, 2.05 · R 0.22, −0.02, 2.02 | fists closed on the strings, arms nearly straight up |
| elbows | L −0.02, 0.06, 1.78 · R 0.30, −0.02, 1.76 | a touch out, biceps loaded |
| shoulders | L 0.02, 0.02, 1.52 · R 0.26, −0.04, 1.50 | shrugged up into the hang |
| head | 0.02, −0.16, 1.44 | thrown back toward camera, chin up, hair falls straight down |
| hips | 0.14, 0.00, 1.05 | pushed forward, the arch |
| knees | L 0.28, 0.18, 0.86 · R 0.36, 0.14, 0.92 | bent, behind her |
| ankles | L 0.40, 0.30, 1.16 · R 0.48, 0.26, 1.22 | feet up behind, pointed |

The script places these as empties named `T_*`. Add the rig in MPFB2 (Rigging → Rigify or the standard rig), switch the limbs to IK, snap the IK targets to the empties, then sculpt the arch by hand.

## The Hand

Primitive glove: rounded-box palm, four cylinder fingers with sphere knuckles and tips, a thumb, a wrist cylinder, a cuff ring. Root empty `HAND` at 1.55, 0.35, 3.35, rotated −10 / −38 / 8, scaled to 2.75 m. Fingers are cartoon-straight on purpose; the paint-over bends the index and middle back.

## Light

One hard warm key, small, high, camera-left, 3400 K: it carves the muscle. A cool rim behind camera-right lifts her off the rose. HDRI fill at 0.10. The field is a rose plane (ROSE 700) and a bruise floor (ROSE 900) so the render's values already read as the patch.

## Camera

50 mm at −1.1, −7.2, 2.0, aimed at 0.45, 0.1, 2.0. f/5.6, focus on her hips.

## Output

`Q:/fun/_BOLO24/renders/patch72/patch72_comp01.blend` and a smoke frame. The frame is the reference under the painted pass; the painted pass is the Vargas job.

## Run

```
"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" --background --python _tools\patch\pose72.py -- --smoke
```
