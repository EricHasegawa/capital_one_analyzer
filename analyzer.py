import os
def analyze(filename, single_identifier="", multi_identifier=""):
    """ Given a file, return a list containing the total number of lines, total
        number of comments, number of multi-line comments, number of single-line comments,
        number of TODOs, and number of actual lines of code.

        Note that if the file is not one of the following types, the comment identifiers must 
        be manually passed in. [Python, Javascript, Java, C++, C#, C, HTML, CSS]

    Parameters:
    filename (str): The name of the file, including the path to it from the program.
    single_identifier [optional] (str): The character identifying a single line comment.
    multi_identifier [optional] (str): The character identifying a multi line comment.

    Returns:
    Dict[str->int]: Dictionary in which keys are labels to the counted statistic, and values are 
                    the actual count.

    """
    if filename[0] == ".":
        return "Please don't pass in hidden files that start with .'"

    # get comment identifiers
    if single_identifier == "" or multi_identifier == "":
        file_extension = os.path.splitext(filename)[1]
        if file_extension == "":
            return "Files passed in must have an extension."
        if get_identifiers(file_extension) == -1:
            return "Invalid file type, please pass in comment idenfiers manually"
        else:
            single_identifier = get_identifiers(file_extension)[0]
            multi_identifier = get_identifiers(file_extension)[1]
    
    # initialize counts and open file
    f = open(filename, "r")
    num_comments = 0
    num_singles = 0
    num_multis = 0
    num_todos = 0
    num_lines = 0
    lines = f.readlines()

    # calculate values
    for line in lines:
        if single_identifier in line:
            num_singles += 1
        if multi_identifier in line:
            num_multis += 1
        if "TODO" in line:
            num_todos += 1
        num_lines += 1
    
    if single_identifier == multi_identifier:
        num_singles = num_multis
        num_comments = num_singles
    else:
        num_comments = num_singles + num_multis
    print("Total # of lines: ", num_lines)
    print("Total # of comment lines: ", num_comments)
    print("Total # of single line comments: ", num_singles)
    print("Total # of comment lines within block comments: ", num_multis)
    print("Total # of block line comments: ", num_multis)
    print("Total # of TODO's: ", num_todos)

def get_identifiers(filetype):
    """Return the characters that identify comments in the given filetype.
       Helper method for analyze().
    
    Parameters:
    filetype (str): the extension of the passed file.

    Returns:
    List[str, str]: List containing the single line identifier, and multi-line identifier.
    """
    if filetype == ".py":
        single_identifier = "#"
        multi_identifier = "\"\"\"" 
    elif filetype == ".js" or filetype == ".java" or filetype == ".cpp" \
         or filetype == ".cs" or filetype == ".c":
        single_identifier = "//"
        multi_identifier = "/*"
    elif filetype == ".css":
        single_identifier = "/*"
        multi_identifier = "/*"
    elif filetype == ".html":
        single_identifier = "<!--"
        multi_identifier = "<!--"
    else:
        return -1
    return [single_identifier, multi_identifier]

print("HTML Test:")
analyze("html_test1.html")

print("C Test:")
analyze("c_test1.c")

print("CPP Test:")
analyze("cpp_test1.cpp")

print("CS Test:")
analyze("cs_test1.cs")

print("CSS Test:")
analyze("css_test1.css")

print("Java Test:")
analyze("java_test1.java")

print("Javascript Test:")
analyze("javascript_test1.js")

print("Python Test:")
analyze("python_test1.py")
print("TESTS FINISHED")