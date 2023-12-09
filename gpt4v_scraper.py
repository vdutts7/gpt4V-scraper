import os
import base64
import subprocess
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI model
ai_model = OpenAI()
ai_model.timeout = 40

# Function to encode image to base64
def encode_image_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Function to capture website snapshot
def capture_website(url):
    print(f"Accessing {url}")

    snapshot_path = "snapshot.jpg"
    if os.path.exists(snapshot_path):
        os.remove(snapshot_path)

    subprocess_result = subprocess.run(
        ["node", "snapshot.js", url],
        capture_output=True,
        text=True
    )

    if not os.path.exists(snapshot_path):
        print("❌ Snapshot failed")
        return "❌ oopsie poopsie this snapshot failed"
    
    return encode_image_to_base64(snapshot_path)

# Function to extract information using AI model
def extract_info_from_image(encoded_image, user_prompt):
    ai_response = ai_model.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "system",
                "content": "You are now a Web Scraper. Your task is extracting maximum info possible based on a snapshot the user provides and the user's instructions.",
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                    {
                        "type": "text",
                        "text": user_prompt,
                    }
                ]
            }
        ],
        max_tokens=1024,
    )

    response_content = ai_response.choices[0].message.content

    if "ANSWER_NOT_FOUND" in response_content:
        print("😔 No answer found. Whoops.")
        return "😔 Could not find answer on this website"
    else:
        print(f"🤖 AI Model Response: {response_content}")
        return response_content

# Function to perform website capture and information extraction
def web_capture_and_extract(url, prompt):
    base64_snapshot = capture_website(url)
    print("Snapshot successful 📸✅ ")
    
    if base64_snapshot == "❌ Snapshot failed":
        return "❌ Snapshot error"
    else:
        return extract_info_from_image(base64_snapshot, prompt)

# Running the function w/ a example website + prompt
result = web_capture_and_extract("https://vd7.io/experience", "Extract this dude's Experience info")
print(result)
