#!/usr/bin/env python3

from pathlib import Path
from typing import Union

import click
# from asserttool import ic
from clicktool import click_add_options
from clicktool import click_global_options
from clicktool import tv
from epprint import epprint
from mptool import output


def walkup_until_found(
    *,
    path: Path,
    name: str,
    verbose: Union[bool, int, float],
) -> Path:

    name_to_find = name
    starting_dir = Path(path).resolve()
    if not starting_dir.is_dir():
        starting_dir = starting_dir.parent
    if verbose:
        epprint(starting_dir)
    assert "/" not in name_to_find
    name_to_find = Path(name_to_find)
    if verbose:
        epprint(name_to_find)

    while True:
        path_guess = starting_dir / name_to_find
        if verbose:
            epprint(path_guess)
        if path_guess.exists():
            return path_guess

        starting_dir = starting_dir.parent
        if len(starting_dir.parts) == 1:
            raise FileNotFoundError(name_to_find)


@click.command()
@click.argument(
    "starting_dir",
    type=click.Path(
        exists=True,
        dir_okay=True,
        file_okay=False,
        path_type=Path,
        allow_dash=True,
    ),
    nargs=1,
    required=True,
)
@click.argument("name_to_find", type=str, nargs=1, required=True)
@click.option("--verbose", is_flag=True)
@click_add_options(click_global_options)
@click.pass_context
def cli(
    ctx,
    *,
    starting_dir: Path,
    name_to_find: str,
    verbose: Union[bool, int, float],
    verbose_inf: bool,
    dict_input: bool,
):

    tty, verbose = tv(
        ctx=ctx,
        verbose=verbose,
        verbose_inf=verbose_inf,
    )

    result = walkup_until_found(
        path=starting_dir,
        name=name_to_find,
        verbose=verbose,
    )

    output(
        result.as_posix(),
        reason=name_to_find,
        dict_input=dict_input,
        tty=tty,
        verbose=verbose,
    )
