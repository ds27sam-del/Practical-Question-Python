import requests
from mcp.server.fastmcp import FastMCP

# 1. Initialize the FastMCP server
mcp = FastMCP("Music Search Server")

# 2. Use the @mcp.tool() decorator to expose this function to the AI
@mcp.tool()
def search_music(term: str, limit: int = 3) -> str:
    """
    Search the iTunes API for a specific artist or song.
    
    Args:
        term: The name of the artist (e.g., 'Satinder Sartaaj') or track.
        limit: The maximum number of results to return.
    """
    url = "https://itunes.apple.com/search"
    params = {"term": term, "media": "music", "limit": limit}
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        results = []
        for track in data.get('results', []):
            song = track.get('trackName')
            album = track.get('collectionName')
            results.append(f"Song: {song} | Album: {album}")
            
        return "\n".join(results) if results else "No results found."
    
    return f"Failed to retrieve data. Status code: {response.status_code}"

# 3. Make the server executable
if __name__ == "__main__":
    mcp.run()