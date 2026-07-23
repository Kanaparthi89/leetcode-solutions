class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<int> result(n, 0);
        stack<int> st;

        int prevTime = 0;

        for (string &log : logs) {
            // Parse log: id:type:time
            int first = log.find(':');
            int second = log.find(':', first + 1);

            int id = stoi(log.substr(0, first));
            string type = log.substr(first + 1, second - first - 1);
            int time = stoi(log.substr(second + 1));

            if (type == "start") {
                // Previous function executed until this moment
                if (!st.empty()) {
                    result[st.top()] += time - prevTime;
                }

                st.push(id);
                prevTime = time;
            }
            else { // end
                // Current function executes including this timestamp
                result[st.top()] += time - prevTime + 1;

                st.pop();

                // Next execution starts after this timestamp
                prevTime = time + 1;
            }
        }

        return result;
    }
};