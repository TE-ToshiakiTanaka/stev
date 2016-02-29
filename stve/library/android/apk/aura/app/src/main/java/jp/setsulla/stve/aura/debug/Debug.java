package jp.setsulla.stve.aura.debug;

/**
 * Created by setsulla on 2016/02/28.
 */
public class Debug {
    private Debug() {}
    private volatile static boolean isUserDebugEnabled = true;
    private static boolean isDevelopmentDebugEnabled = true;

    public static boolean isUserEnabled() {
        return isUserDebugEnabled || isDevelopmentDebugEnabled;
    }

    public static boolean isDevelopmentEnabled() {
        return isDevelopmentDebugEnabled;
    }

    public synchronized static void setUserDebug(boolean isEnabled) {
        isUserDebugEnabled = isEnabled;
    }
}
