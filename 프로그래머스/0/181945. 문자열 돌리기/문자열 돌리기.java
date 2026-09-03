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
        String a = st.nextToken();
        
        // Solution sol = new Solution();
        // int result = sol.solution(triangle);
        // bw.write();

        for(int i = 0; i < a.length(); i++){
            bw.write(a.charAt(i) + "\n");
        }

        bw.close();
    }
}