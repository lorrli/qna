import re

what_is_pattern = [r"what is (.*)",
                        r"what is the definition of (.*)",
                        r"define (.*)",
                        r"how do you define (.*)"
                        ]
what_is_response_pattern = "The definition of {} is {}"
what_is_type = "DEFINITION"

class Template:
    def __init__(self, pattern, response_pattern, lookup_type):
        self.pattern = pattern
        self.response_pattern = response_pattern
        self.lookup_type = lookup_type

def main():
    what_is_template = Template(what_is_pattern, what_is_response_pattern, what_is_type)

    base_str = "how do you define blob"
    capture_group = None 
    for pattern in what_is_template.pattern:
        used_pattern = re.compile(pattern)
        match = re.search(used_pattern, base_str)
        if match:
            capture_group = match.groups()
            print("found: ", re.search(used_pattern, base_str).group())
        else:
            print("noo")
    
    result = what_is_template.response_pattern.format(capture_group[0], capture_group[0])
    print(result)
    return result

if __name__ == "__main__":
    main()