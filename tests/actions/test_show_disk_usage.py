import pytest
from pro_filer.actions.main_actions import show_disk_usage


@pytest.fixture
def tmp_context(tmp_path):
    file_paths = [
        tmp_path / "large_file.txt",
        tmp_path / "medium_file.txt",
        tmp_path / "small_file.txt",
    ]

    for i, file_path in enumerate(file_paths, start=3):
        file_path.write_text("x" * (i * 1000))

    context = {"all_files": [str(file) for file in file_paths]}
    return context


def test_show_disk_usage_order(tmp_context, capsys):
    show_disk_usage(tmp_context)
    captured = capsys.readouterr()

    # Check if the files are listed in descending order of size
    large_file_index = captured.out.find("large_file.txt")
    medium_file_index = captured.out.find("medium_file.txt")
    small_file_index = captured.out.find("small_file.txt")

    assert large_file_index > medium_file_index > small_file_index

    # Additional check: Check if the total size is correct
    total_size_index = captured.out.find("Total size:")
    assert total_size_index != -1

    # Extract and parse the total size from the output
    total_size_str = captured.out[
        total_size_index + len("Total size:"):
    ].strip()
    total_size = int(total_size_str)

    # Calculate the expected total size based on the file sizes in tmp_context
    expected_total_size = sum((i * 1000) for i in range(3, 6))

    # Assert that the calculated total size matches the expected total size
    assert total_size == expected_total_size
