from threading import Lock

class Foo(object):
    def __init__(self):
        self.lock2 = Lock()
        self.lock3 = Lock()

        self.lock2.acquire()
        self.lock3.acquire()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        printFirst()
        self.lock2.release()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        with self.lock2:
            printSecond()
            self.lock3.release()

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        with self.lock3:
            printThird()