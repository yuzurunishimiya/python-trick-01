import os

if not os.sys.version_info > (2, 7):
    print("Use python 3 instead")
elif not os.sys.version_info >= (3,5):
    print("Upgrade your python version")
else:
    print("Good job, keep it up")

version = os.sys.version
print("Your python version is {}".format(version))