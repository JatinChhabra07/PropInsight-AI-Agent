from app.graph import app

def main():
    print("Starting Agent")

    file_path = "data/rent_roll.xlsx"

    initial_state = {
        "messages":[
            ("user", f"Analyze the rent roll at {file_path}")
        ]
    }

    result = app.invoke(initial_state)

    last_message = result["messages"][-1]
    print("AI Response: ")
    print(last_message)

    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        print("\n🛠️  Tool Call Detected:")
        print(last_message.tool_calls)

if __name__ == "__main__":
    main()