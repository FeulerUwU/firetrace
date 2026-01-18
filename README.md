FireTrace 🔥

FireTrace is a lightweight, offline metadata sanitizer designed for privacy-conscious users who value basic OPSEC (Operations Security) hygiene.

In a digital world where every file carries a hidden history, FireTrace helps you reclaim your privacy. It strips away residual metadata without touching the actual content of your files. No cloud, no tracking, no footprints.
✨ Key Features

    Multi-Format Support: Clean metadata from JPG, JPEG, PNG, and PDF files effortlessly.

    Safety First: Cleaned files are saved to your Desktop with a -clean suffix, keeping your originals untouched.

    Sleek UI: A modern, intuitive interface powered by PyQt6.

    Custom Themes: Choose the look that fits your workflow: AMOLED, Dark, or Light.

    Privacy by Design: Fully offline operation. No network requests, no data collection, and zero server interaction.

🔥 Why "FIRE"?

The name FIRE symbolizes the process of "burning away" digital traces.

Unlike simple editing tools, FireTrace doesn't just hide data—it reconstructs the file using only the essential raw data, ensuring that hidden "ghost" information is left behind in the ashes.
🧠 What gets cleaned?
Images (JPG / PNG)

    EXIF Data: Timestamps, shutter speed, and exposure settings.

    GPS Coordinates: Precise location data where the photo was taken.

    Device Profiles: Specific camera or smartphone hardware info.

    Software Tags: Traces left by editing software (Photoshop, GIMP, etc.).

Images are rebuilt from raw pixel data, resulting in a fresh file free of embedded history.
PDFs

    Document Properties: Author names, titles, and software producers.

    Note: Advanced embedded metadata (such as complex XMP streams) may not be fully stripped in the current version.

⚠️ Important Limitations

FireTrace is a privacy tool, not a forensic destruction utility. To remain transparent:

    It does not alter OS-level file system timestamps.

    It does not clear system-wide thumbnail caches.

    It does not remove NTFS Alternate Data Streams (ADS).
