import httpx

url = "https://didactic-eureka-r56677xg5gxhw7q-5000.app.github.dev/"  

authData = {
   "id": "felipe.montero@uconn.edu",
   "token": "3c44fa6d9bc869945c373879aea756de8aba0937d581970b61bdc78f1100f2a7"
}


response = httpx.post(url + "login", data=authData)

# Print the response
print(response.status_code)
print(response.text)

