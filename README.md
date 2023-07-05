# Image Downloader

Image Downloader is a Python script that downloads images from a file containing image URLs.

## Prerequisites

- Python 3.x
- requests library (`pip install requests`)

## Usage

1. Place the file containing image URLs in the `inputs` directory. Each URL should be on a separate line.

2. Run the script using the following command:

   ```shell
   python image_downloader.py <file> [-o <output_dir>]
   ```

   - `<file>`: Path to the file containing image URLs (required).
   - `-o, --output-dir`: Output directory for downloaded images (optional, default: `images`).

3. The downloaded images will be saved in the specified output directory.

## Example

To download images from a file named `image_urls.txt` and save them in the `outputs` directory, run the following command:

```shell
python image_downloader.py inputs/image_urls.txt -o outputs/
```
