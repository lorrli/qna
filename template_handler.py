import re

class Template:
    def __init__(self, response_pattern, lookup_type):
        self.pattern = [r"what is (.*)",
                        r"what is the definition of (.*)",
                        r"define (.*)",
                        r"how do you define (.*)"
                        ]
        self.response_pattern = response_pattern
        self.lookup_type = lookup_type


def main():
    temp1 = Template("what is this", "type")
    print(temp1.pattern)

    base_str = "how do you define blob"
    for pattern in temp1.pattern:
        used_pattern = re.compile(pattern)
        if re.search(used_pattern, base_str):
            print("found: ", re.search(used_pattern, base_str).group())
            print("YAY")
        else:
            print("noo")

if __name__ == "__main__":
    main()