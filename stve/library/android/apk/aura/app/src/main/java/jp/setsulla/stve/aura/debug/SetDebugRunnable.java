package jp.setsulla.stve.aura.debug;

import android.content.Intent;
import android.os.Message;

import jp.setsulla.stve.aura.MessageManager;

/**
 * Created by setsulla on 2016/02/28.
 */
public class SetDebugRunnable implements Runnable {

    public static final String DEBUG_ON = "jp.setsulla.stve.aura.DEBUG_ON";
    private final Intent mOrigIntent;
    private final int mActionId;

    public SetDebugRunnable(Intent intent, int id) {
        mOrigIntent = intent;
        mActionId = id;
    }

    @Override
    public void run() {
        Debug.setUserDebug(true);
        MessageManager.getInstance().sendMessage(mActionId, true, mOrigIntent);
    }
}
