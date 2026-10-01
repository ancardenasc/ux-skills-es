"""Ejecuta un skill de verdad con `claude -p` sobre un fixture y compara con lo esperado.

Opt-in: usa tu sesión de Claude Code y consume cuota. No se ejecuta en el CI.
Uso: python tests/evals/run_eval.py [skill] [fixture]   (por defecto wcag22-audit html-seeded)
"""
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

import compare  # noqa: E402
import yaml  # noqa: E402


def main():
    skill = sys.argv[1] if len(sys.argv) > 1 else "wcag22-audit"
    name = sys.argv[2] if len(sys.argv) > 2 else "html-seeded"
    fixture = ROOT / "tests" / "fixtures" / name
    plugin = ROOT / "plugins" / skill
    extra = ' --tarea "Hacer, guardar y, si hace falta, eliminar un pedido de café"' if skill == "heuristic-review-es" else ""
    cmd = ["claude", "-p", f"/{skill}:{skill} . --idioma es{extra}",
           "--plugin-dir", str(plugin), "--add-dir", str(plugin),
           "--permission-mode", "acceptEdits",
           "--allowedTools", "Read Glob Grep Bash(git:*) Bash(ls:*) Bash(cat:*)",
           "--output-format", "text"]
    res = subprocess.run(cmd, cwd=fixture, capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=900)
    out = Path(tempfile.gettempdir()) / f"eval-{skill}-{name}.md"
    out.write_text(res.stdout, encoding="utf-8")
    expected = yaml.safe_load((fixture / "expected.yml").read_text(encoding="utf-8"))
    r = compare.compare(res.stdout, expected)
    print(f"informe guardado en {out}")
    print({k: r[k] for k in ("valid", "recall", "missed", "decoys_flagged", "manual_wrong", "extra_fails")})
    sys.exit(0 if r["valid"] and not (r["missed"] or r["decoys_flagged"] or r["manual_wrong"]) else 1)


if __name__ == "__main__":
    main()
