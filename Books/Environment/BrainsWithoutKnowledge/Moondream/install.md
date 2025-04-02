```python
import moondream as md

model = md.vl(model="path/to/moondream-0.5B.bin")
```


```python
# ===== STEP 1: Install Dependencies =====
# pip install moondream  # Install dependencies in your project directory


# ===== STEP 2: Download Model =====
# Download model (422 MiB download size, 816 MiB memory usage)
# Use: wget (Linux and Mac) or curl.exe -O (Windows)
# wget https://huggingface.co/vikhyatk/moondream2/resolve/9dddae84d54db4ac56fe37817aeaeb502ed083e2/moondream-0_5b-int4.mf.gz

import moondream as md
from PIL import Image

model = md.vl(model='./moondream-0_5b-int4.mf.gz')  # Initialize model
image = Image.open("./path/to/image.jpg")  # Load image
encoded_image = model.encode_image(image)  # Encode image (recommended for multiple operations)

# 1. Caption any image (length options: "short" or "normal" (default))
caption = model.caption(encoded_image)["caption"]
print("Caption:", caption)

print("Streaming caption:", end=" ", flush=True)
for chunk in model.caption(encoded_image, stream=True)["caption"]:
    print(chunk, end="", flush=True)

# 2. Query any image
answer = model.query(encoded_image, "What do you see in this image?")["answer"]
print("\nAnswer:", answer)  # Single response

print("Streaming answer:", end=" ", flush=True)
for chunk in model.query(encoded_image, "What's in this image?", stream=True)["answer"]:
    print(chunk, end="", flush=True)

# 3. Detect any object
detect_result = model.detect(encoded_image, "subject")  # change 'subject' to what you want to detect
print("\nDetected:", detect_result["objects"])

# Point functionality is only available for 2B models
```
