from pro_filer.actions.main_actions import show_preview  # NOQA


def test_not_found_files_and_dirs(capsys):
    context = {"all_files": [], "all_dirs": []}
    show_preview(context)
    out, err = capsys.readouterr()
    assert out == "Found 0 files and 0 directories\n"
    assert err == ""


def test_show_preview_works_correctly(capsys):
    context = {
        "all_files": ["src/__init__.py"],
        "all_dirs": ["src"]
    }
    show_preview(context)
    out, err = capsys.readouterr()
    message_1 = "Found 1 files and 1 directories\n"
    message_2 = "First 5 files: ['src/__init__.py']\n"
    message_3 = "First 5 directories: ['src']\n"
    assert out == f"{message_1}{message_2}{message_3}"
    assert err == ""


# @pytest.mark.xfail
def test_expect_show_preview_fail(capsys):
    context = {
        "all_files": ["src/__init__.py"],
        "all_dirs": ["src", "src/u", "src/w", "src/x", "src/y", "src/z"]
    }
    show_preview(context)
    out, err = capsys.readouterr()
    mess_1 = "Found 1 files and 6 directories"
    mess_2 = "First 5 files: ['src/__init__.py']"
    mess_3 = "First 5 directories: ['src', 'src/u', 'src/w', 'src/x', 'src/y']"
    assert out == f"{mess_1}\n{mess_2}\n{mess_3}\n"
    assert err == ""
