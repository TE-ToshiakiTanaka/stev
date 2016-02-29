package jp.setsulla.stve.aura;

import android.content.Intent;
import android.os.Message;

/**
 * Created by setsulla on 2016/02/28.
 */
public interface IRunnableFactory {
    Runnable build(Intent intent);
    String getIntentAction(Message msg);
    boolean getActionResult(Message msg);
    Intent getOriginalIntent(Message msg);
}
