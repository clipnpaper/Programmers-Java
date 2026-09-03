import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        String readLine;
        StringTokenizer st;

        readLine = br.readLine();
        st = new StringTokenizer(readLine);
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        // Solution sol = new Solution();
        // int result = sol.solution(triangle);

        bw.write("a = " + a + "\nb = " + b);
        bw.close();
    }
}