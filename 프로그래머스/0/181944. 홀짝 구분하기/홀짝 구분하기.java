import java.util.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        String readLine;
        StringTokenizer st;

        readLine = br.readLine();
        st = new StringTokenizer(readLine);
        int a = Integer.parseInt(st.nextToken());
        boolean flag = a % 2 == 0;
        
        // Solution sol = new Solution();
        // int result = sol.solution(triangle);
        bw.write(a + " is " + ((flag) ? "even" : "odd"));
        bw.close();
    }
}