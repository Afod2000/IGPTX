#!/bin/python3
import requests
import os
from time import sleep
from huggingface_hub import InferenceApi

# Function to print exit message
def exift():
    print()
    print("\033[1;91m[+]\033[1;92m Thanks for using IGPTX")
    sleep(0.14)
    print("\033[1;91m[~]\033[1;92m Don't forget to follow us on social media")
    sleep(0.14)
    print("\033[1;91m[~]\033[1;92m YouTube: https://youtube.com/@Technolex")
    sleep(0.14)
    print("\033[1;91m[~]\033[1;92m Telegram: https://t.me/LinkCentralX")
    sleep(0.14)
    print("\033[1;91m[~]\033[1;92m GitHub: https://github.com/VritraSecz\n")
    sleep(0.14)

# Function to connect to the Hidden Wiki using Tor with retry mechanism
def access_hidden_wiki(url, max_retries=3):
    print("\033[1;91m[+]\033[1;92m Connecting to the dark web...\033[1;92m")

    proxies = {
        'http': 'socks5h://127.0.0.1:9050',  # Use Tor's SOCKS proxy
        'https': 'socks5h://127.0.0.1:9050'
    }

    for attempt in range(max_retries):
        try:
            response = requests.get(url, proxies=proxies, timeout=30)

            if response.status_code == 200:
                print("\033[1;91m[+]\033[1;92m Successfully connected to the Hidden Wiki!")
                return response.text  # Return Hidden Wiki content
            else:
                print(f"\033[1;91m[!] Failed to connect: Status code {response.status_code}")
        except requests.RequestException as e:
            print(f"\033[1;91m[!] Error on attempt {attempt + 1}: Could not connect to {url}. Details: {e}")
            sleep(5)  # Wait before retrying

    print("\033[1;91m[!] Max retries reached. Unable to connect to the Hidden Wiki.\033[1;92m")
    return None

# Function to use Dolphin Mistral LLM via Hugging Face API to generate code in any language
def generate_code(content, task_type, language, hf_api_token):
    print(f"\033[1;91m[+]\033[1;92m Generating {task_type} code in {language} based on hidden knowledge...\033[1;92m")

    try:
        model_name = "mistralai/Mistral-7B-v0.1"
        inference = InferenceApi(repo_id=model_name, token=hf_api_token)

        # Prompt Dolphin Mistral to generate code in the specified language
        prompt = f"Analyze the following hidden web content and generate a {task_type} script in {language} for pen testing or automation:\n\n{content}\n\n"
        response = inference(prompt)

        code = response.get('generated_text', "No response from the model.")
        return code.strip()
    except Exception as e:
        print(f"\033[1;91m[!] Error consulting the LLM: {e}")
        return "Sorry, I could not process your request at this time."

# Function to check and correct code errors using Dolphin Mistral LLM
def check_and_correct_code(user_code, language, hf_api_token):
    print(f"\033[1;91m[+]\033[1;92m Checking {language} code for errors...\033[1;92m")

    try:
        model_name = "mistralai/Mistral-7B-v0.1"
        inference = InferenceApi(repo_id=model_name, token=hf_api_token)

        # Prompt the model to check for errors and correct the code
        prompt = f"Check the following {language} code for errors, bugs, or inefficiencies and correct it:\n\n{user_code}\n\n"
        response = inference(prompt)

        corrected_code = response.get('generated_text', "No response from the model.")
        return corrected_code.strip()
    except Exception as e:
        print(f"\033[1;91m[!] Error consulting the LLM for code checking: {e}")
        return "Sorry, I could not process your request for code correction at this time."

# Main Program Flow
def igptx():
    # Prompt user for Hugging Face API key
    hf_api_token = input("Please enter your Hugging Face API key: ").strip()
    if not hf_api_token:
        print("\033[1;91m[!] API key is required to proceed. Exiting...\033[1;92m")
        return

    # Define Hidden Wiki URL (example)
    hidden_wiki_url = "http://3g2upl4pq6kufc4m.onion"
    
    print("\033[1;91m[+] IGPTX delves into the shadowy depths...\033[1;92m")

    # Access the Hidden Wiki
    hidden_wiki_content = access_hidden_wiki(hidden_wiki_url)

    if hidden_wiki_content:
        print("\033[1;91m[+] Accessing forbidden knowledge...\033[1;92m")

        # Ask the user for the task type: pen testing or automation
        task_type = input("Enter the type of task (e.g., pen testing, automation): ").strip().lower()

        if task_type not in ['pen testing', 'automation']:
            print("\033[1;91m[!] Invalid task type specified. Exiting...\033[1;92m")
            return

        # Ask the user for the language to generate code in
        language = input("Enter the programming language for the script (e.g., Python, Bash, C, JavaScript): ").strip().lower()

        # Generate code based on the Hidden Wiki content for the specified task type and language
        generated_code = generate_code(hidden_wiki_content, task_type, language, hf_api_token)

        # Display the generated code
        print("\033[1;91m[+] Generated Code in " + language.capitalize() + ":\033[1;92m\n")
        print(generated_code)

        # Ask if the user wants to check the code for errors
        check_code = input("Do you want to check the generated code for errors? (yes/no): ").strip().lower()
        if check_code == 'yes':
            corrected_code = check_and_correct_code(generated_code, language, hf_api_token)
            print("\033[1;91m[+] Corrected Code in " + language.capitalize() + ":\033[1;92m\n")
            print(corrected_code)
        else:
            print("\033[1;91m[+] Skipping error checking...\033[1;92m")
    else:
        print("\033[1;91m[!] Unable to retrieve hidden knowledge at this time.\033[1;92m")

# Run the program
if __name__ == "__main__":
    igptx()