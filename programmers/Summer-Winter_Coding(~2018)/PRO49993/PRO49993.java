import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
            
        List<Character> order = new ArrayList<>();
        for (int i=0; i < skill.length(); i++) {
            order.add(skill.charAt(i));
        }
        
        
        for (int i = 0; i < skill_trees.length; i++) {
            char[] s = skill_trees[i].toCharArray();
            int cur = -1;
            boolean flag = false;
            for (int j=0; j < s.length; j++) {
                // order 에 있는 스킬인지 확인하기
                if(order.contains(s[j])){
                    if (order.get(cur+1) != s[j]) {
                        flag = true;
                        break;
                    }
                    else {
                        cur++;
                    }
                }
            }
            if (!flag) {
                answer++;
            }
                
        }
        
        return answer;
    }
}