import requests

print("<h1>Top Github users in Trinidad and Tobago based on follower count</h1>")

api_url = "https://api.github.com/search/users?q=location:trinidad-and-tobago+followers:%3E25"

response = requests.get(api_url)

users=response.json()

print("<table>")
print("<tr><th>username</th><th>name</th><th>no. of followers</th></tr>")

for user in users["items"]:
	print("<tr><td><a href='"+user["html_url"]+"'>"+user["login"]+"</a></td>")
	
	api_url = user["url"]
	
	user_detail = requests.get(api_url).json()
	
	print("<td>"+user_detail.get("name")+"</td>")
	print("<td>"+str(user_detail["followers"])+"</td></tr>")

print("</table>")
