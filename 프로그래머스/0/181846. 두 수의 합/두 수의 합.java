import java.math.*;
class Solution {
    public String solution(String a, String b) {
        String answer = "";
        
        BigInteger i = new BigInteger(a);
        BigInteger j = new BigInteger(b);
        answer = String.valueOf(i.add(j));
        return answer;
    }
}