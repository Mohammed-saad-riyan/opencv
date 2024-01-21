import cv2
import mediapipe as mp
mp_draw = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)
hands = mp_hands.Hands()
while True :
    rt, video = cap.read()
    video = cv2.cvtColor(video,cv2.COLOR_BGR2RGB)
    results = hands.process(video)
    video = cv2.cvtColor(video,cv2.COLOR_RGB2BGR)
    videoHeight, videoWidth, _ = video.shape 
    co=[]
    if results.multi_hand_landmarks :
        for hand_landmarks in results.multi_hand_landmarks :
            mp_draw.draw_landmarks (
                video,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )
            for point in mp_hands.HANDLANDMARK :
                if str(point) == "HandLandmark.WRIST" :
                    normalizedLandmark = hand_landmarks.landmark[point]
                    pixelCoordintesLandmark = mp_draw._


    cv2.imshow("frame",video)
    if cv2.waitKey(1) == ord('q') :
        break
