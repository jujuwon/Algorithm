import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

//baekjoon 알바생 강호 (실버4)
public class Main {
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		Long[] list = new Long[N];

		for (int i = 0; i < N; i++) {
			list[i] = Long.parseLong(br.readLine());
		}

		Arrays.sort(list, Collections.reverseOrder());

		long tip = 0;

		for (int i = 0; i < N; i++) {
			long n = list[i] - i;
			if (n > 0) {
				tip += n;
			}
		}
		System.out.println(tip);
	}
}