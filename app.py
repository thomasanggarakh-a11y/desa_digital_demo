def login(username, password):
  # Simulasi login warga desa
  if username == "admin" and password == 12345: # Hardcoded password!
    print("Welcome, Admin!")
  else:
    print("Access Denied")

login("admin", 12345)
