"""BOLO 83 — turn a résumé spec into a paste sheet for Amazon's one-field-at-a-time application form.
Every value gets its own fenced block (one-click copy, SOP §7 rule 8).

Usage:  python _tools/bolo83/forms.py <spec.json> <out FORM.md> "<job title for the header>"
"""
import io, json, re, sys

MONTHS = {m: i for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}
spec = json.load(io.open(sys.argv[1], encoding="utf-8"))
out = [f"# Paste sheet — {sys.argv[3]}", "",
       "Amazon's form asks one field at a time. Copy each block into the matching box, top to bottom.", ""]

def block(label, value):
    out.extend([f"**{label}**", "```", value, "```", ""])

phone = re.search(r"\(\d{3}\) \d{3}-\d{4}", spec["contact"]).group(0)
email = re.search(r"\S+@\S+", spec["contact"]).group(0)
out.append("## Contact")
block("First name", spec["name"].split()[0].title())
block("Last name", spec["name"].split()[-1].title())
block("Phone", phone); block("Email", email)
block("City, State", "Tallahassee, FL")
out.append("## Work experience (newest first)")
for j in spec["experience"]:
    a, b = [x.strip() for x in j["dates"].split("–")]
    out.append(f"### {j['title']} · {j['org']}")
    block("Job title", j["title"]); block("Company", j["org"]); block("Location", j["where"])
    for lab, d in (("Start", a), ("End", b)):
        if d.lower() == "present": block(lab, "I currently work here"); continue
        mon, yr = d.split()
        block(f"{lab} month / year", f"{MONTHS[mon[:3]]:02d}/{yr}")
    block("Description", "\n".join("• " + x for x in j["bullets"]))
out.append("## Education")
for e in spec["education"]:
    m = re.match(r"(.+?), (.+?) — (.+?), .*\((\d{4})\)", e)
    if m:
        out.append(f"### {m.group(3)}")
        block("School", m.group(3)); block("Degree", m.group(1)); block("Field of study", m.group(2)); block("Graduation year", m.group(4))
out.append("## Certifications")
for c in spec["certs"]: block("Certification", c)
io.open(sys.argv[2], "w", encoding="utf-8", newline="\n").write("\n".join(out))
print("wrote", sys.argv[2])
