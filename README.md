# CHATGPT-CLONE-CLI_BASED
IT IS A CODE SNIPPET WRITTEN IN PYTHON WHICH CLONES THE CHATGPT(AI CHAT BOT)

## Prerequisites

- Python 3.x
- OpenAI API key (sign up at [OpenAI](https://beta.openai.com/signup/) to obtain your key)

## Setup

1. Install required packages:

    ```bash
    pip install openai
    ```

2. Set your OpenAI API key:

    Replace `"YOUR_OPENAI_API_KEY"` in the script with your actual API key. For security, consider using environment variables.

## Usage

Run the script and follow the on-screen prompts to input your desired text prompt. The script will then make a call to the OpenAI API and display the generated response.

To exit the program, enter the special prompt `765`.

```bash
python openai_script.py
```

## Notes

- This script uses the OpenAI GPT-3.5 "text-curie-001" engine with default settings (max_tokens=100, temperature=0.5). Feel free to customize these parameters based on your requirements.

- In case of any errors during the API call, the script will display an error message.

## Disclaimer

Ensure compliance with OpenAI's usage policies and guidelines. Refer to the [OpenAI documentation](https://beta.openai.com/docs/) for more details.

---
