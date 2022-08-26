import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();

		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt(); // 명령의 수

		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < N; i++) {
			String line = scanner.next();
			if (line.startsWith("push")) {
				stack.push(scanner.nextInt());
			} else if (line.equals("pop")) {
				if (stack.empty()) {
					sb.append("-1\n");
				} else {
					sb.append(stack.pop()).append("\n");
				}
			} else if (line.equals("size")) {
				sb.append(stack.size()).append("\n");
			} else if (line.equals("empty")) {
				if (stack.empty()) {
					sb.append("1\n");
				} else {
					sb.append("0\n");
				}
			} else if (line.equals("top")) {
				if (stack.empty()) {
					sb.append("-1\n");
				} else {
					sb.append(stack.peek()).append("\n");
				}
			}
		}

		System.out.println(sb);
        scanner.close();
    }
}
