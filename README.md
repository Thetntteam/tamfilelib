# TAMFile Library

Library for creating and reading TAM (Text and Media) files.

## Installation

You can install the library using pip:

pip install tamfile

## Usage

### Creating a TAM File

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
Loading and Extracting Media from a TAM File
```python
from tamfile import TAMFile

# Load a TAM file
tam = TAMFile.load("example.tam")

# Extract media
tam.extract_media("media1", "output/path/media1")
tam.extract_media("media2", "output/path/media2")

```
