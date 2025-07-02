import asyncio
from fastmcp import Client

client = Client("http://localhost:8001/mcp")

# you can't call the async functions directly 
# so we are making use of the asyncio library.


# async def list_resources():
#     async with client:
#         result = await client.list_resources()
#         print(result)


async def list_tools():
    async with client:
        result = await client.list_tools()
        print(result)

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greeting", {"name": name})
        print(result)



# listing the resources
# print("Getting the resources")
# asyncio.run(list_resources())

# get the list of tools
print("Getting the tool list")
asyncio.run(list_tools())

'''
Getting the tool list
[Tool(name='greeting', title=None, description=None, inputSchema={'properties': {'name': {'title': 'Name', 'type': 'string'}}, 'required': ['name'], 'type': 'object'}, outputSchema={'properties': {'result': {'title': 'Result', 'type': 'string'}}, 'required': ['result'], 'title': '_WrappedResult', 'type': 'object', 'x-fastmcp-wrap-result': True}, annotations=None, meta=None)]
'''

# calling the tool
print("Calling the tool")
asyncio.run(call_tool("Anton"))

'''
Calling the tool
CallToolResult(content=[TextContent(type='text', text='Welcome to MCP Server, Anton!', annotations=None, meta=None)], structured_content={'result': 'Welcome to MCP Server, Anton!'}, data='Welcome to MCP Server, Anton!', is_error=False)
'''
