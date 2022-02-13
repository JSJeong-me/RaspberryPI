
![d32e5588af75d38f8b0720fc7523961c](https://user-images.githubusercontent.com/54794815/153747254-b541becf-63af-41dd-b850-1f550bc99e46.jpg)

        1.MQTT

        MQTT는 클라이언트 publish /  subscribe  메시지 전송 프로토콜입니다. 가볍고 개방적이며 간단하며 구현하기 쉬워서 M2M(Machine-to-Manchine)및 IOT(internet of Things) 에 적합한 선택이다.

        1-1.MQTT 특징

        Client

        MQTT 의 broker 에 연결된 모든 것을 말한다 

        Broker

        Broker 는 모든 메세지를 수신, 필터링, 메시지 구독하는 사람 결정, 클라이언트에게 메세지를 보내는 역할을 한다.

        Publish / Subscribe

        Publish : topic을 지정하여 topic 을 subscribe 하고 있는 클라이언트에게 메세지를 보낸다.

        Subscribe: topic을 구독하여 topic으로 publish된 메시지를 받는다.

        Topic

        MQTT의 topic은 슬래쉬(/)를 분리 문자로 사용하여 폴더 및 파일과 유사한 계층 구조를 가진다.

        example

        house

        house/room

        house/room/main-light

        house/room/left-light


        QoS(Quality of Service)

        0 : 최대 1회 메세지를 보냅니다. 메세지가 소실 될 수 있습니다.

        1 : 최소 1회 메세지를 보냅니다. 메세지가 중복 전송될 수 있습니다.

        2: 핸드쉐이킹 과정으로 메세지를 1회 보냅니다. 메세지를 1회 보내는 것은 보장하지만 대신 성능이 감소 됩니다.



### IoT 콘솔 자습서(Tutorial)

    https://ap-northeast-1.console.aws.amazon.com/iot/home?region=ap-northeast-1#/tutorial?step=1


### Subscribe/Publish Messages


    1. Get Started with AWS IoT Core Quick Connect ---> https://ap-northeast-1.console.aws.amazon.com/iot/home?region=ap-northeast-1#/connIntro
    2. Policy, Certificate attaches
    3. Python을 사용하는 경우 디바이스에서 AWS IoT Core로 MQTT 메시지를 게시 ---> https://aws.amazon.com/ko/premiumsupport/knowledge-center/iot-core-publish-mqtt-messages-python/
