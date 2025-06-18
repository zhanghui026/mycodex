# Screenshot App Example

This repository demonstrates a minimal screenshot utility written in Python. It
lets you select an area of the screen, capture it and draw simple shapes on the
resulting image.

## Requirements

* Python 3
* Pillow (`pip install pillow`)

Image capturing on some Linux systems also requires the `scrot` package.

## Running

```bash
pip install pillow
python3 screenshot_app/screenshot_app.py
```

Click **Capture**, drag to select the desired region and release the mouse. An
editor window will appear where you can draw red lines or rectangles over the
screenshot.
