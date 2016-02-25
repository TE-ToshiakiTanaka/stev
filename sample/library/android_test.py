
if __name__ == "__main__":
    from stve.library.adb.module import AndroidBase

    a = AndroidBase("YT9111NUXX")
    print a.profile.SERIAL
    print a.shell("dumpsys power")
