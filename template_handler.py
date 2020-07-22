import re, string

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

    base_str = "what is an the dog??????????????"
    stripped_str = re.sub(r'\s+\ban\b|\bthe\b|\band\b|\ba\b\s+', '', base_str)
    final_str = stripped_str.translate(str.maketrans('', '', string.punctuation))

    capture_group = None
    for pattern in what_is_template.pattern:
        used_pattern = re.compile(pattern)
        match = re.search(used_pattern, final_str)
        if match:
            capture_group = match.groups()
            print("found: ", re.search(used_pattern, final_str).group())
        else:
            print("did not find any matches")
    if capture_group:
        result = what_is_template.response_pattern.format(capture_group[0], capture_group[0])
        print(result)
    else:
        result = None
    return result

if __name__ == "__main__":
    main()
