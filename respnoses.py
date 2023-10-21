def handle_response(message) -> str:
    message = message.lower()

    if message == "hi":
        return "Hello there!"
    elif message == "help":
        return "Here is a list of commands:\n"
