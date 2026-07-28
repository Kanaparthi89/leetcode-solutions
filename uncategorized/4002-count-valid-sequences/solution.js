/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var countValidSequences = function(n, k) {
    const MOD = 1000000007n;

    const fact = new Array(n + 1);
    const invFact = new Array(n + 1);

    fact[0] = 1n;
    for (let i = 1; i <= n; i++) {
        fact[i] = fact[i - 1] * BigInt(i) % MOD;
    }

    function modPow(a, e) {
        let res = 1n;
        while (e > 0n) {
            if (e & 1n) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1n;
        }
        return res;
    }

    invFact[n] = modPow(fact[n], MOD - 2n);
    for (let i = n; i >= 1; i--) {
        invFact[i - 1] = invFact[i] * BigInt(i) % MOD;
    }

    function C(N, R) {
        if (R < 0 || R > N) return 0n;
        return fact[N] * invFact[R] % MOD * invFact[N - R] % MOD;
    }

    let total = C(n - 1, k - 1);

    let odd = 0n;
    if (n >= k && ((n - k) & 1) === 0) {
        const m = (n - k) / 2;
        odd = C(m + k - 1, k - 1);
    }

    return Number((total - odd + MOD) % MOD);
};