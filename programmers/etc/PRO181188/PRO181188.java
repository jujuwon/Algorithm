import java.util.Arrays;
// Lv2. 요격 시스템
class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        
        Arrays.sort(targets, (o1, o2) -> {
            if (o1[1] == o2[1]) {
                return o1[0] - o2[0];
            }
            return o1[1] - o2[1];
        });
        
        int e = 0;
        for (int i=0; i < targets.length; i++) {
            if (e <= targets[i][0]) {
                answer++;
                e = targets[i][1];
            }
        }
        
        return answer;
    }
}