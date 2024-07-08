class Solution {
    public String decodeString(String s) {
        Stack<String> st = new Stack<>();
        StringBuilder res = new StringBuilder();
        StringBuilder num = new StringBuilder();
        System.out.println(num.length());
        for(char ch : s.toCharArray()){
            if(ch == ']'){
                StringBuilder temp = new StringBuilder(), repeated_string = new StringBuilder();
                while(!st.peek().equals("[")) temp.insert(0,st.pop());
                st.pop();
                if(!st.isEmpty()){
                    int repeats = Integer.parseInt(st.pop());
                    for(int i=0; i<repeats; i++) repeated_string.append(temp.toString());
                }else repeated_string.append(temp.toString());
                st.push(repeated_string.toString());
            }
            else if(Character.isDigit(ch)) num.append(ch);
            else{
                if(num.length() != 0){
                    st.push(num.toString());
                    num = new StringBuilder();
                }
                st.push(Character.toString(ch));
            }
        }
        while(!st.isEmpty()) res.insert(0,st.pop());
        return res.toString();
    }
}