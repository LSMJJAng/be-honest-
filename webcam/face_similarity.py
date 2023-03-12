from deepface import DeepFace

img1 = '/Users/sharekim_hangyuseong/Desktop/송강.jpeg'
img2 = '/Users/sharekim_hangyuseong/Desktop/최우식.png'
img3 = '/Users/sharekim_hangyuseong/Desktop/최우식2.jpg'

backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
result = DeepFace.verify(img1_path=img1, img2_path=img2, detector_backend=backends[1])
result2 = DeepFace.verify(img1_path=img2, img2_path=img3, detector_backend=backends[1])

print(result)
print(result2)