"""Say Hello, World or the message received from user input"""
from agavepy.actors import get_context


def say_hello_world(m):
    """Print message from user if present, else echo "Hello, World"""
    # if user input is an empty message
    if m == " ":
        print("Actor says: Hello, World")
    # print the user input message
    else:
        print("Actor received message: {}".format(m))


def main():
    """Main entry to grab message context from user input"""
    context = get_context()
    message = context['raw_message']
    say_hello_world(message)


if __name__ == '__main__':
    main()
