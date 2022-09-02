package baekjoon.BJ2748;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//baekjoon 피보나치 수 2 (브론즈1)
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		long[] fibo = new long[91];

		fibo[0] = 0;
		fibo[1] = 1;

		int n = Integer.parseInt(br.readLine());

		for (int i = 2; i <= n; i++) {
			fibo[i] = fibo[i - 1] + fibo[i - 2];
		}

		System.out.println(fibo[n]);
	}
}