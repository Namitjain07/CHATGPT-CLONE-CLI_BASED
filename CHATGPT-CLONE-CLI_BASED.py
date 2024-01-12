import openai


openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt=prompt,
        max_tokens=100,
        temperature=0.5,
    )
    return response["choices"][0]["text"]

def main():
    user_input = ""
    
    while user_input != "765":
        user_input = input("Enter a prompt (type '765' to exit): ")
        
        if user_input == "765":
            break
        
        try:
            generated_response = generate_openai_response(user_input)
            print(generated_response)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
