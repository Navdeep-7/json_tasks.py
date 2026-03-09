import json

print("------ TASK 1 : Build JSON Structure ------")

user_profile = {
    "name": "Alex",
    "age": 25,
    "email": "alex@example.com",
    "is_active": True,
    "skills": ["Python", "NumPy", "Pandas"]
}

json_data = json.dumps(user_profile, indent=4)

print(json_data)


print("\n------ TASK 2 : Parse API Response ------")

api_response = '{"status": "success", "data": {"user_id": 101, "username": "alex99", "score": 87.5}}'

data = json.loads(api_response)

username = data["data"]["username"]
score = data["data"]["score"]

print("Username:", username)
print("Score:", score)
print("User", username, "scored", score, "points")


print("\n------ TASK 3 : Handle Nested JSON ------")

nested_json = '''
{
  "name": "Priya",
  "address": {
    "city": "Bengaluru",
    "state": "Karnataka",
    "zip": "560001"
  }
}
'''

data2 = json.loads(nested_json)

city = data2["address"]["city"]
zip_code = data2["address"]["zip"]

print("City:", city)
print("Zip Code:", zip_code)

data2["address"]["country"] = "India"

print("\nUpdated JSON:")
print(json.dumps(data2, indent=4))