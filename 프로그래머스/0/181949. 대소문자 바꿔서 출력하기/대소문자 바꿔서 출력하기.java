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
        String answer = "";
        // Solution sol = new Solution();
        // int result = sol.solution(triangle);
        for (int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if (ch >= 'a' && ch <= 'z') {
                ch += 'A' - 'a';
            }else if(ch >= 'A' && ch <= 'Z'){
                ch += 'a' - 'A';
            }
            answer += ch;
        }
        bw.write(answer + "");
        bw.close();
    }