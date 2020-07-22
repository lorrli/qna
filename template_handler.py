import re

what_is_pattern = [r"what is (.*)",
                    r"what is the definition of (.*)",
                    r"define (.*)",
                    r"how do you define (.*)"
                    ]
what_is_response_pattern = "The definition of {} is {}"
what_is_type = "DEFINITION"

attribute_lookup_pattern = [r"what is (.*) of (.*)",
                            ]
attribute_lookup_response_pattern = "The {} of {} is {}"
attribute_lookup_type = "ATTRIBUTE_LOOKUP"

class Template:
    def __init__(self, pattern, response_pattern, lookup_type):
        self.pattern = pattern
        self.response_pattern = response_pattern
        self.lookup_type = lookup_type

def main():
    what_is_template = Template(what_is_pattern, what_is_response_pattern, what_is_type)
    attribute_lookup_template = Template(attribute_lookup_pattern, attribute_lookup_response_pattern, attribute_lookup_type)
    templates = [what_is_template, attribute_lookup_template]

    base_str = "how do you define blob"
    response_pattern = None
    capture_group = None 
    for template in templates:
        for pattern in template.pattern:
            used_pattern = re.compile(pattern)
            match = re.search(used_pattern, base_str)
            if match:
                capture_group = match.groups()
                response_pattern = template.response_pattern
                # fetch data
                result = response_pattern.format(capture_group[0], capture_group[0])
                print(result)
                return result
            else:
                print("did not find any matches")
    
    if (response_pattern == None):
        return None

if __name__ == "__main__":
    main()
