"""
Escriba el codigo que ejecute la accion solicitada.
"""

# pylint: disable=import-outside-toplevel



def clean_campaign_data():
    """
    En esta tarea se le pide que limpie los datos de una campaña de
    marketing realizada por un banco, la cual tiene como fin la
    recolección de datos de clientes para ofrecerls un préstamo.

    La información recolectada se encuentra en la carpeta
    files/input/ en varios archivos csv.zip comprimidos para ahorrar
    espacio en disco.

    Usted debe procesar directamente los archivos comprimidos (sin
    descomprimirlos). Se desea partir la data en tres archivos csv
    (sin comprimir): client.csv, campaign.csv y economics.csv.
    Cada archivo debe tener las columnas indicadas.

    Los tres archivos generados se almacenarán en la carpeta files/output/.

    client.csv:
    - client_id
    - age
    - job: se debe cambiar el "." por "" y el "-" por "_"
    - marital
    - education: se debe cambiar "." por "_" y "unknown" por pd.NA
    - credit_default: convertir a "yes" a 1 y cualquier otro valor a 0
    - mortage: convertir a "yes" a 1 y cualquier otro valor a 0

    campaign.csv:
    - client_id
    - number_contacts
    - contact_duration
    - previous_campaing_contacts
    - previous_outcome: cmabiar "success" por 1, y cualquier otro valor a 0
    - campaign_outcome: cambiar "yes" por 1 y cualquier otro valor a 0
    - last_contact_day: crear un valor con el formato "YYYY-MM-DD",
        combinando los campos "day" y "month" con el año 2022.

    economics.csv:
    - client_id
    - const_price_idx
    - eurobor_three_months



    """
    import glob
    import pandas as pd
    import os

    input_directory = 'files/input'

    files = glob.glob(f"{input_directory}/*")

    dfs = []

    for file in files:
        df = pd.read_csv(file)
        dfs.append(df)

    ds = pd.concat(dfs)
    ds  

    # Limpieza de datos
    ds['job'] = ds['job'].str.replace('.', '').str.replace('-','_')
    # education: se debe cambiar "." por "_" y "unknown" por pd.NA
    ds['education'] = ds['education'].str.replace('.', '_')
    ds['education'] = ds['education'].apply(lambda x: pd.NA if x == 'unknown' else x) 
    # credit_default: convertir a "yes" a 1 y cualquier otro valor a 0
    ds['credit_default'] = ds['credit_default'].apply(lambda x: 1 if x == 'yes' else 0)
    # mortage: convertir a "yes" a 1 y cualquier otro valor a 0
    ds['mortgage'] = ds['mortgage'].apply(lambda x: 1 if x == 'yes' else 0)
    # previous_outcome: cmabiar "success" por 1, y cualquier otro valor a 0
    ds['previous_outcome'] = ds['previous_outcome'].apply(lambda x: 1 if x == 'success' else 0)
    # campaign_outcome: cambiar "yes" por 1 y cualquier otro valor a 0
    ds['campaign_outcome'] = ds['campaign_outcome'].apply(lambda x: 1 if x == 'yes' else 0)

    # last_contact_day: crear un valor con el formato "YYYY-MM-DD",combinando los campos "day" y "month" con el año 2022.
    ds['month'] = pd.to_datetime(ds['month'], format = '%b').dt.month
    ds['last_contact_day'] = pd.to_datetime({'year':2022, 'month':ds['month'], 'day':ds['day']})

    client = ds[['client_id','age','job','marital','education','credit_default','mortgage']]
    campaign = ds[['client_id','number_contacts','contact_duration','previous_campaign_contacts','previous_outcome','campaign_outcome','last_contact_day']]
    economics = ds[['client_id','const_price_idx','eurobor_three_months']]

    os.makedirs('files/output/', exist_ok=True)

    output_directory = 'files/output/'
    dataframes = {'client':client,
                'campaign': campaign,
                'economics': economics
                }

    for name, df in dataframes.items():
        df.to_csv(f'{output_directory}{name}.csv', index=False)

    return print("Aca termina la limpieza")


if __name__ == "__main__":
    clean_campaign_data()
