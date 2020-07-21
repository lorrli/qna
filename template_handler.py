import re


class Template:
    def __init__(self, pattern, response_pattern, lookup_type):
        self.pattern = pattern
        self.response_pattern = response_pattern
        self.lookup_type = lookup_type


def main():
    what_is_pattern = [r"what is (.*)",
                       r"what is the definition of (.*)",
                       r"define (.*)",
                       r"how do you define (.*)"]
    temp1 = Template(what_is_pattern, "what is this", "type")
    base_str = "how do you define blob"
    for pattern in temp1.pattern:
        used_pattern = re.compile(pattern)
        if re.search(used_pattern, base_str):
            print("found: ", re.search(used_pattern, base_str).group())
            return re.search(used_pattern, base_str).group()
        else:
            print("did not find any matches")


if __name__ == "__main__":
    main()
