### README.md

### The Problem: No Audio in DaVinci Resolve 🧐

You've imported an MP4 video into **DaVinci Resolve**, but the audio track is empty, even though the video has sound when played elsewhere. This happens because the MP4 file uses an audio codec (like **AC3**) that DaVinci Resolve doesn't support.

This script fixes the issue by **re-encoding just the audio** into a compatible format (AAC), leaving the video untouched. This is a fast and efficient solution that preserves video quality.

---

### What You Need 🛠️

You need to have **FFmpeg** installed on your system. It's a free and powerful tool for handling media files.

* **On macOS:**
    1.  Open **Terminal**.
    2.  Install **Homebrew** (a package manager) if you don't have it:
        ```sh
        /bin/bash -c "$(curl -fsSL [https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh](https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh))"
        ```
    3.  Then, install FFmpeg:
        ```sh
        brew install ffmpeg
        ```

* **On Windows:**
    1.  Download **FFmpeg** from its [official website](https://ffmpeg.org/download.html).
    2.  Add the paths to the `ffmpeg.exe` and `ffprobe.exe` files to your system's **PATH** variable.

---

### How to Use the Script 🚀

1.  Save the Python script as `mp4_fix_script.py`.
2.  Open your command-line interface: **Terminal** on macOS or **Command Prompt** on Windows.
3.  Navigate to the folder where you saved the script using the `cd` command.
    * **macOS Example:** `cd ~/Desktop`
    * **Windows Example:** `cd C:\Users\YOUR_USERNAME\Desktop`
4.  Run the script by providing the path to your video folder.

---

### Usage Options ⚙️
### Option 1: Save to a New `output` Folder

The script will automatically create an `output` folder inside your video folder and place the fixed files there.

```sh
python mp4_fix_script.py "path/to/your/videos"
```
Example: python mp4_fix_script.py "~/Movies/My_Videos"

### Option 2: Save to a Different Folder

Use the --output parameter to specify a different destination for the fixed files.

```sh
python mp4_fix_script.py "path/to/source/folder" --output "path/to/results/folder"
```
Example: python mp4_fix_script.py "~/Movies/My_Videos" --output "~/Desktop/Fixed_Videos"

After the script finishes, you can import the new files into DaVinci Resolve. The audio track should now be visible and working! 🎉



