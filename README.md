

# Screenshot Annotation App

A simple example repository demonstrating how to build a macOS application that captures screenshots and lets you annotate them.

## Prerequisites

- macOS 12 or later
- Xcode 14 or later
- Swift 5.7 or later

## Build Steps

1. Clone this repository.
2. Open `ScreenshotApp.xcodeproj` in Xcode.
3. Click **Run** in Xcode or use `xcodebuild` to build from the command line.

## Usage Example

1. Launch the application.
2. Use the capture button or your preferred screenshot shortcut to take a shot.
3. Annotate the image using the provided tools.
4. Save or share the annotated screenshot.
=======
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

