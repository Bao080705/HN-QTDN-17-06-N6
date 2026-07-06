import os
import shutil
import zipfile
from pathlib import Path

root = Path(r"c:/Users/Admin/Documents/TTDN-16-01-N1-main/TTDN-16-01-N1-main/addons/nhan_su")
out = Path(r"c:/Users/Admin/Documents/TTDN-16-01-N1-main/TTDN-16-01-N1-main/addons/nhan_su.zip")

if not root.exists():
    raise SystemExit(f"Missing folder: {root}")

for path in sorted(root.rglob('*'), reverse=True):
    try:
        if path.is_dir() and path.name == '__pycache__':
            shutil.rmtree(path)
        elif path.is_file() and ('Zone.Identifier' in path.name or path.suffix == '.pyc'):
            path.unlink()
    except Exception as e:
        print(f"skip {path}: {e}")

if out.exists():
    out.unlink()

with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
    for path in sorted(root.rglob('*')):
        if path.is_file():
            arcname = f"nhan_su/{path.relative_to(root).as_posix()}"
            z.write(path, arcname=arcname)

print(f"Created {out}")
with zipfile.ZipFile(out) as z:
    names = z.namelist()
    print(f"Entries: {len(names)}")
    for name in names[:20]:
        print(name)
