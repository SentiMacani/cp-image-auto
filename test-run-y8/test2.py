from ultralytics import YOLO

# Load a model
model = YOLO('tutorialandlogin_v1.pt')  # pretrained YOLOv8n model

# Run batched inference on a list of images
screenx_center = 1920/2
screeny_center = 1080/2
    
decision = {
    "login": False,
    "player": False,
    "skeleton": False,
    }

results = model(['login.png'], conf=.20, save=True)  # return a list of Results objects
print("finding login")
boxes = results[0].boxes.xyxy.tolist()
print("loading")
classes = results[0].boxes.cls.tolist()
print("feeding chicken")
names = results[0].names
print("playing coc")
confidences = results[0].boxes.conf.tolist()
print("touching grass")

# Process results list
for box, cls, conf in zip(boxes, classes, confidences):
    x1, y1, x2, y2 = box
    print("box set")
    
    center_x = (x1+x2) / 2
    center_y = (y1+y2) / 2
    print("divided the screen res")

    confidence = conf
    detected_class = cls
    name = names[int(cls)]
    print("name:"+str(name))
    print("conf:"+str(confidence))
    if name=="login":
        decision["login"] = True
        decision["login-location"] = (center_x, center_y)
        print("login figured")
    elif name == "player":
        decision["player"] = True
        decision["player"] = (center_x, center_y)
        print("player_location figured")
    elif name == "skeleton":
        decision["skeleton"] = True
        decision["skeleton"] = (center_x, center_y)    
    # elif name == "continue":
    #     decision["continue"] = True
    #     decision["continue_location"] = (center_x, center_y)
    # elif name == "play":
    #     decision["play"] = True
    #     decision["play_location"] = (center_x, center_y)
    # elif name == "next":
    #     decision["next"] = True
    #     decision["next_location"] = (center_x, center_y)
    # elif name == "tree":
    #     decision["tree"] = True
    #     distance = ((center_x - screenx_center) ** 2 + (center_y - screeny_center) **2) **.5
    #      if "tree_location" in decision:
    #         # Calculate if closer
    #         if distance < decision["tree_distance"]:
    #             decision["tree_location"] = (center_x, center_y)
    #             decision["tree_distance"] = distance
    #     else:
    #         decision["tree_location"] = (center_x, center_y)
    #         decision["tree_distance"] = distance
    # elif name == "building":
    #     decision["building"] = True
    #     distance = ((center_x - screenx_center) ** 2 + (center_y - screeny_center) **2) **.5
    #     if "building_location" in decision:
    #         # Calculate if closer
    #         if distance < decision["building_distance"]:
    #             decision["building_location"] = (center_x, center_y)
    #             decision["building_distance"] = distance
    #     else:
    #         decision["building_location"] = (center_x, center_y)
    #         decision["building_distance"] = distance
    
print(decision)