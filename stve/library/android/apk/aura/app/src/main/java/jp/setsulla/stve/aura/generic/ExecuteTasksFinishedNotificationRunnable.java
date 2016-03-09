package jp.setsulla.stve.aura.generic;

import jp.setsulla.stve.aura.Action;
import jp.setsulla.stve.aura.MessageManager;

/**
 * Created by setsulla on 2016/02/28.
 */
public class ExecuteTasksFinishedNotificationRunnable implements Runnable {
    public static final String MSG_EXECUTE_TASKS_DONE =
            "jp.setsulla.stve.aura.MSG_EXECUTE_TASKS_DONE";
    private int startId;
    private int actionId;

    public ExecuteTasksFinishedNotificationRunnable(int startId) {
        this.startId = startId;
        Action action = Action.getActionFromValue(MSG_EXECUTE_TASKS_DONE);
        actionId = Action.getActionId(action);
    }

    @Override
    public void run() {
        MessageManager.getInstance().sendMessage(actionId, startId);
    }
}
