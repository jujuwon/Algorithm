import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//baekjoon 주유소 (실버4)
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());

		long[] dist = new long[N-1];	//거리
		long[] cost = new long[N];	//비용

		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < N - 1; i++) {
			dist[i] = Long.parseLong(st.nextToken());
		}

		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < N; i++) {
			cost[i] = Long.parseLong(st.nextToken());
		}

		long result = 0;
		long minCost = cost[0];

		for (int i = 0; i < N - 1; i++) {
			if (cost[i] < minCost) {
				minCost = cost[i];
			}

			result += (minCost * dist[i]);
		}

		System.out.println(result);
	}
}