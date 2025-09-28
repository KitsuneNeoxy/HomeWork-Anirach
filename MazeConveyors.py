from collections import deque

def maze_solver_with_conveyors(maze: list[list[str]]) -> dict:
    rows, cols = len(maze), len(maze[0])

  
    directions = {
        ">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
        "v": (1, 0)
    }
  
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


    start = end = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == "S":
                start = (r, c)
            elif maze[r][c] == "E":
                end = (r, c)

    if not start or not end:
        return {"distance": -1, "path": []}


    q = deque()
    q.append((start[0], start[1], 0, [list(start)]))  # row, col, dist, path
    visited = set()
    visited.add(start)

    while q:
        r, c, dist, path = q.popleft()

        if (r, c) == end:
            return {"distance": dist, "path": path}

     
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if maze[nr][nc] == "#":
                continue
            if (nr, nc) in visited:
                continue

            new_path = path + [[nr, nc]]

           
            cr, cc = nr, nc
            while (maze[cr][cc] in directions):
                ddr, ddc = directions[maze[cr][cc]]
                tr, tc = cr + ddr, cc + ddc
                if not (0 <= tr < rows and 0 <= tc < cols):
                    break
                if maze[tr][tc] == "#":
                    break
                if (tr, tc) in visited:
                    break
                new_path.append([tr, tc])
                cr, cc = tr, tc

            if (cr, cc) not in visited:
                visited.add((cr, cc))
                q.append((cr, cc, dist + 1, new_path))

    return {"distance": -1, "path": []}
   
    pass



if __name__ == "__main__":
    maze = [
        ['S', '.', '>', '>', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {'distance': 2, 'path': [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]}

    maze = [
        ['S', '.', '>', '#', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {"distance": -1, "path": []}


    maze = [
        ['S', '.', 'v', '.', 'E'],
        ['#', '#', 'v', '.', '#'],
        ['.', '.', 'v', '.', '.'],
        ['#', '#', '.', '.', '#'],
        ['.', '.', '.', '.', '.']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {'distance': 7, 'path': [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [3, 3], [2, 3], [1, 3], [0, 3], [0, 4]]}
