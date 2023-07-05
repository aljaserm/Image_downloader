import requests
import os
import argparse


def download_images(file_path, output_dir):
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  with open(file_path, 'r') as file:
    for line in file:
      image_url = line.strip()
      if image_url:
        download_image(image_url, output_dir)

  print('Images downloaded successfully!')


def download_image(image_url, output_dir):
  try:
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
      filename = image_url.split('/')[-1]
      save_path = os.path.join(output_dir, filename)
      with open(save_path, 'wb') as file:
        for chunk in response.iter_content(1024):
          file.write(chunk)
      print('Downloaded:', image_url)
    else:
      print('Failed to download:', image_url)
  except requests.exceptions.RequestException as e:
    print('Failed to download:', image_url)
    print(e)


def main():
  parser = argparse.ArgumentParser(description='Image Downloader')
  parser.add_argument('file', help='Path to the file containing image URLs')
  parser.add_argument('-o',
                      '--output-dir',
                      help='Output directory for downloaded images',
                      default='images')
  args = parser.parse_args()

  download_images(args.file, args.output_dir)


if __name__ == '__main__':
  main()
