from Introduction_Python.L7_Regular_Expressions.PS7.watch import parse

def test_long_www():
    assert parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == "https://www.youtu.be/xvFZjo5PgG0"

def test_long_notw():
    assert parse('<iframe width="560" height="315" src="https://youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == "https://youtu.be/xvFZjo5PgG0"

def test_short_www():
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://www.youtu.be/xvFZjo5PgG0"

def test_short_notw():
    assert parse('<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"