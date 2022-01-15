"""Command line interface for clean-jdr.

See https://docs.python.org/3/using/cmdline.html#cmdoption-m for why module is
named __main__.py.
"""

# builtins
import pathlib

# 3rd party/FOSS
from typer import Typer

# this
from clean_jdr.cleaner import Cleaner

app = Typer(help="Clean output files (.jdr) from wire sniffing.")


@app.command()
def clean(
    path: pathlib.Path,
    ext: str = ".jdr",
    group: bool = True,
    dry_run: bool = False,
) -> None:
    """Clean data from file(s)."""
    cleaner = Cleaner(path, ext, group, dry_run)
    cleaner.clean()


if __name__ == "__main__":
    app()
