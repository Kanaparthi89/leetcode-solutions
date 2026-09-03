class Solution {
public:
    int minMoves(vector<string>& classroom, int energy) {
        int m = classroom.size();
        int n = classroom[0].size();

        int sr = -1, sc = -1;
        vector<vector<int>> litterId(m, vector<int>(n, -1));

        int litterCount = 0;

        // Find start and assign an ID to every litter cell.
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (classroom[i][j] == 'S') {
                    sr = i;
                    sc = j;
                }

                if (classroom[i][j] == 'L') {
                    litterId[i][j] = litterCount++;
                }
            }
        }

        // No litter to collect.
        if (litterCount == 0)
            return 0;

        int fullMask = (1 << litterCount) - 1;

        /*
            visited[r][c][mask][e]

            Since m,n <= 20
            mask <= 1024
            energy <= 50

            Maximum states:
            20 * 20 * 1024 * 51 ~= 20 million

            Using a flat vector<char> keeps memory reasonable.
        */

        int E = energy + 1;
        int MASKS = 1 << litterCount;

        auto id = [&](int r, int c, int mask, int e) {
            return (((r * n + c) * MASKS + mask) * E + e);
        };

        vector<char> visited(m * n * MASKS * E, false);

        struct State {
            int r, c;
            int mask;
            int e;
            int dist;
        };

        queue<State> q;

        int startId = id(sr, sc, 0, energy);
        visited[startId] = true;

        q.push({sr, sc, 0, energy, 0});

        int dr[] = {1, -1, 0, 0};
        int dc[] = {0, 0, 1, -1};

        while (!q.empty()) {
            State cur = q.front();
            q.pop();

            // All litter collected.
            if (cur.mask == fullMask)
                return cur.dist;

            // Cannot make another move if energy is 0.
            if (cur.e == 0)
                continue;

            for (int d = 0; d < 4; d++) {
                int nr = cur.r + dr[d];
                int nc = cur.c + dc[d];

                // Outside grid.
                if (nr < 0 || nr >= m || nc < 0 || nc >= n)
                    continue;

                // Obstacle.
                if (classroom[nr][nc] == 'X')
                    continue;

                int newEnergy = cur.e - 1;

                // Collect litter if present.
                int newMask = cur.mask;

                if (classroom[nr][nc] == 'L') {
                    int k = litterId[nr][nc];
                    newMask |= (1 << k);
                }

                // Reset energy on R.
                if (classroom[nr][nc] == 'R') {
                    newEnergy = energy;
                }

                int stateId = id(nr, nc, newMask, newEnergy);

                if (!visited[stateId]) {
                    visited[stateId] = true;

                    q.push({
                        nr,
                        nc,
                        newMask,
                        newEnergy,
                        cur.dist + 1
                    });
                }
            }
        }

        return -1;
    }
};