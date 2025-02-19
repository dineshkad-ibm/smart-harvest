import torch
from PIL import Image
from transformers import AutoProcessor, LlavaForConditionalGeneration

class Crew:
    def __init__(self, agents, tasks):
        self.agents = agents
        self.tasks = tasks
        model_name = "llava-hf/llava-1.5-7b-hf"
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = LlavaForConditionalGeneration.from_pretrained(model_name).to(self.device)
        self.processor = AutoProcessor.from_pretrained(model_name)
        
    def classify_fruit(self, image_path: str):
        image = Image.open(image_path).convert("RGB")
        prompt = "<image> What fruit is in this image? Provide the fruit name, description, and also describe whether it's ripe or not."
        inputs = self.processor(images=image, text=prompt, return_tensors="pt").to(self.device)
        with torch.no_grad():
            output = self.model.generate(**inputs, max_new_tokens=50)
        response = self.processor.batch_decode(output, skip_special_tokens=True)[0]
        fruit_details = response.replace(prompt, "").strip()
        return fruit_details

    def decide_ripeness(self, label):
        ripe_keywords = ["ripe", "ready for harvest", "yellow", "sweet", "soft", "mature"]
        not_ripe_keywords = ["unripe", "green", "hard", "not ripe", "immature"]
        label_lower = label.lower()
        if any(keyword in label_lower for keyword in not_ripe_keywords):
            return "not ripe"
        elif any(keyword in label_lower for keyword in ripe_keywords):
            return "ripe"
        else:
            return "unknown"

    def alert_farmer(self, is_ripe):
        if is_ripe == "ripe":
            return "ALERT: The fruit is ripe and ready for harvest!"
        else:
            return "INFO: The fruit is not yet ripe."

    def kickoff(self, inputs):
        results = {}
        image_path = inputs.get("image_path")
        classification_result = self.classify_fruit(image_path)
        results['classification'] = classification_result
        ripeness_status = self.decide_ripeness(classification_result)
        results['ripeness_status'] = ripeness_status
        alert_message = self.alert_farmer(ripeness_status)
        results['alert'] = alert_message
        return {
            'fruit_details': classification_result,
            'ripeness_status': ripeness_status,
            'alert': alert_message
        }
