class Solution {
    public boolean detectCapitalUse(String word) {

        // Case 1: All uppercase
        if (word.equals(word.toUpperCase())) {
            return true;
        }

        // Case 2: All lowercase
        if (word.equals(word.toLowerCase())) {
            return true;
        }

        // Case 3: Only first letter uppercase
        if (Character.isUpperCase(word.charAt(0)) &&
            word.substring(1).equals(word.substring(1).toLowerCase())) {
            return true;
        }

        return false;
    }
}