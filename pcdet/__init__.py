import subprocess
from pathlib import Path

from .version import __version__

__all__ = [
    '__version__'
]


def get_git_commit_number():
    if not (Path(__file__).parent / '../.git').exists():
        return '0000000'

    cmd_out = subprocess.run(['git', 'rev-parse', 'HEAD'], stdout=subprocess.PIPE)
    return cmd_out.stdout.decode('utf-8')[:7]


script_version = get_git_commit_number()


if script_version not in __version__:
    __version__ = f'{__version__}+py{script_version}'
