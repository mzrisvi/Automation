# This is for simple string manipulation functions
def main():
    sample_string = "  Hello, World!  "
    
    # Strip whitespace
    stripped = sample_string.strip()
    print(f"Stripped: '{stripped}'")
    
    # Convert to uppercase
    uppercased = stripped.upper()
    print(f"Uppercased: '{uppercased}'")
    
    # Replace comma with exclamation mark
    replaced = uppercased.replace(",", "!")
    print(f"Replaced: '{replaced}'")
    
    # Split into words
    words = replaced.split()
    print(f"Words: {words}")

    # String length
    length = len(replaced)
    print(f"Length: {length}")
    
    for x in "Hello":
        print(x)
    string1 = "Mohamnmad"
    string2 = "Risvi"
    print('My name is : ' + string1 + " " + string2)
main()