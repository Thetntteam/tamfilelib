import base64
import json
from datetime import datetime
import os

class TAMFile:
    def __init__(self, text="", media=None, metadata=None):
        self.text = text
        self.media = media if media else []
        self.metadata = metadata if metadata else {
            "version": "1.0",
            "author": "",
            "creation_date": datetime.now().isoformat()
        }

    def add_media(self, media_name, media_path, description=""):
        with open(media_path, "rb") as media_file:
            encoded_media = base64.b64encode(media_file.read()).decode('utf-8')
            extension = os.path.splitext(media_path)[1]
            media_item = {
                "name": media_name,
                "description": description,
                "data": encoded_media,
                "timestamp": datetime.now().isoformat(),
                "extension": extension
            }
            self.media.append(media_item)

    def save(self, file_path):
        tam_content = {
            "metadata": self.metadata,
            "text": self.text,
            "media": self.media
        }
        with open(file_path, "w") as tam_file:
            json.dump(tam_content, tam_file)

    @classmethod
    def load(cls, file_path):
        with open(file_path, "r") as tam_file:
            tam_content = json.load(tam_file)
            text = tam_content.get("text", "")
            media = tam_content.get("media", [])
            metadata = tam_content.get("metadata", {})
            return cls(text, media, metadata)

    def list_media(self):
        for idx, media_item in enumerate(self.media):
            print(f"{idx}: {media_item['name']} - {media_item['description']} ({media_item['extension']})")

    def extract_media_by_name(self, media_name, output_path):
        for media_item in self.media:
            if media_item["name"] == media_name:
                with open(output_path + media_item["extension"], "wb") as media_file:
                    media_file.write(base64.b64decode(media_item["data"]))
                return
        print(f"No media found with name: {media_name}")

    def extract_media_by_index(self, index, output_path):
        if 0 <= index < len(self.media):
            media_item = self.media[index]
            with open(output_path + media_item["extension"], "wb") as media_file:
                media_file.write(base64.b64decode(media_item["data"]))
        else:
            print(f"Invalid index: {index}")
