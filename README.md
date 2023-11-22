# kisok - AI Age Estimation Kiosk
2023.06
kisok - AI Age Estimation Kiosk

#Technology Stack
 Python, MySQL, Kotlin

The document is about a project that uses a kiosk to estimate the user's age and provide personalized services.

This project aims to automatically estimate the age of users to provide a more convenient service to the elderly who often struggle with small kiosk screens and complex payment methods.
Through an ultrasonic sensor connected to a Raspberry Pi, the kiosk measures the distance between the kiosk and the user. Through this, the OLED display provides step-by-step screens such as "EMPTY," "COMING," and "USING." When the "COMING" screen is displayed, the camera is automatically activated to estimate the user's age. The measured age value, obtained through age-trained data, is sent to the database. If the user's age is 60 or older, an enlarged screen is automatically provided, offering a customized kiosk service for elderly individuals.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

키오스크 - AI 나이 추정 키오스크

이 문서는 키오스크를 사용하여 사용자의 나이를 추정하고, 맞춤형 서비스를 제공하는 프로젝트에 관한 설계를 다룬다.
이 프로젝트는 사용자의 나이를 자동으로 추정하여 작은 키오스크 화면과 복잡한 결제 방법에 어려움을 겪는 노인들에게 더 편리한 서비스를 제공하는 것을 목표로 한다. 
라즈베리파이에 연결된 초음파 센서를 통해 키오스와 사용자 간의 거리를 측정한다. 이를 통해 OLED 디스플레이에 "EMPTY", "COMING", "USING"와 같은 단계별 화면을 제공한다. "COMING" 화면이 표시되면 카메라가 자동으로 활성화되어 사용자의 나이를 추정한다. 연령별 훈련된 데이터를 통해 측정된 나잇값은 Database에 전송되며, 사용자의 나이가 60세 이상인 경우 자동으로 확대된 화면이 제공되어 노인들을 위한 맞춤형 키오스크 서비스가 제공된다.


- (Client1) RaspberryPi4, URM09 ultrasonic sensor, i2c OLED 12864, - using Python
- (Client2) kiosk App (bluestack, android) - using Kotlin
- (Server) PC - Python, MySQL

haarcascade_frontalface_default.xml // OpenCv face detection
age_model_new.h5 // trained model


code implementation

<img width="600" alt="image" src="https://github.com/doorunderground/kisok/assets/147718826/3dbe093d-3f36-4798-b28b-db1f506d7570">

<img width="600" alt="image" src="https://github.com/doorunderground/kisok/assets/147718826/666b5e6a-d3b0-4567-ac04-17adcb918884">

<img width="600" alt="image" src="https://github.com/doorunderground/kisok/assets/147718826/8609e7d1-de2f-4b63-9a44-03957211846a">


