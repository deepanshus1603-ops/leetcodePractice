class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(d: int, x1: int, x2: int) -> int:
            y1, y2 = d - x1, d - x2
            for x, y in [(x1, y1), (x2, y2)]:
                if not (0 <= x < n and 0 <= y < n and grid[y][x] >= 0):
                    return lower_boundary
            if d == 2 * (n-1):
                return lower_boundary if grid[n-1][n-1] == -1 else grid[n-1][n-1]
            res = max(dp(d+1, x1+dx1, x2+dx2) for dx1, dx2 in [(0, 0), (1, 0), (0, 1), (1, 1)])
            return res + grid[y1][x1] + (grid[y2][x2] * (x1 != x2))
            
        n = len(grid)
        lower_boundary = - 2 * 2 * (n-1)
        return max(dp(0, 0, 0), 0)
        
            
