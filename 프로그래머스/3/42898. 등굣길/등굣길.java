class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        int[][] dp = new int[m+1][n+1];
        
        // for (int i = 1; i <= m; i++){
        //     dp[i][1] = 1;
        // }
        // for (int j = 1; j <= n; j++){
        //     dp[1][j] = 1;
        // }
        
        dp[1][1] = 1;
        
        for (int w = 0; w < puddles.length; w++){
            int x = puddles[w][0];
            int y = puddles[w][1];
            dp[x][y] = -1;
        }
        
        
        for (int i = 1; i <= m; i++){
            for(int j = 1; j <= n; j++){
                // 현 위치 잡기 => x행 y열
                int x = i; 
                int y = j;
                // 현 위치가 웅덩이라면 -> 넘기기
                if(dp[x][y] == -1) continue;
                // 왼쪽 위치가 웅덩이가 아니라면 -> 그 위치 dp 가져오기
                if(dp[x-1][y] != -1) dp[x][y] += dp[x-1][y];
                // 오른쪽 위치가 웅덩이가 아니라면 -> 그 위치 dp 가져오기
                if(dp[x][y-1] != -1) dp[x][y] += dp[x][y-1];
                dp[x][y] %= 1000000007;
            }
        }
        
        answer = dp[m][n];
        
        
        
        
        return answer;
    }
}