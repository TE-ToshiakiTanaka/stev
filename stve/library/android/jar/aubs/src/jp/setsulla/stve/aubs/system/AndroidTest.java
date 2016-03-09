package jp.setsulla.stve.aubs.system;

import com.android.uiautomator.core.UiObject;
import com.android.uiautomator.core.UiObjectNotFoundException;
import com.android.uiautomator.core.UiSelector;

import jp.setsulla.stve.aubs.AubsBase;

/**
 * Created by 0000138083 on 2016/03/09.
 */
public class AndroidTest extends AubsBase {
    public void testAllowSettingsApp() {
        try {
            UiObject notshow = new UiObject(
                    new UiSelector().resourceId("com.android.vending:id/positive_button"));
            notshow.clickAndWaitForNewWindow();
        } catch (UiObjectNotFoundException e) {
            System.out.println("[Error] Can't search the target object.");
            e.printStackTrace();
        }
    }
}
