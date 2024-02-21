"""

** Requirements:
- Give a UNKNOWN NESTED LEVEL dictionary. We don't know the dictionary's shape or any dictionary's metadata
- Write a function to remove all newline charactors on all string value in dict
- All other value's data type is kept normally
- All two or more whitespace charactors side by side should be replaced by single string

** For example: 
* This dictionary below is messy and we need to remove all newline charactors
dict_sample_1 = {
    "texts": [
        "text_1": {
            "title": "The \n\n spiderman",
            "content": "This is the content\n\n. After new line\n. Final new line\n"
        },
        "text_2": {
            "rate": 4.5,
            "content": "Content has\n\n"
        },
        "text_3": {
            "sub_text": {
                "title": "Title contains \n and\n"
            }
        }
    ],
    "description": "This description has\n\n",
    "user_001": {
        "name": "John \n\n Smith"
    }
}

*The correct output should be
processed_dict = {
    "texts": [
        "text_1": {
            "title": "The spiderman",
            "content": "This is the content. After new line. Final new line"
        },
        "text_2": {
            "rate": 4.5,
            "content": "Content has"
        },
        "text_3": {
            "sub_text": {
                "title": "Title contains and"
            }
        }
    ],
    "description": "This description has",
    "user_001": {
        "name": "John Smith"
    }
}

"""

def extracted_dict_string(raw_dict: dict):
    new_dict = raw_dict
    # TODO: Write your code to change new_dict here
    return new_dict