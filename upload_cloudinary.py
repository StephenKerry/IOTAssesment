import cloudinary
import cloudinary.uploader

# Replace these with your actual Cloudinary credentials
cloudinary.config( 
  cloud_name = "ddzx8vocz", 
  api_key = "599369767232934", 
  api_secret = "auzIARoaJjHSQGCOJOSAV8JOkMs" 
)

def upload_image(file_path):
    try:
        response = cloudinary.uploader.upload(file_path)
        return response.get("secure_url")
    except Exception as e:
        print(f"Cloudinary Error: {e}")
        return None
