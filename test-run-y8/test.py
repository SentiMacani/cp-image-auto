from ultralytics import YOLO

# Load a model
model = YOLO('tutorialandlogin_v1.pt')  # pretrained YOLOv8n model

# Run batched inference on a list of images
screenx_center = 1920/2
screeny_center = 1080/2
    
decision = {
    "login": False,
    }

results = model(['login.png'], conf=.20, save=True)  # return a list of Results objects
boxes = results[0].boxes.xyxy.tolist()
classes = results[0].boxes.cls.tolist()
names = results[0].names
confidences = results[0].boxes.conf.tolist()

# Process results list
for box, cls, conf in zip(boxes, classes, confidences):
    x1, y1, x2, y2 = box
    
    center_x = (x1+x2) / 2
    center_y = (y1+y2) / 2

    confidence = conf
    detected_class = cls
    name = names[int(cls)]
    
    if name=="login":
        decision["login"] = True
        decision["login-location"] = (center_x, center_y)
    elif name == "player":
        decision["player"] = True
        decision["player_location"] = (center_x, center_y)
    elif name == "skeleton":
        decision["skeleton"] = True
        decision["skeleton_location"] = (center_x, center_y)    

    
print(decision)