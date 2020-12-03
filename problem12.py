import os
import time
start = time.time()
numberStrings = open(os.path.dirname(__file__)+"/data/problem12data.txt").readlines()
numberStrings = [s.strip("\n")for s in numberStrings]

print(numberStrings)
end=time.time()
print("Ran in: " + str(end - start) + " seconds ")