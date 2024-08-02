# Notation Engine

Ongoing passion project of experiments with sound in Python

## Overview
(Work in progress)
Notation Engine is a tool designed to automatically transcribe audio recordings into sheet music and provide playback 
functionality. It processes audio files, detects musical notes and rhythms, and generates standard musical notation. 
The service features a web-based interface for users to upload recordings, view transcriptions, and make edits.

## Running Locally

To run the Music Notation Engine locally, you will need to set it up alongside any required services.

### Setup and Installation

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/stevegreghatch/music-notation-engine.git
   cd music-notation-engine

2. **Install Dependencies**:
   - Ensure you have Python and Docker installed.
   - Create a virtual environment and install the necessary Python packages:

     ```sh
     python -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt
     ```

3. **Run the Application**:
   - Start the application:

     ```sh
     python app.py
     ```

4. **Access the Service**:
   - Navigate to `http://localhost:8000` in your web browser to use the application.
