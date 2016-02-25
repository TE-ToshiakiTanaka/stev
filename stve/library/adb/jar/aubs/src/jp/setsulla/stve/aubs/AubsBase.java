package jp.setsulla.stve.aubs;

/**
 * Created by 0000138083 on 2016/02/25.
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

import junit.framework.Assert;

import com.android.uiautomator.core.UiObject;
import com.android.uiautomator.core.UiObjectNotFoundException;
import com.android.uiautomator.core.UiSelector;
import com.android.uiautomator.testrunner.UiAutomatorTestCase;

public class AubsBase extends UiAutomatorTestCase {

    public boolean existUiObject(String resourceId, String text){
        UiObject target = new UiObject(
                new UiSelector().resourceId(resourceId));
        try {
            return target.getText().equals(text);
        } catch (UiObjectNotFoundException e){
            System.out.println("[Exception] Not Find the Target UiObject.");
            e.printStackTrace();
            return false;
        }
    }

    public boolean existUiObjectClass(String classname, String text){
        UiObject target = new UiObject(
                new UiSelector().className(classname));
        try {
            return target.getText().equals(text);
        } catch (UiObjectNotFoundException e){
            System.out.println("[Exception] Not Find the Target UiObject.");
            e.printStackTrace();
            return false;
        }
    }

    public boolean intent(String intent){
        String[] command = {"am", "start", "-n", intent};
        return this.shell(command);
    }

    public boolean stop(String pack){
        String[] command = {"am", "force-stop", pack};
        return this.shell(command);
    }

    public boolean keyevent(String event){
        String[] command = {"input", "keyevent", event};
        return this.shell(command);
    }

    public boolean screencap(String path){
        String[] command = {"screencap", "-p", path};
        return this.shell(command);
    }

    public boolean shell(String[] command){
        ProcessBuilder pb = new ProcessBuilder(command);
        Process pc;
        try {
            pc = pb.start();
            InputStream stdin = pc.getInputStream();
            InputStreamReader isr = new InputStreamReader(stdin);
            BufferedReader br = new BufferedReader(isr);
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
            pc.waitFor();
            return true;
        } catch (IOException e) {
            e.printStackTrace();
            Assert.fail(e.getMessage());
        } catch (InterruptedException e) {
            e.printStackTrace();
            Assert.fail(e.getMessage());
        }
        return false;
    }
}
