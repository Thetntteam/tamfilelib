# TAMFile Library
https://pypi.org/project/tamfile/1.0.2/
Library for creating and reading TAM (Text and Media) files.

## Installation

You can install the library using pip:

pip install tamfile

## Usage

### Creating a TAM File
The following example demonstrates how to create a TAM file, add media to it, and save it.
```python
from tamfile import TAMFile

# Create a TAMFile instance
tam = TAMFile(text="This is a test text", metadata={"author": "Your Name"})

# Add media
tam.add_media("media1", "path/to/media1.jpg", "This is a description for media1")
tam.add_media("media2", "path/to/media2.mp4", "This is a description for media2")

# Save the TAM file
tam.save("example.tam")
```
### Loading and Extracting Media from a TAM File
The following example demonstrates how to load a TAM file, display its content, and extract all media files.

```python
import os
from tamfile import TAMFile

def extract_all_media(tam_file, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for idx, media in enumerate(tam_file.media):
        media_name = media['name']
        media_extension = media['extension']
        output_path = f"{output_dir}/{media_name}{media_extension}"
        tam_file.extract_media_by_index(idx, output_path)
        print(f"Extracted {media_name} to {output_path}")

def main():
    # Load the TAM file
    tam_file = TAMFile.load("test_document.tam")
    
    # Display the text and author to the console
    print("Text Content:", tam_file.text)
    print("Author:", tam_file.metadata.get("author", "Unknown"))
    
    # Extract all media
    extract_all_media(tam_file, "extracted_media")

if __name__ == "__main__":
    main()

```
## Function Explanations
TAMFile
Description: The TAMFile class represents a TAM file, which contains text content, media files, and metadata.

__init__(self, text="", media=None, metadata=None)
Parameters:

text (str): The text content of the TAM file.
media (list): A list of media items (each media item is a dictionary containing media details).
metadata (dict): Metadata about the TAM file, such as version, author, and creation date.
Description: Initializes a TAMFile instance with the provided text, media, and metadata. If no media or metadata is provided, it initializes with an empty list for media and default metadata.

add_media(self, media_name, media_path, description="")
Parameters:

media_name (str): The name of the media item.
media_path (str): The file path to the media item.
description (str): A description of the media item.
Description: Adds a media item to the TAM file. The media file is read and encoded in base64 format.

save(self, file_path)
Parameters:

file_path (str): The file path where the TAM file will be saved.
Description: Saves the TAM file content, including text, media, and metadata, to a JSON file at the specified path.

load(cls, file_path)
Parameters:

file_path (str): The file path from which to load the TAM file.
Returns: TAMFile instance

Description: Loads a TAM file from the specified file path and returns a TAMFile instance containing the loaded content.

extract_media(self, media_name, output_path)
Parameters:

media_name (str): The name of the media item to extract.
output_path (str): The file path where the extracted media will be saved.
Description: Extracts a specific media item from the TAM file by name and saves it to the specified output path.

extract_media_by_index(self, index, output_path)
Parameters:

index (int): The index of the media item to extract.
output_path (str): The file path where the extracted media will be saved.
Description: Extracts a specific media item from the TAM file by its index and saves it to the specified output path.

If you need help join https://discord.gg/ADFYwR8jvg
