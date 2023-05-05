import java.lang.StringBuffer;

// Lv1. 신규 아이디 추천
class Solution {
    public String solution(String new_id) {
        String answer = "";
        
        // 1. 소문자 치환
        new_id = new_id.toLowerCase();
        
        // 2. 규정 외 모든 문자 제거
        // new_id = new_id.replaceAll("[^a-z0-9_.-]", "");
        
        StringBuilder sb = new StringBuilder();
        for (int i=0; i < new_id.length(); i++) {
            char c = new_id.charAt(i);
            if (('a' <= c && c <= 'z') || ('0' <= c && c <= '9') 
                || c == '_' || c == '-' || c == '.') {
                sb.append(c);
            }
        }
        new_id = sb.toString();
        
        
        // 3. 마침표 2번 연속된 부분을 하나의 마침표로 치환
        new_id = sb.toString().replace("..", ".");
        while(new_id.contains("..")) {
            new_id = new_id.replace("..", ".");
        }
    
        // 4. 마침표가 처음이나 끝에 위치한다면 제거
        if (new_id.length() > 0 && new_id.charAt(0) == '.') {
            new_id = new_id.substring(1, new_id.length());
        }
        
        if (new_id.length() > 0 && new_id.charAt(new_id.length() - 1) == '.') {
            new_id = new_id.substring(0, new_id.length() - 1);
        }
        
        // 5. 빈 문자열이면 a 대입
        if (new_id.equals("")) {
            new_id = "a";
        }
        
        // 6. 길이가 16자 이상이면, 첫 15개 문자 제외 나머지 모두 제거
        if (new_id.length() >= 16) {
            new_id = new_id.substring(0, 15);
        }
        if (new_id.length() > 0 && new_id.charAt(new_id.length() - 1) == '.') {
            new_id = new_id.substring(0, new_id.length() - 1);
        }
        
        // 7. 길이가 2자 이하이면, 마지막 문자를 길이가 3이 될때까지 붙이기
        sb = new StringBuilder(new_id);
        char c = new_id.charAt(new_id.length() - 1);
        if (new_id.length() <= 2) {
            while(sb.length() < 3) {
                sb.append(c);
            }
            new_id = sb.toString();
        }
        
        return new_id;
    }
}