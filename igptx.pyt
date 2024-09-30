#!/bin/python3
# https://github.com/Afod2000
# Code By: Carderbro
# Modified by: Mr. Matrix
# Don't be a copycat, create your own

import requests
from huggingface_hub import InferenceApi
import os
from time import sleep

# Function to print exit message
def exift():
    print()
    print("\033[1;91m[+]\033[1;92m Thanks for using \033[1;91mMr. Matrix")
    sleep(0.14)
    print("\033[1;91m[~]\033[1;92m Don't forget to follow us on social media")
    sleep(0.14)
    print("\033[1;91m[~]\033[1;92m YouTube:\033[1;94m https://youtube.com/@Technolex")
    sleep(0.14)
    print("\033[1;91m[~]\033[1;92m Telegram:\033[1;94m https://t.me/carderbro345")
    sleep(0.14)
    print("\033[1;91m[~]\033[1;92m GitHub:\033[1;94m https://github.com/Afod2000")
    sleep(0.14)

# Print banner (replace with your banner or logo)
os.system('cat banr')
print("\n\033[1;91m[+] \033[1;92mAsk anything you want. To Exit, just use \033[1;91mexit \033[1;92mor\033[1;91m bye\033[1;92m command.\n")

# Ask for Hugging Face API key at the start
hf_api_token = input("Please enter your Hugging Face API key: ").strip()

if not hf_api_token:
    print("\033[1;91m[!] API key is required to proceed. Exiting...\033[1;92m")
    exit()

# Initialize Hugging Face Inference API for Dolphin Mistral model
model_name = "mistralai/Mistral-7B-v0.1"
inference = InferenceApi(repo_id=model_name, token=hf_api_token)

# Main program loop
while True:
    askx = input("\033[1;91m][\033[1;97mYou\033[1;91m]> \033[1;92m")

    if askx.lower() in ['exit', 'bye']:
        exift()
        break

    if askx == '':
        pass
    else:
        try:
            # Query Hugging Face API using Dolphin Mistral LLM
            prompt = askx
            
            response = inference(prompt)
            
            # Get and display the response text
            answer = response.get('generated_text', "No response from the model.")
            print(f"\n\033[1;91m][\033[1;97mMr. Matrix\033[1;91m]>\033[1;92m {answer.strip()}\n")

        except Exception as e:
            print(f"\033[1;91m[!] Error: {e}\033[1;92m")
