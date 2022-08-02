import java.util.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        
        int correctCnt = 0; // 일치횟수
        int zeroCnt = 0; // 0 의 개수
        
        for (int lotto : lottos) {
            if (lotto == 0) {
                zeroCnt++;
            } else if (Arrays.stream(win_nums).anyMatch(i -> i == lotto)) {
                correctCnt++;
            }
        }
        
        Map<Integer, Integer> map = new HashMap<>();
        for (int i=6; i > 0; i--) {
            map.put(i, 7-i);
        }
        map.put(0, 6);
        
        return new int[]{map.get(correctCnt + zeroCnt), map.get(correctCnt)};
    }
}