# Useful Pandas Snippets

## Data Types and Conversion (Типи даних та перетворення)
Convert Series datatype to numeric (will error if column has non-numeric values)
Перетворити тип даних Series у числовий (викличе помилку, якщо стовпець містить нечислові)
```
pd.to_numeric(df['Column Name'])
```

Convert Series datatype to numeric, changing non-numeric values to NaN
Перетворити тип даних Series у числовий, замінюючи нечислові значення на NaN
```
pd.to_numeric(df['Column Name'], errors='coerce')
```

Change data type of DataFrame column
Змінити тип даних стовпця DataFrame
```
df.column_name = df.column_name.astype(np.int64)
```


## Exploring and Finding Data

Get a report of all duplicate records in a DataFrame, based on specific columns
Отримати звіт про всі дублікати записів у DataFrame на основі конкретних колонок
```
dupes = df[df.duplicated(['col1', 'col2', 'col3'], keep=False)]
```
List unique values in a DataFrame column
Отримати унікальні значення в колонці DataFrame
```
df['Column Name'].unique()
```
For each unique value in a DataFrame column, get a frequency count
Для кожного унікального значення в колонці DataFrame отримати частоту з якою це значення зустрічається у виборці
```
df['Column Name'].value_counts()
```
Grab DataFrame rows where column = a specific value
Вибрати рядки DataFrame, де значення колонки дорівнює певному значенню
```
df = df.loc[df.column == 'somevalue']
```
Grab DataFrame rows where column value is present in a list
Фільтрація DataFrame за значеннями зі списку 
```
test_data = {'hi': 'yo', 'bye': 'later'}
df = pd.DataFrame(list(test_data.items()), columns=['col1', 'col2'])
valuelist = ['yo', 'heya']
result = df[df['col2'].isin(valuelist)]
print(result)
```
Grab DataFrame rows where column value is not present in a list
```
mask = ~df['col2'].isin(valuelist)  # булева маска: позначає True для тих рядків, де значення ВІДСУТНЄ у списку
df_filtered = df.loc[mask] # вибирає рядки, для яких значення маски True
```
Select from DataFrame using criteria from multiple columns (use | instead of & to do an OR)
Вибір рядків DataFrame за умовами з кількох колонок (використовуй | замість &, щоб зробити OR)
```
newdf = df[(df['column_one']>2004) & (df['column_two']==9)]
```
Loop through rows in a DataFrame (if you must)
Прохід по рядках DataFrame (якщо вже дуже потрібно-повільно, може змінити ттип даних)
```
for index, row in df.iterrows():
    print (index, row['some column'])
```
Much faster way to loop through DataFrame rows if you can work with tuples
Значно швидший спосіб проходу по рядках, якщо можна працювати з кортежами (швидше за список, збереже тип даних, але не можна змінити цей кортеж)
```
for row in df.itertuples():
    print(row)
```
Get top n for each group of columns in a sorted DataFrame(make sure DataFrame is sorted first)
Отримати топ-N рядків для кожної групи колонок у відсортованому DataFrame(переконайся, що DataFrame відсортований заздалегідь)
```
top5 = df.groupby(['groupingcol1', 'groupingcol2']).head(5)
```
Grab DataFrame rows where specific column is null/notnull
Вибрати рядки DataFrame, де конкретна колонка має null / не має null
```
newdf = df[df['column'].isnull()]
```
Select from DataFrame using multiple keys of a hierarchical index
Вибір з DataFrame за кількома ключами ієрархічного індексу
```
df.xs(('index level 1 value','index level 2 value'), level=('level 1','level 2'))
```
Slice values in a DataFrame column (aka Series)
Зріз значень у колонці DataFrame (Series)
```
df.column.str[0:2]
```
Get quick count of rows in a DataFrame
Швидко отримати кількість рядків у DataFrame
```
len(df.index)
```
Get length of data in a DataFrame column
Отримати довжину значень у колонці DataFrame
```
df.column_name.str.len()
```


## Updating and Cleaning Data - Оновлення та очищення даних у pandas

Delete column from DataFrame
Видалення колонки з DataFrame
```
del df['column']
```
Rename several DataFrame columns
Перейменування кількох колонок
```
df = df.rename(columns = {
    'col1 old name':'col1 new name',
    'col2 old name':'col2 new name',
    'col3 old name':'col3 new name',
})
```
Lower-case all DataFrame column names
Зробити всі назви колонок нижнім регістром
```
df.columns = map(str.lower, df.columns)
```
Even more fancy DataFrame column re-naming
lower-case all DataFrame column names (for example)
«Просунуте» перейменування колонок
```
df.rename(columns=lambda x: x.split('.')[-1], inplace=True)
```
Lower-case everything in a DataFrame column
Зробити всі значення колонки нижнім регістром
```
df.column_name = df.column_name.str.lower()
```
Sort DataFrame by multiple columns
Сортування DataFrame за кількома колонками
```
df = df.sort_values(['col1','col2','col3'], ascending=[1,1,0])
```
Change all NaNs to None (useful before loading to a db)
Заміна NaN на None (перед записом у БД)
```
df = df.where((pd.notnull(df)), None)
```
More pre-db insert cleanup...make a pass through the DataFrame, stripping whitespace from strings and changing any empty values to None
(not especially recommended but including here b/c I had to do this in real life once)
Очищення перед вставкою в БД (НЕ рекомендовано)
```
df = df.applymap(lambda x: str(x).strip() if len(str(x).strip()) else None)
```
Get rid of non-numeric values throughout a DataFrame:
Видалення нечислових символів у всьому DataFrame
```
for col in refunds.columns.values:
  refunds[col] = refunds[col].replace('[^0-9]+.-', '', regex=True)
```
Set DataFrame column values based on other column values
Умовне оновлення значень колонки

```
df.loc[(df['column1'] == some_value) & (df['column2'] == some_other_value), ['column_to_change']] = new_value
```
Clean up missing values in multiple DataFrame columns
Очищення пропусків у кількох колонках
```
df = df.fillna({
    'col1': 'missing',
    'col2': '99.999',
    'col3': '999',
    'col4': 'missing',
    'col5': 'missing',
    'col6': '99'
})
```
Doing calculations with DataFrame columns that have missing values. In example below, swap in 0 for df['col1'] cells that contain null.
Обчислення з урахуванням пропусків
```
df['new_col'] = np.where(pd.isnull(df['col1']), 0, df['col1']) + df['col2']
```
Split delimited values in a DataFrame column into two new columns
Розбиття значень колонки на дві нові
```
df['new_col1'], df['new_col2'] = zip(*df['original_col'].apply(lambda x: x.split(': ', 1)))
```
Collapse hierarchical column indexes
Прибрати багаторівневі (hierarchical) колонки
```
df.columns = df.columns.get_level_values(0)
```
## Reshaping, Concatenating, and Merging Data - Перетворення, об’єднання та злиття даних

Pivot data (with flexibility about what what becomes a column and what stays a row).
(зведена таблиця)
```
pd.pivot_table(
  df,values='cell_value',
  index=['col1', 'col2', 'col3'],               #these stay as columns; will fail silently if any of these cols have null values
  columns=['col4'])                             #data values in this column become their own column

```
Concatenate two DataFrame columns into a new, single column
(useful when dealing with composite keys, for example)
Обʼєднання двох колонок в одну

```
df['newcol'] = df['col1'].astype(str) + df['col2'].astype(str)
```
## Display and formatting - Відображення та форматування
Set up formatting so larger numbers aren't displayed in scientific notation
Вимкнути наукову нотацію (відключити 12е+06)
```
pd.set_option('display.float_format', lambda x: '%.3f' % x)
```
To display with commas and no decimals
Відображення з комами без дробів (1,234,567)
```
pd.options.display.float_format = '{:,.0f}'.format
```
## Creating DataFrames - Створення датафреймів
Create a DataFrame from a Python dictionary
Зі словника Python
```
df = pd.DataFrame(list(a_dictionary.items()), columns = ['column1', 'column2'])
```
Convert Django queryset to DataFrame
```
qs = DjangoModelName.objects.all()
q = qs.values()
df = pd.DataFrame.from_records(q)
```
Creating Series
Create a new series using an index from an existing series
Нова Series з індексом старої
```
# original_series = the original series
# simplisitically generate a list of values to use in the new series
new_series_values = list(range(1, len(original_series) + 1))
new_series = pd.Series(new_series_values, index=original_series.index)
```
