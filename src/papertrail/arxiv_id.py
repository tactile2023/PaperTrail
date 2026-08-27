import re



def normalize_arxiv_id(string):
    string = string.strip()

    if not string:
        raise ValueError("arXiv identifier cannot be empty")

    
    if string.startswith("https://arxiv.org/abs/"):
        string = string[len("https://arxiv.org/abs/"):]

    elif string.startswith("https://arxiv.org/html/"):
        string = string[len("https://arxiv.org/html/"):]

    elif string.startswith("https://arxiv.org/pdf/"):
        string = string[len("https://arxiv.org/pdf/"):]
        if string.endswith(".pdf"):
            string = string[:-4]

    modern_id_pattern = r"\d{4}\.\d{4,5}(v\d+)?"
    archive_id_pattern = r"[a-z-]+(\.[A-Z]{2})?/\d{7}(v\d+)?"

    #checking if valid id
    if not (re.fullmatch(modern_id_pattern, string) or re.fullmatch(archive_id_pattern, string)):
        raise ValueError("Invalid arXiv identifier")

    return string