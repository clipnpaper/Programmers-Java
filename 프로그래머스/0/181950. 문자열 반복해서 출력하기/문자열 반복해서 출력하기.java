import java.util.*;

public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        String readLine;
        StringTokenizer st;

        readLine = br.readLine();
        st = new StringTokenizer(readLine);
        String s = st.nextToken();
        int b = Integer.parseInt(st.nextToken());
        String answer = "";
        // Solution sol = new Solution();
        // int result = sol.solution(triangle);
        for(int i = 0; i < b; i++){
            answer += s;
        }
        bw.write(answer + "");
        bw.close();
    }