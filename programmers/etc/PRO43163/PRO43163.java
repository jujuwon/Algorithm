import java.util.Queue;
import java.util.LinkedList;

// Lv3. 단어 변환
class Solution {
    
    static int len;
    
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        
        len = begin.length();
        
        boolean[] visited = new boolean[words.length];
        Queue<Word> queue = new LinkedList<>();
        queue.add(new Word(begin, 0));
        
        // words (50개) 문자 중에서 바꿀 수 있는 문자가 있는지 확인하기 -> 하나의 문자만 바꿔서 words 의 문자가 되어야 함
        // 바꾼 문자를 queue 에 넣기
        while (!queue.isEmpty()) {
            
            Word w = queue.poll();
            
            if (w.str.equals(target)) {
                answer = w.cnt;
                break;
            }
            
            for (int i = 0; i < words.length; i++) {
                if (visited[i]) continue;
                int correctCnt = 0;
                for (int j=0; j < len; j++) {
                    if (words[i].charAt(j) == w.str.charAt(j)) {
                        correctCnt++;
                    }
                }
                if ((len - correctCnt) == 1) {
                    queue.add(new Word(words[i], w.cnt + 1));
                    visited[i] = true;
                }
            }
        }
        
        return answer;
    }
    
    class Word {
        String str;
        int cnt;
        Word(String str, int cnt) {
            this.str = str;
            this.cnt = cnt;
        }
    }
}