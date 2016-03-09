package jp.setsulla.stve.aura;

/**
 * Created by setsulla on 2016/02/28.
 */
public interface IRunnableTaskExecutor {
    void submitTask(Runnable runnable);
    void submitTaskFirst(Runnable runnable);
    void execute() throws IllegalThreadStateException;
    void shutdown();
    void clearTasks();
    boolean hasTasks();
}
