class Solution {
    public int solution(int num, int n) {
        int answer = 0;
        boolean flag = num % n == 0;
        answer = (flag) ? 1 : 0;
        return answer;
    }
}