package baekjoon.BJ1343;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();

		String a = str.replaceAll("XXXX", "AAAA");
		String b = a.replaceAll("XX", "BB");

		if (b.contains("X")) {
			System.out.println("-1");
		} else {
			System.out.println(b);
		}
    }
}
