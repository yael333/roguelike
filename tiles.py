from typing import Tuple

import numpy as np

graphic_dt = np.dtype(
    [
        ("ch", np.int32), # unicode codepoint
        ("fg", "3B"), # 3 unsigned bytes, for RGB colors.
        ("bg", "3B"),
    ]
)

tile_dt = np.dtype(
    [
        ("walkable", np.bool_), # true if this tile can be walked over.
        ("transparent", np.bool_), # true if this tile doesn't block FOV.
        ("dark", graphic_dt), # graphics for when this tile is not in FOV.
        ("light", graphic_dt), # graphics for when the tile is in FOV.
    ]
)

def new_tile(
    *,
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)



# SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord(" "), (255, 255, 255), (0x28, 0x28, 0x28)), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255, 255, 255), (0xa8, 0x99, 0x84)),
    light=(ord(" "), (255, 255, 255), (0xeb, 0xdb, 0xb2)),
)

wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (255, 255, 255), (0x3c, 0x38, 0x36)),
    light=(ord(" "), (255, 255, 255), (0xa8, 0x99, 0x84)),
)