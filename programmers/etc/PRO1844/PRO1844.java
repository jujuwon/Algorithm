import java.util.Queue;
import java.util.LinkedList;

// Lv2. 게임 맵 최단거리
class Solution {
    
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    
    public int solution(int[][] maps) {
        int answer = -1;
        
        boolean[][] visited = new boolean[maps.length][maps[0].length];
        
        Queue<Point> queue = new LinkedList<>();
        Point first= new Point(0, 0, 1);
        queue.add(first);
        visited[first.x][first.y] = true;
        
        while (!queue.isEmpty()) {
            Point p = queue.poll();
            
            if (p.x == maps.length - 1 && p.y == maps[0].length - 1) {
                answer = p.cnt;
                break;
            }
            
            for (int i=0; i < 4; i++) {
                int xx = p.x + dx[i];
                int yy = p.y + dy[i];
                
                if (xx < 0 || yy < 0 
                    || xx >= maps.length || yy >= maps[0].length
                    || visited[xx][yy] || maps[xx][yy] != 1) continue;
                
                queue.add(new Point(xx, yy, p.cnt+1));
                visited[xx][yy] = true;
            }
        }
        
        return answer;
    }
}

class Point {
    int x;
    int y;
    int cnt;
    Point(int x, int y, int cnt) {
        this.x = x;
        this.y = y;
        this.cnt = cnt;
    }
}