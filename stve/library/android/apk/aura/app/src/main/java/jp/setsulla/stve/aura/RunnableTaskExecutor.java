package jp.setsulla.stve.aura;

import android.os.Handler;
import android.os.HandlerThread;
import android.os.Looper;

import java.util.ArrayList;

/**
 * Created by setsulla on 2016/02/28.
 */
public class RunnableTaskExecutor implements IRunnableTaskExecutor {

    private final ArrayList<Runnable> mTaskList = new ArrayList<Runnable>();
    private final HandlerThread mWorkerThread;
    private final Handler mWorkerHandler;

    private RunnableTaskExecutor() {
        mWorkerThread = new HandlerThread("ServiceWorkerThread");
        mWorkerThread.start();
        mWorkerHandler = new Handler(mWorkerThread.getLooper());
    }

    public final static IRunnableTaskExecutor createNewExecutor() {
        return new RunnableTaskExecutor();
    }

    @Override
    public final synchronized void submitTask(Runnable runnable) {
        mTaskList.add(runnable);
    }

    @Override
    public synchronized void submitTaskFirst(Runnable runnable) {
        mTaskList.add(0, runnable);
    }

    @Override
    public final synchronized void execute() throws IllegalThreadStateException {
        if (mWorkerThread.isAlive()) {
            throw new IllegalThreadStateException(
                    "Can not execute because underlaying thread is dead");
        }
        if (!mTaskList.isEmpty()) {
            for (Runnable runnable : mTaskList) {
                mWorkerHandler.post(runnable);
            }
            mTaskList.clear();
        }
    }

    @Override
    public final synchronized void shutdown() {
        final Looper looper = mWorkerThread.getLooper();
        looper.quit();
        try {
            mWorkerThread.join(5000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    @Override
    public final synchronized void clearTasks() {
        mTaskList.clear();
    }

    @Override
    public final synchronized boolean hasTasks() {
        return !mTaskList.isEmpty();
    }
}
