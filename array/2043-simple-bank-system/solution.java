class Bank {

    private long[] balance;

    public Bank(long[] balance) {
        this.balance = balance;
    }
    
    public boolean transfer(int account1, int account2, long money) {
        if (!isValidAccount(account1) || !isValidAccount(account2)) {
            return false;
        }

        if (balance[account1 - 1] < money) {
            return false;
        }

        balance[account1 - 1] -= money;
        balance[account2 - 1] += money;

        return true;
    }
    
    public boolean deposit(int account, long money) {
        if (!isValidAccount(account)) {
            return false;
        }

        balance[account - 1] += money;

        return true;
    }
    
    public boolean withdraw(int account, long money) {
        if (!isValidAccount(account)) {
            return false;
        }

        if (balance[account - 1] < money) {
            return false;
        }

        balance[account - 1] -= money;

        return true;
    }

    private boolean isValidAccount(int account) {
        return account >= 1 && account <= balance.length;
    }
}