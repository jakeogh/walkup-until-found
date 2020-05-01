#!/usr/bin/env python3

#import os
#import sys
import click
from pathlib import Path
from icecream import ic
ic.configureOutput(includeContext=True)
from shutil import get_terminal_size
ic.lineWrapWidth, _ = get_terminal_size((80, 20))


# DONT CHANGE FUNC NAME
@click.command()
@click.argument("starting_dir", type=click.Path(exists=True, dir_okay=True, file_okay=False, path_type=str, allow_dash=True), nargs=1, required=True)
@click.argument("name_to_find", type=str, nargs=1, required=True)
@click.option('--verbose', is_flag=True)
def cli(starting_dir, name_to_find, verbose):
    starting_dir = Path(starting_dir).resolve()
    if verbose:
        ic(starting_dir)
    assert '/' not in name_to_find
    name_to_find = Path(name_to_find)
    if verbose:
        ic(name_to_find)

    while True:
        path_guess = starting_dir / name_to_find
        if verbose:
            ic(path_guess)
        if path_guess.exists():
            print(path_guess.as_posix())
            quit(0)
        starting_dir = starting_dir.parent
        if len(starting_dir.parts) == 1:
            exit(1)


if __name__ == "__main__":
    cli()
