from bs4 import BeautifulSoup
import requests

def extract_data_and_display_grid(doc_url):
    # Extracting the contents from the Google Doc url
    response = requests.get(doc_url)
    
    if response.status_code != 200:
        print(f"Error: Unable to fetch the document. (Status code: {response.status_code})")
        return
    
    # Parsing the document content from Google doc
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.get_text("\n").strip().splitlines()
    
    start_actual_data = False
    actual_data = []
    for item in data:
        if start_actual_data:
            actual_data.append(item)
        else:
            if item == 'y-coordinate':
                start_actual_data = True
            
    print("Actual data: " + str(actual_data))
    
    # Creating a dictionary to hold the characters and coordinates that is read from doc
    coordinates = {}
    x = 0
    y = 0
    character = ""
    for index, item in enumerate(actual_data):
        if index % 3 == 0:
            x = int(item.strip())
        if index % 3 == 1:
            character = item
        if index % 3 == 2:
            y = int(item.strip())
            coordinates[(x, y)] = character
    print("Coordinates: " + str(coordinates))
    
    # Calculating maximum size of the grid
    max_x = max(co[0] for co in coordinates) + 1
    max_y = max(co[1] for co in coordinates) + 1
    
    print("Max x,y: " + str(max_x), str(max_y))
    
    # Creating and filling the grid
    grid = [[' ' for _ in range(max_x)] for _ in range(max_y)]
    
    for (x, y), character in coordinates.items():
        grid[y][x] = character
    
    # Displaying the grid
    for y in range(max_y - 1, -1, -1):  # Reversing the order of rows so that max valued cell is displayed first
        print(''.join(grid[y]))


doc_url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
# doc_url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"

extract_data_and_display_grid(doc_url)