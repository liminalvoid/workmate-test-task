import pytest

from app.main import main


def test_file_reading():
    with pytest.raises(FileNotFoundError, match="No such file or directory"):
        main()
