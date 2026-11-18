class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        for(int i=0; i<s.length(); i++){
            if(s.charAt(i)=='[' || s.charAt(i)=='{' || s.charAt(i)=='('){
                stack.push(s.charAt(i));
            }

            if(stack.isEmpty()){return false;}

            if(!stack.isEmpty()){
                char br=stack.peek();
                if(s.charAt(i)==']'){
                    if(br!='['){
                        return false;
                    }
                    stack.pop();
                }

                if(s.charAt(i)=='}'){
                    if(br!='{'){
                        return false;
                    }
                    stack.pop();
                }

                if(s.charAt(i)==')'){
                    if(br!='('){
                        return false;
                    }
                    stack.pop();
                }
            }
        }

        if(stack.isEmpty()){
            return true;
        }

        return false;
    }
}
