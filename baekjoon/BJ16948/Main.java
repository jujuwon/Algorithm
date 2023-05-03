package baekjoon.BJ16948;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Knight {
	int r;
	int c;
	int cnt;

	Knight(int r, int c, int cnt) {
		this.r = r;
		this.c = c;
		this.cnt = cnt;
	}
}

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	static int N;
	static int[][] map;
	static boolean[][] visited;
	static int[] dr = {-2, -2, 0, 0, 2, 2};
	static int[] dc = {-1, 1, -2, 2, -1, 1};
	static int r1, c1;
	static int r2, c2;

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());

		map = new int[N][N];
		visited = new boolean[N][N];

		r1 = Integer.parseInt(st.nextToken());
		c1 = Integer.parseInt(st.nextToken());
		r2 = Integer.parseInt(st.nextToken());
		c2 = Integer.parseInt(st.nextToken());

		System.out.println(bfs());
	}

	static int bfs() {
		Queue<Knight> queue = new LinkedList<>();
		queue.add(new Knight(r1, c1, 0));
		visited[r1][c1] = true;

		while (!queue.isEmpty()) {

			Knight k = queue.poll();

			for (int i = 0; i < 6; i++) {
				int rr = k.r + dr[i];
				int cc = k.c + dc[i];

				// 맵 경계검사, 방문 체크
				if (rr < 0 || cc < 0 || rr >= N || cc >= N || visited[rr][cc]) continue;
				// 도착지 도달 체크
				if (rr == r2 && cc == c2) {
					return k.cnt + 1;
				}
				// 다시 큐에 넣어서 탐색
				visited[rr][cc] = true;
				queue.add(new Knight(rr, cc, k.cnt + 1));
			}
		}

		return -1;
	}
}
