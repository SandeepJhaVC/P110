import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('keras_model.h5')
vid = cv2.VideoCapture(0)

while True:
    check,frame = vid.read()
    image = cv2.resize(frame,(224,224))
    test_image = np.array(image,dtype=np.float32)
    test_image=np.expand_dims(test_image,axis=0)
    normalised_image = test_image/255.0
    prediction = model.predict(normalised_image)
    print(prediction)
    cv2.imshow('results',frame)
    key=cv2.waitKey(1)
    if key ==32:
        print('closing')
        break

vid.release()