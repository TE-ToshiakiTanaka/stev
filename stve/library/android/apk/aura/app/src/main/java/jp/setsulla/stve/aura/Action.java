package jp.setsulla.stve.aura;

import static jp.setsulla.stve.aura.debug.SetDebugRunnable.DEBUG_ON;
import static jp.setsulla.stve.aura.generic.ExecuteTasksFinishedNotificationRunnable.MSG_EXECUTE_TASKS_DONE;

/**
 * Created by setsulla on 2016/02/28.
 */
public enum Action {
    DO_TASKS_DONE(MSG_EXECUTE_TASKS_DONE),

    SET_DEBUG_ON_ACTION(DEBUG_ON),

    UNKNOWN("unknown");

    private final String mIntentActionValue;

    private Action(String intentAction) {
        mIntentActionValue = intentAction;
    }

    public static int getActionId(Action action) {
        return action.ordinal();
    }

    public static int getActinIdFromActionValue(String actionValue) {
        for (Action action : Action.values()) {
            if (actionValue.equalsIgnoreCase(action.getActionValue())) {
                return action.ordinal();
            }
        }
        throw new RuntimeException(
                "Could not find action with value [ " + actionValue + "] in list");
    }

    public static Action getActionFromValue(String actionValue) {
        for (Action action : Action.values()) {
            if (actionValue.equalsIgnoreCase(action.getActionValue())) {
                return action;
            }
        }
        throw new RuntimeException(
                "Could not find action value [ " + actionValue + " : in list");
    }

    public static Action getActionFromId(int id) {
        if (id >= 0 && id <= Action.values().length) {
            return Action.values()[id];
        }
        throw new IndexOutOfBoundsException(
                "Id + [ " + id + " ] is outside of range, max is " + Action.values().length);
    }

    public String getActionValue() {
        return mIntentActionValue;
    }

}
