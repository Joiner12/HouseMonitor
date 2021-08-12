import pybullet as p
from time import sleep

physicsClient = p.connect(p.GUI)

p.setGravity(0, 0, -10)
planeId = p.loadURDF(r"D:\anaconda3\pkgs\pybullet-3.17-py38h60cbd38_0\Lib\site-packages\pybullet_data\plane.urdf")
cubeStartPos = [0, 0, 1]
cubeStartOrientation = p.getQuaternionFromEuler([0, 0, 0])
boxId = p.loadURDF("r2d2.urdf", cubeStartPos, cubeStartOrientation)
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)

useRealTimeSimulation = 0

if (useRealTimeSimulation):
    p.setRealTimeSimulation(1)

while 1:
    if (useRealTimeSimulation):
        p.setGravity(0, 0, -10)
        sleep(0.01)  # Time in seconds.
    else:
        p.stepSimulation()
