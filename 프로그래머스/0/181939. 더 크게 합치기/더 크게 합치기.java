class Solution {
    public int solution(int a, int b) {
            int answer = 0;
            int answer1 = 0;
            int answer2 = 0;
            StringBuilder sb = new StringBuilder();
            sb.append(a);
            sb.append(b);
            answer1 = Integer.parseInt(sb.toString());
            sb = new StringBuilder();
            sb.append(b);
            sb.append(a);
            answer2 = Integer.parseInt(sb.toString());
            answer = Math.max(answer1, answer2);
            return answer;
        }
}