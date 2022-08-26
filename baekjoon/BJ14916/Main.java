import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// baekjoon 거스름돈 (실버5)
public class Main {
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int result = 0;

		//나머지의 개수로 접근하자
		if (N == 1 || N == 3) { // 1or3 이면 -1 리턴
			result = -1;
		} else { // 거스름돈을 5원으로 나누면 나머지는 0~4
			if (N % 5 % 2 == 0) { // 나머지가 0,2,4 인 경우 거스름돈/5 + 거스름돈%5/2
				result = N / 5 + N % 5 / 2;
			} else { //나머지가 1,3인 경우 5원을 하나 덜 사용하고 2로 나누기
				result = (N / 5 - 1) + (N % 5 + 5) / 2;
			}
		}
		System.out.println(result);
	}
}