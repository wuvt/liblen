import xlrd


def parse_stack(path):
    releases = []
    book = xlrd.open_workbook(path)
    for s in range(book.nsheets):
        sheet = book.sheet_by_index(s)
        # skip first row since it has the headings
        for r in range(1, sheet.nrows):
            row = sheet.row(r)

            year = row[3].value
            if type(year) == float:
                year = int(year)
            elif type(year) != int:
                year = None

            releases.append({
                'artist': str(row[0].value).strip(),
                'title': str(row[1].value).strip(),
                'label': str(row[2].value).strip(),
                'year': year,
                'genres': [genre.strip() for genre in
                           str(row[4].value).split('/')],
                'stack': str(row[5].value).strip(),
            })

    return releases
