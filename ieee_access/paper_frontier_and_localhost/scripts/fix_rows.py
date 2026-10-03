"""Repair rows whose unquoted system name carried commas (the Mem0 vendor refresh row)."""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "..", "supplementary", "p3_refresh_2026-10.csv")
with open(P, encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))
hdr, out, fixed = rows[0], [rows[0]], 0
for r in rows[1:]:
    if r[1].startswith("Mem0 Platform (2026 refresh"):
        # collapse the shattered name/venue fields back into the 15 (+master_alias) columns
        joined = ",".join(r[1:5])  # "Mem0 Platform (2026 refresh: history, feedback, expiration, decay), 3, 2026, docs..."
        name = "Mem0 Platform (2026 refresh: history, feedback, expiration, decay)"
        rest = joined[len(name):].lstrip(", ").split(", ", 2)  # ["3", "2026", "docs... (venue, may contain ', ')"]
        venue_and_more = rest[2] if len(rest) > 2 else ""
        new = [r[0], name, rest[0].strip(), rest[1].strip(), venue_and_more.strip()] + r[5:]
        if len(new) != len(hdr):
            # venue may have been split further; rejoin until lengths match
            extra = len(new) - len(hdr)
            new = new[:4] + [", ".join(new[4:5 + extra])] + new[5 + extra:]
        r = new; fixed += 1
    out.append(r)
with open(P, "w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(out)
bad = [r for r in out[1:] if len(r) != len(hdr) or not r[2].strip().replace(".", "").isdigit()]
print("fixed", fixed, "| remaining malformed:", len(bad), [b[1][:40] for b in bad])
