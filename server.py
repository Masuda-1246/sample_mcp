import json
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("reactbits-mcp")

def get_components():
    file_path = "get_components.json"
    with open(file_path, "r") as file:
        return json.load(file)

def get_component_details():
    file_path = "get_component_details.json"
    with open(file_path, "r") as file:
        return json.load(file)

@mcp.tool()
async def get_components():
    return get_components()

@mcp.tool()
async def get_component_detail(component: str):
    components_details = get_component_details()
    return components_details[component]

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
