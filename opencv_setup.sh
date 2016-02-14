#! /bin/bash
# check cv2
OPENCVPATH=`sudo find / -name cv2.so | tail -1 | sed -e 's/\/cv2.so//g'` 2>/dev/null
SITE_PACKAGES=`python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()"`
cd $SITE_PACKAGES
if [ -e $SITE_PACKAGES/cv2.so ]; then
    :
else
    ln -s $OPENCVPATH/cv2.so cv2.so
fi
if [ -e $SITE_PACKAGES/cv.py ]; then
    :
else
    ln -s $OPENCVPATH/cv.py cv.py
fi
