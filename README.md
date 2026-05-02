<h1>SSDoorbell</h1>

A Python-based IoT doorbell for the Raspberry Pi. The system captures a photo when a physical button is pressed, uploads the image to the cloud, sends an email notification with the photo link, and publishes the event data to an MQTT broker.

<h1>Features</h1>

* *Physical Trigger:* Uses a hardware button connected to GPIO 6  
* *Image Capture:* Captures high-quality images using the picamera2 library  
* *Cloud Storage:* Automatically uploads captured photos to Cloudinary  
* *Email Alerts:* Sends an instant email notification via Gmail SMTP  
* *MQTT Connectivity:* Publishes a JSON payload containing the image URL and timestamp to a public broker  

<h1>Hardware</h1>

* Raspberry Pi (with Camera Module installed)  
* Physical button connected to GPIO 6 and GND

* References: Followed https://randomnerdtutorials.com/raspberry-pi-send-email-python-smtp-server/ for STMP gmail code configuration
* Used Week 5 Doorbell script from lab for camera configuration
* Used ChatGPT To edit ReadMe to look nicer with italix text and formatting
