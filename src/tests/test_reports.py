from tabulate import tabulate

from app.reports import report_average_price, report_average_rating


data = [
    ["name", "brand", "price", "rating"],
    ["iphone 15 pro", "apple", "999", "4.9"],
    ["galaxy s23 ultra", "samsung", "1199", "4.8"],
    ["redmi note 12", "xiaomi", "199", "4.6"],
    ["iphone 14", "apple", "799", "4.7"],
    ["galaxy a54", "samsung", "349", "4.2"],
    ["poco x5 pro", "xiaomi", "299", "4.4"],
    ["iphone se", "apple", "429", "4.1"],
    ["galaxy z flip 5", "samsung", "999", "4.6"],
    ["redmi 10c", "xiaomi", "149", "4.1"],
    ["iphone 13 mini", "apple", "599", "4.5"],
]


def test_report_average_rating():
    mock_data = [
        ["", "brand", "rating"],
        ["1", "apple", "4.55"],
        ["2", "samsung", "4.53"],
        ["3", "xiaomi", "4.37"],
    ]
    mock_table = tabulate(
        mock_data[1:],
        headers=mock_data[0],
        tablefmt="psql",
        floatfmt=".2f",
    )

    assert mock_table == report_average_rating(data)


def test_report_average_price():
    mock_data = [
        ["", "brand", "price"],
        ["1", "samsung", "849.00"],
        ["2", "apple", "706.50"],
        ["3", "xiaomi", "215.67"],
    ]
    mock_table = tabulate(
        mock_data[1:],
        headers=mock_data[0],
        tablefmt="psql",
        floatfmt=".2f",
    )

    assert mock_table == report_average_price(data)
