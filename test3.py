import os
import shutil

def rename_file(input_folder, output_folder):
  """
  Renames all files with 'cfg' extension to 'png' in the input folder.

  Args:
    input_folder: Path to the input folder containing the files.
    output_folder: Path to the output folder where the renamed files will be saved.

  Raises:
    FileNotFoundError: If the input folder does not exist.
  """

  if not os.path.exists(input_folder):
    raise FileNotFoundError(f"Input folder '{input_folder}' not found.")

  if not os.path.exists(output_folder):
    os.makedirs(output_folder)

  for filename in os.listdir(input_folder):
    if filename.endswith(".cfg"):
      src_path = os.path.join(input_folder, filename)
      new_filename = os.path.splitext(filename)[0] + ".png"
      dst_path = os.path.join(output_folder, new_filename)
      shutil.copy2(src_path, dst_path)

# Example usage:
input_dir = "/path/to/your/input/folder"
output_dir = r"D:\itokiana_png"
rename_file(input_dir, output_dir)