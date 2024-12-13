# Decoding a Secret Message

## Overview

This program retrieves and parses a Google Doc containing a list of Unicode characters and their coordinates in a 2D grid. It then reconstructs and displays the grid, revealing a secret message formed by uppercase letters.

---

## Code Explanation (Step-by-Step)

### **1. Importing Libraries**
```python
from bs4 import BeautifulSoup
import requests
```
- **`BeautifulSoup`**: Used to parse and extract meaningful data from the HTML of the Google Doc.
- **`requests`**: Used to make HTTP requests to retrieve the document's content.

---

### **2. Function Definition**
```python
def extract_data_and_display_grid(doc_url):
```
- This function takes a single argument, `doc_url`, which is the URL of the Google Doc containing the grid data.

---

### **3. Fetching Document Content**
```python
response = requests.get(doc_url)

if response.status_code != 200:
    print(f"Error: Unable to fetch the document. (Status code: {response.status_code})")
    return
```
- **`requests.get(doc_url)`**: Sends a GET request to fetch the content of the document.
- Checks if the request is successful using `response.status_code`. If not (`200` indicates success), it prints an error and exits the function.

---

### **4. Parsing the Document**
```python
soup = BeautifulSoup(response.text, 'html.parser')
data = soup.get_text("\n").strip().splitlines()
```
- **`BeautifulSoup(response.text, 'html.parser')`**: Parses the HTML content of the document.
- **`get_text("\n")`**: Extracts plain text, separating lines with `\n`.
- **`splitlines()`**: Splits the text into a list of lines.

---

### **5. Extracting the Relevant Data**
```python
start_actual_data = False
actual_data = []

for item in data:
    if start_actual_data:
        actual_data.append(item)
    else:
        if item == 'y-coordinate':
            start_actual_data = True
```
- **`start_actual_data`**: A flag that ensures the program processes lines only after the header `y-coordinate` is encountered.
- **`actual_data`**: Collects all relevant lines after the header for further processing.

---

### **6. Building the Coordinates Dictionary**
```python
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
```
- **`coordinates`**: A dictionary where keys are `(x, y)` tuples, and values are the corresponding characters.
- **`index % 3 == 0`**: Indicates the x-coordinate.
- **`index % 3 == 1`**: Indicates the character.
- **`index % 3 == 2`**: Indicates the y-coordinate.

---

### **7. Calculating the Grid Size**
```python
max_x = max(co[0] for co in coordinates) + 1
max_y = max(co[1] for co in coordinates) + 1
```
- **`max(co[0] for co in coordinates)`**: Finds the maximum x-coordinate.
- **`max(co[1] for co in coordinates)`**: Finds the maximum y-coordinate.
- Adds `1` to both to account for the zero-based index and determine the grid size.

---

### **8. Creating and Filling the Grid**
```python
grid = [[' ' for _ in range(max_x)] for _ in range(max_y)]

for (x, y), character in coordinates.items():
    grid[y][x] = character
```
- **`[[' ' for _ in range(max_x)] for _ in range(max_y)]`**: Initializes a 2D grid filled with spaces.
- Loops through `coordinates` and places each character at its respective `(x, y)` position.

---

### **9. Displaying the Grid**
```python
for y in range(max_y - 1, -1, -1):
    print(''.join(grid[y]))
```
- Loops from the highest `y` to the lowest (`max_y - 1` to `0`) to print the grid in the correct orientation.
- **`''.join(grid[y])`**: Joins the characters in each row into a string for printing.

---

### **10. Calling the Function**
```python
doc_url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
extract_data_and_display_grid(doc_url)
```
- **`doc_url`**: The URL of the Google Doc containing the grid data.
- **`extract_data_and_display_grid(doc_url)`**: Executes the function with the provided URL.

---

## Output
The program displays a grid of characters, with each character correctly placed according to its `(x, y)` coordinates, revealing the secret message.

---