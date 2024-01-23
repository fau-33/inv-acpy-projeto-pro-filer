import pytest
from pro_filer.actions.main_actions import show_disk_usage


@pytest.fixture
def tmp_context(tmp_path):
    file_paths = [
        tmp_path / "file1.txt",
        tmp_path / "file2.txt",
        tmp_path / "file3.txt",
    ]

    for file_path in file_paths:
        file_path.write_text("Test content")

    context = {"all_files": [str(file) for file in file_paths]}
    return context


def test_show_disk_usage(tmp_context, capsys):
    show_disk_usage(tmp_context)
    captured = capsys.readouterr()

    # Check if the output contains the expected information
    assert "'file3.txt':" in captured.out
    assert "Total size:" in captured.out


def test_show_disk_usage_empty(tmp_path, capsys):
    # Test when there are no files in the context
    context = {"all_files": []}
    show_disk_usage(context)
    captured = capsys.readouterr()

    assert "Total size: 0" in captured.out


def test_show_disk_usage_order(tmp_path, capsys):
    # Test if the files are listed in descending order of size
    file_paths = [
        tmp_path / "large_file.txt",
        tmp_path / "medium_file.txt",
        tmp_path / "small_file.txt",
    ]

    for i, file_path in enumerate(file_paths, start=3):
        file_path.write_text("x" * (i * 1000))

    context = {"all_files": [str(file) for file in file_paths]}
    show_disk_usage(context)
    captured = capsys.readouterr()

    # Check if the files are listed in descending order of size
    large_file_index = captured.out.find("large_file.txt")
    medium_file_index = captured.out.find("medium_file.txt")
    small_file_index = captured.out.find("small_file.txt")

    assert large_file_index < medium_file_index < small_file_index
