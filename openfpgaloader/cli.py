from functools import lru_cache
from pathlib import Path
from shutil import which
from subprocess import Popen
from sys import exit, stderr, stdout
from time import sleep


@lru_cache(maxsize=1)
def _get_openfpgaloader() -> str:
    exe = which("openFPGALoader")
    if not exe:
        root = Path(__file__).parent.resolve()
        exe = str((root / "bin" / "openFPGALoader").resolve())
    return exe


def openfpgaloader(argv):
    build_cmd = [
        _get_openfpgaloader(),
        *argv,
    ]
    process = Popen(build_cmd, stderr=stderr, stdout=stdout)
    while process.poll() is None:
        sleep(0.1)
    if process.returncode != 0:
        exit(process.returncode)


def main():
    from sys import argv as _argv

    openfpgaloader(_argv[1:])
