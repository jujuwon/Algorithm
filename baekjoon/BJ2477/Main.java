package baekjoon.BJ2477;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int K = Integer.parseInt(br.readLine());

		/**
		 * 방향이 한번씩 등장하는지, 두번씩 등장하는지 확인하기
		 * 한번씩 등장하는 방향은 큰 사각형의 너비/높이로 사용
		 * 두번씩 등장하는 방향은 작은 사각형의 너비/높이로 사용
		 * 1: EAST
		 * 2: WEST
		 * 3: SOUTH
		 * 4: NORTH
		 */
		int[][] arr = new int[6][2];
		int[] cnt = new int[4 + 1];

		for (int i = 0; i < 6; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int direction = Integer.parseInt(st.nextToken());
			arr[i][0] = direction;
			arr[i][1] = Integer.parseInt(st.nextToken());
			cnt[direction]++;
		}

		int big = 1;
		int small = 1;

		for (int i = 0; i < 6; i++) {
			if (cnt[arr[i][0]] == 1) {
				// 한번 등장한 방향
				big *= arr[i][1];
				continue;
			}

			// 두번 등장한 방향
			// 지금 방향이랑 다음다음 방향이 같으면, 다음 방향은 작은 사각형의 너비/높이!
			// 다음 방향
			int n = (i + 1) % 6;
			int nn = (i + 2) % 6;
			if (arr[i][0] == arr[nn][0])
				small *= arr[n][1];
		}

		System.out.println((big - small) * K);
	}
}
