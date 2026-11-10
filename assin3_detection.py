from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput

# Load the object detection network
net = detectNet("ssd-mobilenet-v2", threshold=0.3)

# Set input to your local photo file
camera = videoSource("/home/nvidia/jetson-inference/data/images/dog_0.jpg") 

# Set output to a new file path (e.g., .jpg, .png, or .mp4)
output = videoOutput("output_result.jpg") 

print("Processing image...")

# Process the single image frame
while output.IsStreaming():
    img = camera.Capture()
    
    if img is None: # End of stream / capture timeout
        break
        
    # Detect objects in the image
    detections = net.Detect(img)
    for detection in detections:
        print(detection)  
    print(f"Detected {len(detections)} object(s).")
    
    # Render the image (this writes it to your output file)
    output.Render(img)
    
    # Break out of the loop since static images only have one frame
    break

print("Processing complete. Saved to output_result.jpg")
