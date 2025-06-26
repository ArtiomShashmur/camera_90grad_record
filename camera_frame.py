import cv2

cap = cv2.VideoCapture(0)


frame_width = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))

print("q - exit")

while True:
    success, img = cap.read()
    if not success:
        break


    rotated_frame = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)


    cv2.imshow('Result', rotated_frame)


    out.write(rotated_frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
