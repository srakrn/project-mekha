from mekha import logger


def test_logger(capsys):
    l = logger.Logger("test-logger")
    l.log("test-message")
    captured = capsys.readouterr()
    assert captured.out == "test-logger: test-message\n"
