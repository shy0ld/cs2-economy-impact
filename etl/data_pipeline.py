import json
import pandas as pd
from sqlalchemy import create_engine
from functools import reduce

def parse_steam_item(file_path, prefix):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # витягуємо ціни і робимо датафрейм
    df = pd.DataFrame(data['prices'], columns=['Date', f'{prefix}_price', f'{prefix}_vol'])
    
    # прибираємо час з дати (залишаємо перші 11 символів типу 'Nov 29 2013')
    df['Date'] = pd.to_datetime(df['Date'].str[:11]).dt.normalize()
    
    df[f'{prefix}_price'] = df[f'{prefix}_price'].astype(float)
    df[f'{prefix}_vol'] = df[f'{prefix}_vol'].astype(int)

    # групуємо по днях на випадок дублів від стіма
    return df.groupby('Date', as_index=False).agg({
        f'{prefix}_price': 'mean', 
        f'{prefix}_vol': 'sum'
    })

def parse_butterfly(file_path):
    # у метелика інша структура json, тому окрема функція
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    
    # чистимо таймзони, щоб нормально змерджити
    df['Date'] = pd.to_datetime(df['day']).dt.normalize().dt.tz_localize(None)
    
    # ціна в центах, перевод в доллари
    df['butterfly_price'] = df['avg_price'] / 100.0
    df['butterfly_vol'] = df['count'].astype(int)

    return df[['Date', 'butterfly_price', 'butterfly_vol']]

def process_players(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['DateTime']).dt.normalize()
    
    # середній онлайн за день
    df_daily = df.groupby('Date', as_index=False)['Players'].mean()
    # округлюємо людей і ставимо Int64 щоб не падало через порожні значення (NaN)
    df_daily['Players'] = df_daily['Players'].round().astype('Int64')
    
    return df_daily

def main():
    print("Start processing...")

    # список файлів для парсингу
    items = {
        'm4a1': 'm4a1_cyrex.json',
        'p90': 'p90_asiimov.json',
        'case': 'breakout_case.json',
        'key': 'breakout_key.json',
        'm9': 'm9.json',
        'headshot': 'ak47_hs.json',
        'printstream': 'm4a1s_ps.json'
    }
    
    dataframes = [parse_steam_item(path, prefix) for prefix, path in items.items()]

    # додаємо метелика і онлайн
    dataframes.append(parse_butterfly('butterfly.json'))
    dataframes.append(process_players('steamdb_chart_730.csv'))

    print("Merging data...")
    # зліплюємо всі таблиці в одну по даті
    df_master = reduce(lambda left, right: pd.merge(left, right, on='Date', how='outer'), dataframes)
    df_master = df_master.sort_values('Date').reset_index(drop=True)

    # робимо всі колонки маленькими літерами для постгреса
    df_master.columns = df_master.columns.str.lower()

    # зберігання в csv для табло
    df_master.to_csv('cs2_final_dataset.csv', index=False)
    print("CSV saved.")

    # залиття в базу
    try:
        engine = create_engine('postgresql://postgres@localhost:5432/cs2_economy')
        df_master.to_sql('market_data', engine, if_exists='replace', index=False)
        print("DB updated.")
    except Exception as e:
        print(f"DB connection error: {e}")

if __name__ == '__main__':
    main()