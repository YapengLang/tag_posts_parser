from tpp import __main__ as tpp


_feeds = [
    {
        "folders": ["hw1"],
        "log": [{"t": "2025-08-6T17:00:00Z", "u": "1"}],
    },
    {
        "folders": ["hw1"],
        "log": [{"t": "2025-08-11T17:00:00Z", "u": "2"}],
    },
    {
        "folders": ["hw2"],
        "log": [{"t": "2025-08-12T17:00:00Z", "u": "1"}],
    },
    {
        "folders": ["hw2"],
        "log": [{"t": "2025-08-20T17:00:00Z", "u": "2"}],
    },
]

_folders = {
    "hw1": [
        {"t": "2025-08-6T17:00:00Z", "u": "1"},
        {"t": "2025-08-11T17:00:00Z", "u": "2"},
    ],
    "hw2": [
        {"t": "2025-08-12T17:00:00Z", "u": "1"},
        {"t": "2025-08-20T17:00:00Z", "u": "2"},
    ],
}

_cutoff = {
    "hw1": tpp._format_timestamp("2025-8-15-0"),
    "hw2": tpp._format_timestamp("2025-8-15-0"),
}


def test_id_to_email():
    all_users = [
        {"id": "1", "email": "uxxx@edu.au", "role": "student"},
        {"id": "2", "email": "foo@edu.au", "role": "ta"},
    ]
    result = tpp._id_to_email(all_users)
    assert len(result) == 1
    assert result["1"] == "uxxx@edu.au"


def test_format_timestamp():
    date_str = "2025-8-10-17"
    result = tpp._format_timestamp(date_str)
    assert str(result) == "2025-08-10 17:00:00"


def test_format_timestamp_mal():
    date_str = "2025-08-10-7"
    result = tpp._format_timestamp(date_str)
    assert str(result) == "2025-08-10 07:00:00"


def test_sort_feeds():
    result = tpp._sort_feeds(_feeds)
    assert len(result) == 2
    assert len(result["hw1"]) == 2
    assert len(result["hw2"]) == 2


def test_count_activities():
    deadline = tpp._format_timestamp("2025-8-15-0")
    result1 = tpp._count_activities(_folders["hw1"], deadline)
    assert len(result1) == 2
    assert result1["1"] == 1
    assert result1["2"] == 1

    result2 = tpp._count_activities(_folders["hw2"], deadline)
    assert len(result2) == 1
    assert result2["1"] == 1


def test_summarise_feeds():
    result = tpp._summarise_feeds(
        _folders, {"1": "uxxx@edu.au", "2": "foo@edu.au"}, _cutoff
    )
    assert len(result) == 2
    assert result["1"]["email"] == "uxxx@edu.au"
    assert result["1"]["hw1"] == 1
    assert result["1"]["hw2"] == 1
    assert result["2"]["email"] == "foo@edu.au"
    assert result["2"]["hw1"] == 1
    assert result["2"]["hw2"] == 0
