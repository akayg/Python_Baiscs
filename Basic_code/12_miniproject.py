import json

def beautify_json(json_string):
    """
    Beautifies a JSON string by formatting it with indentation.
    """
    try:
        parsed_json = json.loads(json_string)
        beautified_json = json.dumps(parsed_json, indent=4, sort_keys=True)
        return beautified_json
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e}"

def main():
    print("Welcome to the JSON Beautifier!")
    print("Enter your JSON string below (or type 'exit' to quit):")
    
    while True:
        user_input = input("\nJSON Input: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        result = beautify_json(user_input)
        print("\nBeautified JSON:")
        print(result)

if __name__ == "__main__":
    main()