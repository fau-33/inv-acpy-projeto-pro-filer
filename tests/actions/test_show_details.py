import os
from pro_filer.actions.main_actions import show_details  # NOQA


data = [
    "File name: out.txt\n",
    "File size in bytes: 0\n",
    "File type: file\n",
    "File extension: .txt\n",
    "Last modified date: 2024-01-23\n"
    ]

data_for_file_without_extension = [
    "File name: without_extension\n",
    "File size in bytes: 0\n",
    "File type: file\n",
    "File extension: [no extension]\n",
    "Last modified date: 2024-01-23\n"
    ]


def test_show_details_works_correctly(tmp_path, capsys):
    output_path = tmp_path / "out.txt"
    context = {"base_path": str(output_path)}
    output_path.touch()
    returned = ''
    for i in data:
        returned += i

    show_details(context)
    out, err = capsys.readouterr()

    assert os.path.isfile(output_path)
    assert out == returned
    assert err == ""


def test_show_details_files_without_extension(tmp_path, capsys):
    output_path = tmp_path / "without_extension"
    context = {"base_path": str(output_path)}
    output_path.touch()
    returned = ''
    for i in data_for_file_without_extension:
        returned += i

    show_details(context)
    out, err = capsys.readouterr()

    assert os.path.isfile(output_path)
    assert out == returned
    assert err == ""


def test_show_details_validation_of_file_existance(capsys):
    context = {"base_path": 'batata.txt'}
    show_details(context)
    out, err = capsys.readouterr()
    assert out == "File 'batata.txt' does not exist\n"
    assert err == ""
