import java.util.concurrent.TimeUnit;

class Task extends Thread{
    // number
    private int num;

    public Task(int num){
        this.num = num;
    }

    private long fibonacci(int num){
        if(num <= 2)
            return 1;
        return fibonacci(num-1) + fibonacci(num-2);
    }

    // Thread's task
    @Override
    public void run(){
        System.out.println(num+" : "+fibonacci(this.num));
    }
}

class Fib{
    public static void main(String []args) throws Exception{
        Thread t1 = new Task(50);
        Thread t2 = new Task(50);

        long startTime = System.currentTimeMillis();

        t1.start();
        t2.start();

        t1.join();
        t2.join();

        long timeElapsed = System.currentTimeMillis() - startTime;

        System.out.println("Time : " + (double)timeElapsed/1000);
    }
}