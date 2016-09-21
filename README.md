# ImagizerPython

The official Python Client for the Imagizer Media Engine

The Imagizer Media Engine accelerates media delivery to your mobile Apps or Webpages by dynamically rescaling, cropping, and compressing images in real time. See all Imagizer features in our [Doc](demo.imagizercdn.com/doc).

## Basic Usage
```python
import imagizer_client

client = imagizer_client.ImagizerClient()

# http://demo.imagizercdn.com/image.jpg?width=200&crop=fit&height=300
url = client.build_url("image.jpg", {
    "width": 200,
    "height": 300,
    "crop": "fit"
})
```
