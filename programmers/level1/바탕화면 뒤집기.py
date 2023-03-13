def solution(wallpaper):
    answer = []
    n,m = len(wallpaper), len(wallpaper[0])
    start_pos, end_pos = [n-1,m-1],[0,0]
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == '#':
                if start_pos[0] > i:
                    start_pos[0] = i
                if start_pos[1] > j:
                    start_pos[1] = j
                if end_pos[0] < i:
                    end_pos[0] = i
                if end_pos[1] < j:
                    end_pos[1] = j
    print(start_pos, end_pos)
    return answer
solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]	)