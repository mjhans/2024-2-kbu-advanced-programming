// linux : time -p java -cp . RunnableEx 5
// mac : gtime -p java -cp . RunnableEx 5

import java.util.Random;
import java.util.ArrayList;

class RunnableEx {
    public static void main(String args[]) {
        try{        
            ArrayList<Thread> threads = new ArrayList<>();
            
            int listCount = 0;
            try {
                listCount = Integer.parseInt(args[0]);
            } catch (Exception e) {
                listCount = 0;
            }
            long start = System.currentTimeMillis();
            for (int i = 0; i < listCount; i++){
                Thread t = new Thread(new MyRunnable((long)(10_000_000 / listCount)));
                t.start();
                threads.add(t);
            } 
            for (Thread t : threads){  
                t.join();
            }
            long end = System.currentTimeMillis();
            long elapsedTime = end - start;
            System.out.println("elased time(ms) : " + elapsedTime);

        } catch (Exception  e){
            System.out.println(e.getMessage());
        }
        
    }
}

class MyRunnable implements Runnable {
    long size = 0;
    public MyRunnable(long size){
        this.size = size;
    }
    @Override
    public void run() {
        Random rand = new Random();
        long cnt = 1;        
        while(cnt <= size) {
            cnt += rand.nextInt(5);   
        }
    }
}