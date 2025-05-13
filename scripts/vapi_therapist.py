#from vapi_python import Vapi

from client_sdk_python_main.vapi_python.vapi_python import Vapi  # use this if buffering is an issue on uni laptop
from client_sdk_python_main.vapi_python.daily_call import DailyCall

class Vapi_TheRapist:
    def __init__(self, image_description, patient_history, audio_queue):
        # Initialise Vapi client
        self.daily_call = DailyCall(audio_queue)  # ← start Daily first
        self.assistant = Vapi(api_key="a47017e1-76b2-40fd-8c5e-19eee6b056a2", daily_client=self.daily_call)
        self.image_description = image_description
        self.patient_history = patient_history
        self.audio_queue = audio_queue

    def create_and_start_assistant(self):
        assistant_overrides = {
            "recordingEnabled": False,
            "model": {
                "provider": "openai",
                "model": "gpt-4o",
                "emotionRecognitionEnabled": True
            },
            "variableValues": {
                "image_description": self.image_description,
                "patient_history_pdf": self.patient_history
            }
        }

        # Start the Vapi assistant
        self.assistant.start(
            assistant_id='ba05d6d9-8f92-4065-b88b-ecef1ea39d69',
            assistant_overrides=assistant_overrides
        )

    def stop_assistant(self):
        self.assistant.stop()
