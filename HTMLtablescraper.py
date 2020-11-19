#HTML table scraper, return list
				table_locator = <find element with xpath table locator>
        data_table = find_element(table_locator).get_attribute('innerHTML').replace('<th></th>', '')
        soup = BeautifulSoup(data_table, 'lxml')
        data_rows = soup.find_all('tr')
        rows_values_scrap = [[td.getText() for td in data_rows[i].findAll('td')]
                       for i, v in enumerate(data_rows)]
        rows_values = [x for x in rows_values_scrap if x]
        columns_scrap = [[td.getText() for td in data_rows[i].findAll('th')]
                       for i, v in enumerate(data_rows)]
        columns = [x for x in columns_scrap if x]
        if columns[1:] != []:
            for i, r in enumerate(columns[1:]):
                table=[f'column: {columns[0][j]}, row_title: {columns[1:][i][0]}, cell: {rows_values[i][j]}' for j, c in enumerate(columns[0])]
        else:
            table=[f'column: {columns[0][j]}, cell: {rows_values[0][j]}' for j, c in enumerate(columns[0]) if columns[1:] == []]
        table.insert(0, f'title: {self.find_visible_element(title_locator).text}')
        return table
