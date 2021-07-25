from sdg.open_sdg import open_sdg_build

def alter_data(df):
    def row_matches_ref_area(row):
        return row['REF_AREA'] == 'VN'

    df = df.copy()
    mask = df.apply(row_matches_ref_area, axis=1)
    return df[mask]

open_sdg_build(config='config.yml', alter_data=alter_data)
