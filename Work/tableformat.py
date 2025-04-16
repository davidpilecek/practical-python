#Exercise 4.5

class TableFormatter:
    def headings(self, headers):
        '''
        Emit table headings.
        '''
        raise NotImplementedError()
    
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()
    
class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        print("<tr>", end='')
        for h in headers:
            print(f'<th>{h}</th>', end='</tr>')
        print()

    def row(self, rowdata):
        print("<tr>", end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='</tr>')
        print()

def create_formatter(name):
    '''
    Create table formatter based on user-specified input.
    '''
    match name:
        case 'txt':
            formatter = TextTableFormatter()
        case 'csv':
            formatter = CSVTableFormatter()
        case 'html':
            formatter = HTMLTableFormatter()
        case _:
            raise RuntimeError(f'Format {name} not defined.')
    return formatter

def print_table(portfolio, attributes, formatter):
    '''
    Print table with specified attributes.
    '''
    formatter.headings(attributes)
    for row in portfolio:
        rowdata = [getattr(row, a) for a in attributes]
        formatter.row(rowdata)


    

