from PIL import Image
import os

def convert_to_webp(input_path, output_path):
    try:
        image = Image.open(input_path)
        image.save(output_path, "webp")
        print(f"Converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

def batch_convert(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.webp'
            output_path = os.path.join(output_folder, output_filename)
            convert_to_webp(input_path, output_path)

if __name__ == "__main__":
    input_folder = "input_images"  # Replace with your input folder path
    output_folder = "output_images"  # Replace with your output folder path
    batch_convert(input_folder, output_folder)