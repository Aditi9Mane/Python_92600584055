def multi_func(a : int, b: int, fname, lname): #**kwargs
    total = a+b
    diff = a-b
    clean_name = fname.strip().lower() + lname.strip().lower()
    email = clean_name + "@gmail.com"
    print(total)
    print(diff)
    print(email)

multi_func(69, 45, "Max   ", "    Verstappen     ")


