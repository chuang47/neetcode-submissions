class Solution {
    public boolean isPalindrome(String s) {
        String sc = s.replaceAll("[^a-zA-Z0-9]", "");
        sc=sc.toLowerCase();
        int j=sc.length()-1;
        for(int i=0; i<sc.length()/2; i++){
            if(!(sc.charAt(i)==sc.charAt(j-i))) return false;
        }

        return true;
    }
}
