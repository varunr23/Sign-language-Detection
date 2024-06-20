import os
import cv2


DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 27
alphabet_dict = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
    5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
    15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
    20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'Middle'
}
dataset_size = 50

cap = cv2.VideoCapture(0)

for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print(f'Collecting data for class {alphabet_dict[j]}')

    while True:
        ret, fra = cap.read()
        frame=cv2.flip(fra,1)
        cv2.rectangle(frame, (5,5), (280,43), (255,255,255), -1)
        cv2.putText(frame, 'Ready? Press Q!', (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2,cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break

        elif cv2.waitKey(1) == 27:
            break

    counter = 0
    while counter < dataset_size:
        ret, fra = cap.read()
        frame=cv2.flip(fra,1)

        cv2.rectangle(frame, (5,5), (470,43), (255,255,255), -1)
        text=f'Press Space Bar to Capture for class {alphabet_dict[j]}'
        cv2.putText(frame, text, (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2,cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1)==ord(' '):
            cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)          
            counter += 1

        elif cv2.waitKey(1) == 27:
            break

cap.release()
cv2.destroyAllWindows()