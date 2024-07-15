import os

image_files = []
os.chdir(os.path.join("data", "test", "Vehicle registration plate"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("data/test/Vehicle registration plate/" + filename)
os.chdir("..")
os.chdir("..")
with open("test.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")