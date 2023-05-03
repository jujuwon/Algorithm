package baekjoon.BJ15900;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static ArrayList<Integer>[] graph;
	static boolean[] visited = new boolean[500001];
	static int cnt = 0;

	public static void main(String[] args) throws IOException {

		int N = Integer.parseInt(br.readLine());

		graph = new ArrayList[N + 1];
		for (int i = 1; i <= N; i++) {
			graph[i] = new ArrayList<>();
		}

		for (int i = 0; i < N-1; i++) {
			st = new StringTokenizer(br.readLine(), " ");

			int firstNode = Integer.parseInt(st.nextToken());
			int secondNode = Integer.parseInt(st.nextToken());

			graph[firstNode].add(secondNode);
			graph[secondNode].add(firstNode);
		}

		dfs(1, 0);
		System.out.println((cnt % 2 == 0) ? "No" : "Yes");
	}

	public static void dfs(int node, int depth) {
		boolean flag = true;
		visited[node] = true;
		for (int v : graph[node]) {
			if (!visited[v]) {
				flag = false;
				dfs(v, depth + 1);
			}
		}
		if (flag) { // 방문할 노드가 없다 -> 리프노드 ?
			cnt += depth;
		}
	}
}
