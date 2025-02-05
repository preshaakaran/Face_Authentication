import json
from deepface import DeepFace

#face matching
# result = DeepFace.verify(img1_path="id1.jpg", img2_path="dp1.jpg")
# print(json.dumps(result, indent=2))

#find face in db
# dfs = DeepFace.find(img_path="id1.jpg", db_path="./db")
# print(dfs)

#face analysis
objs = DeepFace.analyze(img_path="sumi2.jpg")
print(json.dumps(objs, indent=2))  