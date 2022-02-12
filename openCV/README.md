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
    
    
    Camera 설치: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
    
    Video Stream 테스트: https://appuals.com/how-to-perform-video-streaming-using-raspberry-pi
    
    
    
    openCV install

    https://docs.opencv.org/4.x/d2/de6/tutorial_py_setup_in_ubuntu.html
