# mcp-playground
model control protocol playground with various services

There are a lot of Junk advice on the Internet mainly to promote each ones libraries.
With just fastMCP you can run both the server and client.  

You don't need an LLM to interact with MCP client and Server.  

You can just create a server and then using the client directly call the server. This is very useful for testing your MCP server and tools before bringing on the LLM.

This example shows this approach.

Once tested, this can be connected to the LLM.

The approach followed is to expose the server on a http port so that this can be hosted remotely.
Most examples on the Internet wants to run locally. This won't be the case as your client won't be having python or any execution environment for this code to run locally.  

Always use a remote server so that the client can connect to the server hosted remotely.

Install uv if you haven't already  
`curl -LsSf https://astral.sh/uv/install.sh | sh`

Create a virtual environment  
`uv venv`  

Activate the virtual environment  
`source .venv/bin/activate`

### Start the server in a separate terminal
`uv run greetings-server.py`

### Run the client in a separate terminal
`uv run mcp-client.py`

### To open the MCP inspector
first run the MCP Server  
`uv run calculator-server.py`  


Then run the inspector    

`fastmcp dev calculator-server.py`

use the inspector URL with the security token in the browser.

`  http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=234d31f8df1bdebf0c879285724860d39791afdfd651d7296be8d0d233ef7e11`

Select the MCP server for http transport  
enter the MCP server details
`http://localhost:8002/mcp  `

Now you can interact with the prompts, tools and resources.  

