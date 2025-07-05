from fastmcp import FastMCP

mcp = FastMCP("Calculator MCP Server")

# Tools Section #

# Register the add function
@mcp.tool()
def add(num1: int, num2: int) -> int:
    """Add two number and return the result"""
    return num1+ num2

# Register the subtract function
@mcp.tool()
def subtract(num1: int, num2: int) -> int:
    """Subract two numbers and return the result""" 
    return num1 - num2

# Register the multiple function
@mcp.tool()
def multiply(num1: int, num2: int) -> int:
    """ Multiple two numbers and return the result"""
    return num1 * num2

# Register the divide function
@mcp.tool()
def divide(num1: float, num2:float) -> float:
    """ Divide the first number by second. Raise error on division by zero """
    # This raises the error
    # so when using it that function should 
    # catch it and send a string back for response
    if num2 == 0:
        raise ValueError("Division by zero")
    return num1/num2


# Resource Section
# Add a dynamic resource
@mcp.resource("calculator://greet/{name}")
def calculator_greeting(name: str) -> str:
    """ Get a personalized greeting for using the service"""
    return f"Hi, {name}! what calculations do you want to do today?"

# Add a static resource
@mcp.resource("usage://guide")
def get_usage()-> str:
    with open("docs/usage.txt") as file:
        return file.read()


def add_second(num1, num2):
    return num1 + num2

# Creating the valid prompts for the calculator service
# Note: This can't call any of the function which are declared
# as tool.
# This is not a good prompt implementation
# The prompt should return a prompt so that the result
# can be passed to an LLM to obtain the actual result
# Here the prompt is already displaying the end result.
@mcp.prompt()
def calculator_prompt(num1: float, num2: float, operation: str)-> str:
    """ Prompt for a calculation involving two numbers and returning the result"""

    # after the attribution of tool the method is not longer callable.
    # we can't call the function now
    if operation == "add":
        result = add_second(num1, num2)
        return f"The result of adding {num1} and {num2} is {result}"
    elif operation == "subtract":
        return f"The result of subtracting {num1} and {num2} is {subtract(num1, num2)}"
    elif operation == "multiple":
        return f"The result of multiplying {num1} and {num2} is {multiply(num1, num2)}"
    elif operation == "divide":
        try:
            return f"The result of diving {num1} and {num2} is {divide(num1, num2)}"
        except ValueError as e:
            return str(e)
    else:
        return "Invalid operation, Please choose add, subtract, multiply or divide"



if __name__ == "__main__":
    mcp.run(
        transport = "http", 
        host = "127.0.0.1", 
        port = 8002)