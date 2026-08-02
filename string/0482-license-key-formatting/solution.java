class Solution {
    public String licenseKeyFormatting(String s, int k) {

        // Remove dashes and convert to uppercase
        String str = s.replace("-", "").toUpperCase();

        StringBuilder result = new StringBuilder();

        int count = 0;

        // Build groups from right to left
        for (int i = str.length() - 1; i >= 0; i--) {

            if (count == k) {
                result.append('-');
                count = 0;
            }

            result.append(str.charAt(i));
            count++;
        }

        // We built the string backwards
        return result.reverse().toString();
    }
}