import math
import json

squared=math.sqrt(30)
print("square root of 30 is ", math.ceil(squared))

def greeting(name):
    print("Hello " + name)
    

sample_data={
"quiz": {
        "sport": {
            "q1": {
                "question": "Which one is correct team name in NBA?",
                "options": [
                    "New York Bulls",
                    "Los Angeles Kings",
                    "Golden State Warriros",
                    "Huston Rocket"
                ],
                "answer": "Huston Rocket"
            }
        },
        "maths": {
            "q1": {
                "question": "5 + 7 = ?",
                "options": [
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "answer": "12"
            },
            "q2": {
                "question": "12 - 8 = ?",
                "options": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "answer": "4"
            }
        }
    }
}

response=json.dumps(sample_data)
print(response)


data=[1,2,3,4,5,6,7,8,9,10]
chunk_size=3
for i in range(0,len(data),chunk_size):
    chunk=data[i:i + chunk_size]
    print(chunk)
