import cv2

video = cv2.VideoCapture('videos/people_walking.mp4')

subtractor = cv2.createBackgroundSubtractorMOG2(500, 500, detectShadows=True)

while True:
    _, frame = video.read()

    if _:
        frame = cv2.resize(frame, (960, 720))
        mask = subtractor.apply(frame)
        cv2.imshow('Mask', mask)

        if cv2.waitKey(27) == ord('q'):
            break

    else:
        video = cv2.VideoCapture('videos/people_walking.mp4')

cv2.destroyAllWindows()
video.release()