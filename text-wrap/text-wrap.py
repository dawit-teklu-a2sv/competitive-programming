import textwrap

def wrap(string, max_width):
    wraped_text = textwrap.wrap(string,max_width) # splits the string to equal length array elements
    return "\n".join(wraped_text)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
