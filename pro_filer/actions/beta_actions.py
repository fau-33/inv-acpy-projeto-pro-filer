def contar_barra(path):
    barra = '/'
    return sum(1 for char in path if char == barra)


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        deepest_file = max(context["all_files"], key=contar_barra)
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]
        if not case_sensitive and search_term.lower() in file_name.lower():
            found_files.append(path)
        elif case_sensitive and search_term in file_name:
            found_files.append(path)

    return found_files


x = {
    "all_files": [
            "/path/to/file.sql",
            "/path/to/file.txt",
            "/path/to/file2.txt",
            "/path/to/FILE.txt",
            "/path/to/FILE2.TXT",
            "/path/to/something.txt",
            "/path-to/file.txt",
        ]
}
print(find_file_by_name(x, 'file', case_sensitive=False))
