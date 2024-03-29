#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path

import click
from clicktool import click_add_options
from clicktool import click_global_options
from clicktool import tv
from epprint import epprint
from mptool import output


def walkup_until_found(
    *,
    path: Path,
    name: str,
    verbose: bool | int | float = False,
) -> Path:
    name_to_find = name
    starting_dir = Path(path).resolve()
    if not starting_dir.is_dir():
        starting_dir = starting_dir.parent
    if verbose:
        epprint(f"{starting_dir=}")
    assert "/" not in name_to_find
    name_to_find = Path(name_to_find)
    if verbose:
        epprint(f"{name_to_find=}")

    while True:
        path_guess = starting_dir / name_to_find
        if path_guess.exists():
            if verbose:
                epprint("found:", f"{path_guess=}")
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
@click_add_options(click_global_options)
@click.pass_context
def cli(
    ctx,
    *,
    starting_dir: Path,
    name_to_find: str,
    verbose_inf: bool,
    dict_output: bool,
    verbose: bool | int | float = False,
):
    tty, verbose = tv(
        ctx=ctx,
        verbose=verbose,
        verbose_inf=verbose_inf,
    )

    result = walkup_until_found(
        path=starting_dir,
        name=name_to_find,
    )

    output(
        result.as_posix(),
        reason=name_to_find,
        dict_output=dict_output,
        tty=tty,
    )
