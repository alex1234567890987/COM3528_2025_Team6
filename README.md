# MiroGPT: Reminiscence Therapy for Dementia

Using Miro to deliver reminiscence therapy for dementia patients.

## Description

This program aims to automate reminiscence therapy using a Miro robot. The robot will take the role of the therapist and deliver a conherent convosation with the client, responding with emotions.

## Repository Contents

- `miro_emotions.py`: ROS file controlling MiRo’s emotional expressions (e.g., idle, happy, sad, listening, speaking).
- `start_screen.py`: Tkinter GUI for launching and managing the therapy session.
- `main.py`: FastAPI backend handling webhook input and updating shared state.
- `client_sdk_python_main/`: Patched version of vapi-python sdk
- `vapi_therapist.py`: To start Vapi assistant
- `image_description.py`: Describe the uploaded image to send to Vapi
- `Azure-ttk-theme-main`: Tkinter Theme
- `marg-draft-history.pdf`: A template history
- `requirements.txt`: Python dependencies for the system.
- `README.md`: This file.
- `images/`: some images to test out.

## Getting Started

### Dependencies and Installation

- Must have sudo access to install all packages 

- Must be on at least pip version 25.0.0+

- **ROS Noetic** must be installed and sourced.
-  MiRo robot setup and ROS bridge running.
- Python 3.8+.
  
- must have an `ngrok` account and installed binary (for webhook exposure). (I have left a static ngrok domain in the repo to use  - you may have to reset this in start_screen.py:197)   

  - here is an ngrok guide if there is any problems: 
  - [`ngrok`](https://ngrok.com/download) installed and create an ngrok account.
  - [ngrok Authtoken](https://dashboard.ngrok.com/get-started/setup) set up in your local config with the authtoken.

  - you can set the ngrok token like this:  ngrok config add-authtoken <YOUR_AUTH_TOKEN>

  - IMPORTANT: if your ngrok installion is not at  cd ~ && ./ngrok you must change start_screen.py:197 to point to the correct path


- to install all dependencies run -> pip install -r requirements.txt
  
- common problems might be related to vapi_python installation - this should be solved easily with sudo (for portaudio issues) and pip version (for daily-python issues)
    - if still not then install ddaily-python from here https://pypi.org/project/daily-python/#files and use a recent pip to run pip install on the correct wheel (should be first one)
 

### API SET UP

you must have an openai account, set up an API key and put this in image_description.py and main.py 

you must also have a vapi account, in the dashboard set up a blank template assistant with the prompt located in the appendix of the report, only other settings were to disable background noise 

**EXTREMELY IMPORTANT FOR VAPI EMOTION SET UP**: in the assistant you must put your ngrok static domain in the server url - in order to stream vapi messages - you must put your ngrok auth-token here too - this is easily found on the ngrok website at the top of the page

- ngrok static domain for now is this: https://eminent-sought-beetle.ngrok-free.app (this may get reset before you check and you will have to set it up)

![image](https://github.com/user-attachments/assets/3a59c906-e8d5-4216-9f8d-b1f6e445c839)

![image](https://github.com/user-attachments/assets/992eab4e-4082-4144-9550-9b0560179de4)





### Executing program

clone into your system 

roslaunch COM3528_2025_Team6 miro_therapy.launch


### Using the system
1. Pick a user profile from your device using gui
1. Pick an image to use from your device using gui
1. Press start server
1. Press start therapy
1. Miro will ask a question about something in the picture
1. Press T once to respond to Miro
1. Press T again to finish response
1. Repeat the last 3 steps until you want to end convo
1. Press end call to finish convo
## Help

![Screenshot 2025-05-13 003811](https://github.com/user-attachments/assets/48a66008-8955-45d8-a081-467eb89518f4)


