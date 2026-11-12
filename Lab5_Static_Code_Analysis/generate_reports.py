"""Generate before-and-after reports for the three lab analysis tools."""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
REPORTS = ROOT / "reports"
TOOLS = {
    "pylint": [sys.executable, "-m", "pylint"],
    "bandit": [sys.executable, "-m", "bandit", "-r"],
    "flake8": [sys.executable, "-m", "flake8"],
}
FILES = {
    "before": ROOT / "address_book_before.py",
    "after": ROOT / "address_book.py",
}


def run_tool(tool_name, command, source_file, output_file):
    """Run one analyzer and save its output, preserving its exit status."""
    result = subprocess.run(
        command + [str(source_file)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    output = result.stdout
    if result.stderr:
        output += "\n[stderr]\n" + result.stderr
    output_file.write_text(output, encoding="utf-8")
    print(f"{tool_name}: saved {output_file.relative_to(ROOT)} (exit {result.returncode})")


def main():
    """Generate all six reports."""
    for stage, source_file in FILES.items():
        stage_dir = REPORTS / stage
        stage_dir.mkdir(parents=True, exist_ok=True)
        for tool_name, command in TOOLS.items():
            run_tool(
                tool_name,
                command,
                source_file,
                stage_dir / f"{tool_name}_report.txt",
            )


if __name__ == "__main__":
    main()
