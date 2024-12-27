## Environment

Please use requirements.txt to install Python packages needed.
Provide your own Gemini API key in the following line. You can get the key in Google AI Studio.
```python
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
```
Either set GEMINI_API_KEY environment variable with your key, or directly write your key in the code.

## Usage
```bash
python genai_queries.py
```
Enter the address of the property from the terminal and press Enter
```bash
Enter the address of the property: 
```
Wait until the following is printed on the terminal:
```bash
Response written to property_info.txt
Response written to school_info.txt
```
The information will be stored in property_info.txt and school_info.txt

## Test Cases
Empty or invalid address: the terminal will prompt the user to re-enter
```bash
Invalid address. Please re-enter
Enter the address of the property: 
```
990 Capitola Way, Santa Clara, CA 95051\
1-1 Chiyoda, Chiyoda City, Tokyo 100-8111, Japan\
1085 Tasman Dr, Sunnyvale, CA 94089
