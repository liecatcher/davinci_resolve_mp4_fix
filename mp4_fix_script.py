import subprocess
import os
import argparse


def check_and_convert_video(input_file, output_file):
    """
    Checks the video file for an audio track and, if necessary,
    converts it for compatibility with DaVinci Resolve.
    """
    try:
        # Check audio codec using ffprobe
        probe_command = [
            'ffprobe', '-v', 'error', '-select_streams', 'a:0',
            '-show_entries', 'stream=codec_name', '-of', 'default=noprint_wrappers=1:nokey=1',
            input_file
        ]
        codec_name = subprocess.check_output(probe_command, stderr=subprocess.STDOUT, text=True).strip()

        if not codec_name:
            print(f"❗ No audio track found in file '{os.path.basename(input_file)}'. Skipping.")
            return

        print(f"✅ Found audio codec: {codec_name}")
        print("Starting conversion...")

        convert_command = [
            'ffmpeg', '-i', input_file, '-c:v', 'copy', '-c:a', 'aac',
            '-b:a', '192k', '-y', output_file
        ]
        subprocess.run(convert_command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        print(f"🎉 Conversion of '{os.path.basename(input_file)}' completed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"❌ Error executing FFmpeg for file '{os.path.basename(input_file)}': {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred for file '{os.path.basename(input_file)}': {e}")


def process_folder(input_folder, output_folder):
    """
    Processes all MP4 files in the specified folder.
    """
    if not os.path.isdir(input_folder):
        print(f"Error: Folder not found at path {input_folder}")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created a folder for saving results: {output_folder}")

    files_processed = 0
    for filename in os.listdir(input_folder):
        if filename.endswith('.mp4'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            print(f"\n--- Processing file: {filename} ---")
            check_and_convert_video(input_path, output_path)
            files_processed += 1

    if files_processed == 0:
        print("\nNo MP4 files to process in the specified folder.")
    else:
        print(f"\n✅ All files processed. {files_processed} file(s) checked and/or converted.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Converts audio tracks of MP4 files for compatibility with DaVinci Resolve.")
    parser.add_argument('input_folder', type=str, help="Path to the folder with source MP4 files.")
    parser.add_argument('--output', dest='output_folder', type=str,
                        help="Path to the folder for saving converted files. Defaults to creating an 'output' folder inside the input folder.",
                        default=None)

    args = parser.parse_args()

    input_dir = args.input_folder
    output_dir = args.output_folder

    # If the output folder is not specified, create 'output' inside the input folder
    if output_dir is None:
        output_dir = os.path.join(input_dir, 'output')

    try:
        process_folder(input_dir, output_dir)
    except FileNotFoundError:
        print("\n❌ Error: FFmpeg or ffprobe not found. Make sure they are installed and available in your PATH.")
