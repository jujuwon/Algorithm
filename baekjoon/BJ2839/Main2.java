package baekjoon.BJ2839;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// //baekjoon 설탕 배달 (실버4) - dp 로 푼 버전
public class Main2 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int N;
	static int[] dp = new int[5001];

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());

		dp[0] = -1;
		dp[1] = -1;
		dp[2] = -1;
		dp[3] = 1;
		dp[4] = -1;

		for (int i = 5; i <= 5000; i++) {
			int min = Integer.MAX_VALUE;
			if (i % 5 == 0) {
				min = (i / 5);
			}
			if (dp[i - 5] != -1) {
				if (dp[i - 5] + 1 < min) {
					min = dp[i - 5] + 1;
				}
			}
			if (dp[i - 3] != -1) {
				if (dp[i - 3] + 1 < min) {
					min = dp[i - 3] + 1;
				}
			}
			if (i % 3 == 0) {
				if ((i / 3) < min) {
					min = (i / 3);
				}
			}
			if (min == Integer.MAX_VALUE) {
				dp[i] = -1;
			} else {
				dp[i] = min;
			}
		}

		System.out.println(dp[N]);
	}
}
