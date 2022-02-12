### RaspberryPI Camera 연결 및 테스트

    https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/1
    
    VNC 터미널에서 Thonny IDE로 camera01.py 실행



### openCV

    raspberry$ sudo nano /etc/dphys-swapfile   --> CONF_SWAPSIZE=2048
    
    VNC 설정 방법
    
    raspberry$ sudo raspi-config
    
    메뉴> interface  -> VNC: Enable
    
    raspberry$ vncserver :1 -geometry 1280x1024 -depth 16 -pixelformat rgb565
    
    VNC Viewer 설치 :  https://www.realvnc.com/en/connect/download/viewer/
    
    C:\Program Files\RealVNC\VNC Viewer>vncviewer 192.168.137.89:5901
    
    
    
       
    Getting started with the Camera Module
    
    https://www.raspberrypi.com/documentation/accessories/camera.html
    
    
    * Camera 설치: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
    
    raspberry$ raspistill -o testImage.jpg
    
    raspberry$ raspistill -hf-o testImage.jpg  (horizontal flliped)
    
    raspberry$ raspistill -o timelaps%04d.jpg -t 1000000 -tl 5000  (5초마다 1장씩)
    
    * RaspberryPI video stream to PC
    
    raspberry$ sudo apt-get install mplayer netcat
    
    raspberry$ raspivid -o filename.h264 (Display camera output to display, and optionally saves an H264 capture at requested bitrate)
    
    Program: netcat.zip mplayer 설치
    
    raspberry$ apt-get install mplayer netcat
    
    c:\>ipconfig
    C:\>nc -l -p 5001 | mplayer -fps 31 -cache 1024 -
    
    raspberry$ raspivid -t 999999 -o - | nc 192.168.35.241 5001   

    
    * H.264 -> mp4
    
    Installation
        sudo apt-get update
        sudo apt-get install gpac
        y

    Usage
        MP4Box -add filename.h264 filename.mp4
    
    
    Video Stream 테스트: https://appuals.com/how-to-perform-video-streaming-using-raspberry-pi
    
    
    
    openCV install

    https://docs.opencv.org/4.x/d2/de6/tutorial_py_setup_in_ubuntu.html
    
    
    Python Image Display Library
    
    - image01.py
    - image02.py
    - image03.py
    
    
    


### Video Web Streaming Service
    
    raspberry$ python3 rpi_video_streaming.py
    
    
