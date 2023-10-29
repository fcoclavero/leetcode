"""

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.

# Examples

Example 1:

Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
Output: 3

# Constraints

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from typing import List


class Solution:
    """
    - Left to right, top to bottom traversal.
    - At each coordinate:
        - Check top and left neighbors. If all water, create new island.
        - If only one is land, add new coordinate to island
        - If both are land, merge islands and add.
    - O[n x m]

    # Examples

    Example 3:

    Input: grid = [
        ["0","0","1","0","0"],
        ["0","1","1","0","0"],
        ["1","1","1","0","0"],
        ["0","0","0","1","1"]
    ]

    Example 4:

    Input: grid = [
        ["0","1","0","0","1"],
        ["1","1","0","1","1"],
        ["1","1","1","0","0"],
        ["0","0","0","1","1"]
    ]
    """
    def numIslands(self, grid: List[List[str]]) -> int:

        class Island:
            def __init__(self):
                self.link: "Island" = None

            @property
            def root_island(self) -> "Island":
                if self.link is None:
                    return self
                else:
                    return self.link.root_island

        def merge_islands(island_1: Island, island_2: Island) -> Island:
            new_root = Island()
            island_1.root_island.parent = new_root
            island_2.root_island.parent = new_root
            return new_root

        island_mapping: dict[int, dict[int, Island]] = {}

        for i, row in enumerate(grid):
            for j, tile in row:
                if tile:
                    try:
                        left = island_mapping[i][j - 1]
                    except IndexError:
                        left = None
                    try:
                        top = island_mapping[i - 1][j]
                    except IndexError:
                        top = island_mapping[i - 1][j]

                    if left and top:
                        island_mapping[i][j] = merge_islands(left, top)

                    elif left and not top:
                        island_mapping[i][j] = left

                    elif not left and top:
                        island_mapping[i][j] = top

                    else:
                        island_mapping[i][j] = Island()

        return
