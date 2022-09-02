import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//baekjoon 트리 순회 (실버1)
public class Main {

	static Node head = new Node('A', null, null);

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());

		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			char root = st.nextToken().charAt(0);
			char left = st.nextToken().charAt(0);
			char right = st.nextToken().charAt(0);

			insertNode(head, root, left, right);
		}

		preOrder(head);
		System.out.println();
		inOrder(head);
		System.out.println();
		postOrder(head);
	}

	static class Node {
		char value;
		Node left;
		Node right;

		Node(char value, Node left, Node right) {
			this.value = value;
			this.left = left;
			this.right = right;
		}
	}

	public static void insertNode(Node node, char root, char left, char right) {
		if (node.value == root) {	//insert 대상 node 찾음
			node.left = (left == '.') ? null : new Node(left, null, null);
			node.right = (right == '.') ? null : new Node(right, null, null);
		} else {	//insert 대상 node 못 찾음
			if (node.left != null) insertNode(node.left, root, left, right);
			if (node.right != null) insertNode(node.right, root, left, right);
		}
	}

	public static void preOrder(Node node) {	//root -> left -> right
		if (node == null) return;
		System.out.print(node.value);
		preOrder(node.left);
		preOrder(node.right);
	}

	public static void inOrder(Node node) {	//left -> root -> right
		if (node == null) return;
		inOrder(node.left);
		System.out.print(node.value);
		inOrder(node.right);
	}

	public static void postOrder(Node node) {	//left -> right -> root
		if (node == null) return;
		postOrder(node.left);
		postOrder(node.right);
		System.out.print(node.value);
	}
}