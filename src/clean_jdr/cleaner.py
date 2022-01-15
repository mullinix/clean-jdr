"""Methods to support cleaning files."""

# builtins
import pathlib
import re


class Cleaner:
    """File cleaner class."""

    def __init__(
        self,
        path: pathlib.Path,
        ext: str = ".jdr",
        group: bool = True,
        dry_run: bool = False,
    ) -> None:
        """Initialize file cleaner class.

        Args:
            path: path to file/directory
            ext: file extension to look for.
            group: whether to group on 3+ approved chars
                 - will also print each group on a separate line
            dry_run: will print output to stdout instead of a file
                      - otherwise, will replace `ext` with `.txt` and save file

        Returns:
            None
        """
        self.path = path
        self.ext = ext
        self.group = group
        self.dry_run = dry_run

    def _clean(self, file_: pathlib.Path) -> None:
        """Cleans a file.

        Results are stored in `self.data`.
        """
        print(f"Decoding file: {file_}")
        with open(file_, "rb") as f:
            contents = f.read()

        # ignore unresolvable bytes
        decoded = contents.decode("latin-1", "ignore")

        if self.group:
            grouped = re.findall(r"[0-9A-Za-z:\*\%\?\,\.\-\+\=]{3,}", decoded)
            self.data = "\n".join(grouped)
        else:
            self.data = re.sub(r"[^\s0-9A-Za-z:\*\%\?\,\.\-\+\=]", " ", decoded)

    def clean(self) -> None:
        """Cleans file(s) as requested."""
        if self.path.is_dir():
            for file_ in self.path.glob(f"*{self.ext}"):
                self._clean(file_)
                self.print(file_)
        else:
            self._clean(self.path)
            self.print(self.path)

    def print(self, file_: pathlib.Path) -> None:
        """Print the cleaned data.

        Prints to stdout if `self.dry_run` is True.

        Args:
            file_: path of file that was processed.
                   - used to create output file name, if self.dry_run is False.
        """
        if self.dry_run:
            print(self.data)
        else:
            stem = str(file_).strip(self.ext)
            file_out = pathlib.Path(f"{stem}.txt")
            with open(file_out, "w") as f:
                f.write(self.data)
