from .bot import Explorer


def test_create():
    """
    Test if the bot can be created
    """
    bot = Explorer(id=0, grid_size=(1, 1))
    assert bot is not None
