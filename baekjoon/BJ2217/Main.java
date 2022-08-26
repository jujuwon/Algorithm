import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

//baekjoon 로프 (실버4)
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		int w = 0;
		Integer[] weight = new Integer[N];

		for (int i = 0; i < N; i++) {
			weight[i] = Integer.parseInt(br.readLine());
		}
		Arrays.sort(weight, Collections.reverseOrder());

		for (int i = 0; i < N; i++) {
			w = Math.max(w, weight[i] * (i+1));
		}
		System.out.println(w);
	}
}