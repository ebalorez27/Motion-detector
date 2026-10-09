# Motion Detector

A small Python app that detects motion in a video and highlights moving areas with green boxes. You can use your webcam or select a video file.

## What you'll need

* Python 3.10 or newer
* A webcam if you want to use camera mode

## Get started on Windows

Open PowerShell in the project folder and run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python .\motion_detector.py
```

If PowerShell won't let you activate the virtual environment, you can run the app directly with:

```powershell
.\.venv\Scripts\python.exe .\motion_detector.py
```

## Using the app

Choose `webcam` to use your camera, or `file` to browse for a video. Video files can be MP4, AVI, or MOV. Press `q` to close the video window.

## Project files

* `motion_detector.py` — the motion detection app
* `requirements.txt` — Python dependencies
* `.gitignore` — files Git should leave out
* `demo/` — demonstration videos
