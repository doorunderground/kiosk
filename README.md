# KISOK - AI Age Estimation Kiosk

## Overview
This project  aims to provide personalized services by automatically performing age estimation through a camera, utilizing a Raspberry Pi connected to an ultrasonic sensor to measure the distance between the user and the kiosk. The project involves various components, including Python, MySQL, and Kotlin.

## Technology Stack
- Python
- MySQL
- Kotlin

## Project Description
The ultrasonic sensor connected to a Raspberry Pi, the kiosk measures the distance between the kiosk and the user. Through this, the OLED display provides step-by-step screens such as "EMPTY," "COMING," and "USING." When the "COMING" screen is displayed, the camera is automatically activated to estimate the user's age. The measured age value, obtained through age-trained data, is sent to the database. If the user's age is 60 or older, an enlarged screen is automatically provided, offering a customized kiosk service for elderly individuals.

## Components
- Client1 (Raspberry Pi):** RaspberryPi4, URM09 ultrasonic sensor, i2c OLED 12864 - implemented using Python.
- Client2 (Kiosk App):** Kiosk App using Kotlin (compatible with Bluestacks on Android).
- Server:** PC with Python and MySQL.

## Trained Models and Files
- `haarcascade_frontalface_default.xml`: OpenCV face detection model.
- `age_model_new.h5`: Trained age estimation model.

## Code Implementation
-
<img width="550" alt="스크린샷 2023-11-22 오후 11 25 33" src="https://github.com/doorunderground/kiosk/assets/147718826/dea0e7e2-dba0-4f26-814a-e39ca4c21af6">

<img width="550" alt="스크린샷 2023-11-22 오후 11 29 43" src="https://github.com/doorunderground/kiosk/assets/147718826/3e56f2ff-2bc9-43a4-b8fd-1da874154bf4">

<img width="550" alt="스크린샷 2023-11-22 오후 11 29 14" src="https://github.com/doorunderground/kiosk/assets/147718826/eb3400fe-0b5c-43a8-a013-8d6778589841">



