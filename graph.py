import cv2
import os
import numpy as np
import urllib.request
import time
import matplotlib.pyplot as plt

start_time = time.time()
time1 = [0]
image_count = [0]
for i in range(1, 40):
    try:
        req = urllib.request.Request(
            'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/' + '{:03d}'.format(i) + '.png')
        response = urllib.request.urlopen(req)
        rr = response.read()
        ba = bytearray(rr)
        time1.append(time.time() - start_time)
        image_count.append(i)
        image = np.asarray(ba, dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)
        cv2.imwrite("images/" + '{:04d}'.format(i) + ".png", image)
        print("Saved " + '{:04d}'.format(i) + ".png")
    except Exception as e:
        print("Error Occured for Pokemon " + '{:04d}'.format(i))
        print(str(e))
        
end_time = time.time()
print("Done")
print("Time Taken = ", end_time - start_time, "sec")
plt.plot(image_count,time1)
plt.title("time vs no of images download")
plt.xlabel("no of images")
plt.ylabel("time")
plt.show()
os.system('pause')