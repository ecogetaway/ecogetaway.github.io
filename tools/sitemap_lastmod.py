"""Rewrite <lastmod> in a sitemap from each page's real last-change time.

Usage: python3 sitemap_lastmod.py <sitemap_in> <sitemap_out> <base_url> [repo_root]

For every <loc>, the matching file's last commit time (ISO 8601 with time zone)
becomes its <lastmod>. A file with uncommitted changes gets the current time,
because it is about to be deployed as changed. If git is unavailable, the
existing <lastmod> is kept, so the script can never make a date less accurate.
"""
import datetime as dt, os, re, subprocess, sys

GITS = ["git", "/Library/Developer/CommandLineTools/usr/bin/git"]

def run_git(args, root):
    for g in GITS:
        try:
            r = subprocess.run([g, "-C", root] + args, capture_output=True, text=True, timeout=30)
            if r.returncode == 0:
                return r.stdout.strip()
        except (OSError, subprocess.TimeoutExpired):
            continue
    return None

def url_to_file(url, base, root):
    path = url[len(base):].lstrip("/")
    for cand in ([path] if path.endswith(".html") else []) + [path.rstrip("/") + ".html" if path else "", os.path.join(path, "index.html"), "index.html" if not path else ""]:
        if cand and os.path.isfile(os.path.join(root, cand)):
            return cand
    return None

def main():
    src, out, base = sys.argv[1], sys.argv[2], sys.argv[3].rstrip("/")
    root = sys.argv[4] if len(sys.argv) > 4 else "."
    xml = open(src, encoding="utf-8").read()
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()

    def fix(m):
        block = m.group(0)
        loc = re.search(r"<loc>(.*?)</loc>", block).group(1)
        f = url_to_file(loc, base, root)
        stamp = None
        if f:
            dirty = run_git(["status", "--porcelain", "--", f], root)
            if dirty:
                stamp = now
            elif dirty == "":
                stamp = run_git(["log", "-1", "--format=%cI", "--", f], root) or None
        if not stamp:
            return block
        if "<lastmod>" in block:
            return re.sub(r"<lastmod>.*?</lastmod>", f"<lastmod>{stamp}</lastmod>", block)
        return block.replace("</loc>", f"</loc>\n    <lastmod>{stamp}</lastmod>")

    xml = re.sub(r"<url>.*?</url>", fix, xml, flags=re.S)
    open(out, "w", encoding="utf-8").write(xml)

if __name__ == "__main__":
    main()
