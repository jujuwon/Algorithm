package baekjoon.BJ2805;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N;
	static int M;

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		int[] arr = new int[N];

		int max = Integer.MIN_VALUE;
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			int temp = Integer.parseInt(st.nextToken());
			if (max < temp) {
				max = temp;
			}
			arr[i] = temp;
		}

		int left = 0;
		int right = max;

		// 이진 탐색
		while (left <= right) {
			int H = (left + right) / 2;

			long sum = 0;
			for (int i = 0; i < N; i++) {
				int temp = arr[i] - H;
				if (temp > 0) {
					sum += temp;
				}
			}
			if (M <= sum) {
				left = H + 1;
			} else {
				right = H - 1;
			}
		}

		System.out.println(right);
	}
}
