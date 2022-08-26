import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int[] fibo = new int[21];
		fibo[0] = 0;
		fibo[1] = 1;

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		for (int i = 2; i <= n; i++) {
			fibo[i] = fibo[i - 2] + fibo[i - 1];
		}

		System.out.println(fibo[n]);
        sc.close();
    }
}
