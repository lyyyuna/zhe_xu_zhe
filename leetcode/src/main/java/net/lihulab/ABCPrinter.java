package net.lihulab;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class ABCPrinter implements Runnable {

    private final ReentrantLock lock;
    private final Condition thisCondition;
    private final Condition nextCondition;
    private char printChar;

    public ABCPrinter(ReentrantLock lock, Condition thisCondition, Condition nextCondition, char printChar) {
        this.lock = lock;
        this.thisCondition = thisCondition;
        this.nextCondition = nextCondition;
        this.printChar = printChar;
    }

    @Override
    public void run() {
        lock.lock();

        try {
            while (true) {
                System.out.print(printChar);
                if (printChar == 'C') {
                    Thread.sleep(1000);
                    System.out.println();
                }
                nextCondition.signal();

                try {
                    thisCondition.await();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }

    public static void main(String[] args) throws InterruptedException {
        ReentrantLock lock = new ReentrantLock();
        Condition cond1 = lock.newCondition();
        Condition cond2 = lock.newCondition();
        Condition cond3 = lock.newCondition();

        Thread threadA = new Thread(new ABCPrinter(lock, cond1, cond2, 'A'));
        Thread threadB = new Thread(new ABCPrinter(lock, cond2, cond3, 'B'));
        Thread threadC = new Thread(new ABCPrinter(lock, cond3, cond1, 'C'));

        threadA.start();
        //Thread.sleep(500);
        threadB.start();
        //Thread.sleep(500);
        threadC.start();
    }
}
