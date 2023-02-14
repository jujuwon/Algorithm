package baekjoon.BJ2558;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

//baekjoon A+B-2 (브론즈5)
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
		int b = Integer.parseInt(br.readLine());
		System.out.println(a+b);
	}
}

