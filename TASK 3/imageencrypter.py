from PIL import Image
import os

def encrypt_image(input_path, output_path, key=50):
    try:
        img = Image.open(input_path).convert("RGB")
        pixels = img.load()
        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                pixels[x, y] = (r, g, b)

        img.save(output_path)
        print("✅ Image encrypted and saved as:", output_path)

    except FileNotFoundError:
        print("❌ File not found. Make sure the image", input_path, "exists.")
    except Exception as e:
        print("❌ Error during encryption:", e)

def decrypt_image(input_path, output_path, key=50):
    try:
        img = Image.open(input_path).convert("RGB")
        pixels = img.load()
        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                pixels[x, y] = (r, g, b)

        img.save(output_path)
        print("✅ Image decrypted and saved as:", output_path)

    except FileNotFoundError:
        print("❌ File not found. Make sure the image", input_path, "exists.")
    except Exception as e:
        print("❌ Error during decryption:", e)

print("📁 Available files in directory:")
print(os.listdir("."))

original_image = "i.jpg"
encrypted_image = "encrypted.png"
decrypted_image = "decrypted.png"

encrypt_image(original_image, encrypted_image)
decrypt_image(encrypted_image, decrypted_image)
