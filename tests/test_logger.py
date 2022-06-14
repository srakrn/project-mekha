import os
import tempfile

from mekha import logger


def test_logger_single_logging(capsys):
    l = logger.Logger("test-logger")
    l.log("test-message")
    captured = capsys.readouterr()
    assert captured.out == "test-logger: test-message\n"


def test_logger_multi_logging(capsys):
    l = logger.Logger("test-logger")
    l.log("test-message-1")
    l.log("test-message-2")
    l.log("test-message-3")
    captured = capsys.readouterr()
    assert (
        captured.out == "test-logger: test-message-1\n"
        "test-logger: test-message-2\n"
        "test-logger: test-message-3\n"
    )


def test_file_logger_single_logging():
    log_file_name = "test_logger"
    with tempfile.TemporaryDirectory() as temp_directory:
        log_path = os.path.join(temp_directory, log_file_name)
        fl = logger.FileLogger(log_path)
        fl.log("test-message-1")

        with open(log_path, encoding="utf-8") as f:
            log_contents = f.read()
            assert log_contents == "test-message-1\n"


def test_file_logger_multi_logging():
    log_file_name = "test_logger"
    with tempfile.TemporaryDirectory() as temp_directory:
        log_path = os.path.join(temp_directory, log_file_name)
        fl = logger.FileLogger(log_path)
        fl.log("test-message-1")
        fl.log("test-message-2")
        fl.log("test-message-3")

        with open(log_path, encoding="utf-8") as f:
            log_contents = f.read()
            assert (
                log_contents == "test-message-1\n" "test-message-2\n" "test-message-3\n"
            )
