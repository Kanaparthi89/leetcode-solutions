class LFUCache {
public:

    struct Node {
        int key;
        int value;
        int freq;

        Node(int k, int v) {
            key = k;
            value = v;
            freq = 1;
        }
    };

    int capacity;
    int minFreq;

    unordered_map<int, Node*> keyMap;

    // freq -> list of nodes
    unordered_map<int, list<Node*>> freqMap;

    // key -> iterator in frequency list
    unordered_map<int, list<Node*>::iterator> pos;


    LFUCache(int capacity) {
        this->capacity = capacity;
        minFreq = 0;
    }


    int get(int key) {

        if (keyMap.find(key) == keyMap.end()) {
            return -1;
        }

        Node* node = keyMap[key];

        updateFrequency(node);

        return node->value;
    }


    void put(int key, int value) {

        if (capacity == 0)
            return;


        // Key already exists
        if (keyMap.find(key) != keyMap.end()) {

            Node* node = keyMap[key];

            node->value = value;

            updateFrequency(node);

            return;
        }


        // Cache full
        if (keyMap.size() == capacity) {

            // Remove least recently used node
            Node* lfu = freqMap[minFreq].back();

            freqMap[minFreq].pop_back();

            pos.erase(lfu->key);
            keyMap.erase(lfu->key);

            delete lfu;
        }


        // Insert new node
        Node* node = new Node(key, value);

        keyMap[key] = node;

        freqMap[1].push_front(node);
        pos[key] = freqMap[1].begin();

        minFreq = 1;
    }


private:

    void updateFrequency(Node* node) {

        int oldFreq = node->freq;


        // Remove from old frequency list
        auto it = pos[node->key];

        freqMap[oldFreq].erase(it);


        // If this was the minimum frequency and list became empty
        if (freqMap[oldFreq].empty() && minFreq == oldFreq) {
            minFreq++;
        }


        // Increase frequency
        node->freq++;


        // Add to new frequency list
        freqMap[node->freq].push_front(node);

        pos[node->key] = freqMap[node->freq].begin();
    }
};