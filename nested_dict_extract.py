"""

** Requirements:
- Give a UNKNOWN NESTED LEVEL dictionary. We don't know the dictionary's shape or any dictionary's metadata
- Write a function to remove all the newline characters \n and the escaped newline characters \\n on all string value in dict
- All other value's data type is kept normally
- All two or more consecutive whitespace characters should be replaced by single whitespace
"""

# For example: 
# This dictionary below is messy and we need to remove all newline charactors
dict_sample_1 = {
    "texts": [
        {
            "title": "The \n\n spiderman",
            "content": "This is the content\n\n. After new line\n. Final new line\n"
        },
        {
            "rate": 4.5,
            "content": "Content has\n\n"
        },
        "This is the text with newline \\n\\n",
        {
            "random_array": ["Hello \n \\n World", "No new line"],
            "string": "This is a random string\n\n",
        }
    ],
    "description": "This description has\n\n",
    "user_001": {
        "name": "John \n\n Smith"
    }
}

# The correct output should be
processed_dict = {
    "texts": [
        {
            "title": "The spiderman",
            "content": "This is the content. After new line. Final new line"
        },
        {
            "rate": 4.5,
            "content": "Content has"
        },
        "This is the text with newline",
        {
            "random_array": ["Hello World", "No new line"],
            "string": "This is a random string",
        }
    ],
    "description": "This description has",
    "user_001": {
        "name": "John Smith"
    }
}



def process_dict_string(raw_dict: dict):
    new_dict = raw_dict
    # TODO: Write your code to change new_dict here
    return new_dict
