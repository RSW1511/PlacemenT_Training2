def check_rotation(original, rotation):
    if len(original) != len(rotation):
        return False
    
    concatenated = original + original
    
    if rotation in concatenated:
        return True
    
    return False

if __name__ == "__main__":
    input_str = input("Please enter original String: ")
    rotation_str = input("Please enter rotation of String: ")
    
    if check_rotation(input_str, rotation_str):
        print(input_str + " and " + rotation_str + " are rotation of each other")
    else:
        print("Sorry, they are not rotation of another")
