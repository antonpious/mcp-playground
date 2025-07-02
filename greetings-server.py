# This is the library
# that abstract MCP implementation
from fastmcp import FastMCP

mcp = FastMCP("Greetings MCP Server")


# create a tool for greeting
@mcp.tool
def greeting(name: str) -> str:

    if name:
        # return the greeting with name
        output = f"Welcome to MCP Server, {name}!"
    else:
        output = "welcome to MCP Server, Guest!"
    
    return output


'''
Why do we need the if __name__ == "__main__": block?

Within the FastMCP ecosystem, this line may be unnecessary. However, including it ensures that your FastMCP server runs for all users and clients in a consistent way and is therefore recommended as best practice.

If you execute the script, python would look
for the main method and run that
uv run greetings-server.py

'''

# this would run MCP on a remote http port
# on local host
if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8001)
   

