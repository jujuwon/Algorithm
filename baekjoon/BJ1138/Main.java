package baekjoon.BJ1138;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int[] line = new int[N];
		List<Integer> answer = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			line[i] = Integer.parseInt(st.nextToken());
		}

		for (int i = N-1; i >= 0; i--) {
			/**
			 * 키를 내림차순으로 돌면서 숫자를 확인
			 * 앞에 몇명인지를 확인하고 해당 인덱스에다가 넣어주기
			 * 내림차순이기 때문에 해당 인덱스에 넣으면 그 앞에 본인보다 큰 사람이 들어감
			 */
			answer.add(line[i], i + 1);
		}

		for (int i : answer) {
			System.out.print(i + " ");
		}
	}
}
