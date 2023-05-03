package baekjoon.BJ2108;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		List<Integer> numbers = new ArrayList<>();
		int[] count = new int[8001];

		int sum = 0;
		int min = Integer.MAX_VALUE;
		int max = Integer.MIN_VALUE;
		for (int i = 0; i < N; i++) {
			int num = Integer.parseInt(br.readLine());

			if (num < min) {
				min = num;
			}

			if (max < num) {
				max = num;
			}

			numbers.add(num);
			count[num + 4000]++;
			sum += num;
		}
		// 산술평균
		System.out.println(Math.round((double)sum / N));

		// 중앙값
		Collections.sort(numbers);
		System.out.println(numbers.get(numbers.size() / 2));

		// 최빈값
		int modeCountMax = 0;	// 최다 등장 값 (최빈값)
		int mode = 0;
		boolean flag = false;
		for (int i = min + 4000; i <= max + 4000; i++) {
			if (modeCountMax < count[i]) {
				modeCountMax = count[i];
				mode = i - 4000;
				flag = true;
			} else if (modeCountMax == count[i] && flag) {
				mode = i - 4000;
				flag = false;
			}
		}
		System.out.println(mode);

		// 범위
		System.out.println(max - min);
	}
}
