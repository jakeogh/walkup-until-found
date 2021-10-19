#!/usr/bin/env python3

#import os
#import sys
from pathlib import Path

import click
from asserttool import ic


def walkup_until_found(*,
                       path: Path,
                       name: str,
                       verbose: bool,
                       debug: bool,):

    name_to_find = name
    starting_dir = Path(path).resolve()
    assert starting_dir.is_dir()
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
            return path_guess.as_posix()

        starting_dir = starting_dir.parent
        if len(starting_dir.parts) == 1:
            raise FileNotFoundError(name_to_find)



@click.command()
@click.argument("starting_dir", type=click.Path(exists=True,
                                                dir_okay=True,
                                                file_okay=False,
                                                path_type=Path,
                                                allow_dash=True,), nargs=1, required=True)
@click.argument("name_to_find", type=str, nargs=1, required=True)
@click.option('--verbose', is_flag=True)
@click.option('--debug', is_flag=True)
def cli(starting_dir: Path,
        name_to_find: str,
        verbose: bool,
        debug: bool,
        ):

    result = walkup_until_found(path=starting_dir, name=name_to_find, verbose=verbose, debug=debug)
    print(result)
