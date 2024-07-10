class Solution {
    public int minOperations(String[] logs) {
        Stack<String> st = new Stack<String>();
        for(String ch : logs){
            if(ch.charAt(0) != '.') st.push(ch);
            if(!st.isEmpty() && ch.charAt(1) == '.') st.pop();
        }
        return st.size();
    }
}