package baekjoon.BJ6986;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		List<String> answer = new ArrayList<>();

		double[] scores = new double[N];

		for (int i = 0; i < N; i++) {
			scores[i] = Double.parseDouble(br.readLine());
		}
		Arrays.sort(scores);

		double sum = 0;
		for (int i = K; i < N - K; i++) {
			sum += scores[i];
		}
		// answer.add(Math.round(sum / ((N - K) - K) * 100) / 100.0);
		answer.add(String.format("%.2f", sum / ((N - K) - K)));

		for (int i = 0; i < K; i++) {
			scores[i] = scores[K];
			scores[N - 1 - i] = scores[N - K - 1];
		}

		sum = 0;
		for (double score : scores) {
			sum += score;
		}
		// answer.add(Math.round(sum / N * 100) / 100.0);
		answer.add(String.format("%.2f", sum / N));

		for (String ans : answer) {
			System.out.println(ans);
		}
	}
}
