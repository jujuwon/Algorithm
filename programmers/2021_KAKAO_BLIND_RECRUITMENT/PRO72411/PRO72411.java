import java.util.*;
import java.lang.StringBuilder;

// Lv2. 메뉴 리뉴얼
class Solution {
    
    static Map<String, Integer> map;
    
    public static void cb(String str, StringBuilder sb, int idx, int cnt, int n) {
        if (cnt == n) {
            map.put(sb.toString(), map.getOrDefault(sb.toString(), 0) + 1);
            return;
        }
        
        for (int i=idx; i < str.length(); i++) {
            sb.append(str.charAt(i));
            cb(str, sb, i+1, cnt+1, n);
            sb.delete(cnt, cnt+1);
        }
    }
    
    public String[] solution(String[] orders, int[] course) {
        List<String> result = new ArrayList<>();
        
        // orders 에 있는 주문들을 course 에서 요구하는 개수만큼 조합해서 맵으로 저장.
        // 정렬하기
        for (int i=0; i < orders.length; i++) {
            char[] newArr = orders[i].toCharArray();
            Arrays.sort(newArr);
            orders[i] = String.valueOf(newArr);
        }
        
        for (int i=0; i < course.length; i++) {
            map = new HashMap<>();
            for (int j=0; j < orders.length; j++) {
                StringBuilder sb = new StringBuilder();
                if (course[i] <= orders[j].length()) {
                    cb(orders[j], sb, 0, 0, course[i]);
                }
            }
            
            int max = Integer.MIN_VALUE;
            // 가장 많이 주문된 조합 찾기
            for (Map.Entry<String, Integer> entry : map.entrySet()) {
                if (max < entry.getValue()) {
                    max = entry.getValue();
                }
            }

            if (max < 2) continue;
            // map 에서 주문횟수가 가장 많은 조합 찾기
            for (Map.Entry<String, Integer> entry : map.entrySet()) {
                if (max == entry.getValue()) {
                    result.add(entry.getKey());
                }
            }
        }
        
        Collections.sort(result);
        int len = result.size();
        String[] answer = result.toArray(new String[len]);
        
        return answer;
    }
}