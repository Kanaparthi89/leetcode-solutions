class Solution {
    public String maskPII(String s) {

        // Email
        if (s.contains("@")) {
            s = s.toLowerCase();

            int at = s.indexOf('@');

            String name = s.substring(0, at);
            String domain = s.substring(at);

            return name.charAt(0) + "*****" +
                   name.charAt(name.length() - 1) +
                   domain;
        }

        // Phone number
        StringBuilder digits = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                digits.append(c);
            }
        }

        int totalDigits = digits.length();
        int countryCode = totalDigits - 10;

        String lastFour = digits.substring(totalDigits - 4);

        StringBuilder result = new StringBuilder();

        if (countryCode > 0) {
            result.append("+");

            for (int i = 0; i < countryCode; i++) {
                result.append("*");
            }

            result.append("-");
        }

        result.append("***-***-");
        result.append(lastFour);

        return result.toString();
    }
}
