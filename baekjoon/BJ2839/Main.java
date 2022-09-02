package baekjoon.BJ2839;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//baekjoon 설탕 배달 (실버4)
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		int result = 0;
		boolean flag = false;

		while (N >= 0) {
			if (N % 5 == 0) {
				flag = true;
				result += N / 5;
				break;
			}

			N -= 3;
			result += 1;
		}

		if (flag) {
			System.out.println(result);
		} else {
			System.out.println("-1");
		}
	}
}