class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;

        for (string &token : tokens) {
            // If token is a number
            if (token != "+" && token != "-" && token != "*" && token != "/") {
                st.push(stoi(token));
            }
            else {
                int b = st.top(); st.pop(); // second operand
                int a = st.top(); st.pop(); // first operand

                if (token == "+") {
                    st.push(a + b);
                }
                else if (token == "-") {
                    st.push(a - b);
                }
                else if (token == "*") {
                    st.push(a * b);
                }
                else {
                    st.push(a / b); // C++ truncates toward zero
                }
            }
        }

        return st.top();
    }
};