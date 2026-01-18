import sqlite3
import pandas as pd

def export_bgc_summary_with_rank0(db_path, output_csv):
    conn = sqlite3.connect(db_path)
    query = """
    SELECT 
        bgc.id AS bgc_id,
        bgc.name AS BGC,
        ROUND(bgc.length_nt / 1000.0, 2) AS "length (kb)",
        CASE 
            WHEN bgc.on_contig_edge = 0 THEN 'complete' 
            ELSE 'partial' 
        END AS completeness,
        gm.gcf_id AS "best hit",
        gm.membership_value AS distance
    FROM 
        bgc
    JOIN 
        gcf_membership AS gm 
        ON bgc.id = gm.bgc_id
    ORDER BY
        bgc.id;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    df.to_csv(output_csv, index=False)
    print(f"✅ Saved: {output_csv}")

db_path = "output_folder_2/reports/2/data.db"
output_csv = "output_folder/bigslice_rank0_summary.csv"
export_bgc_summary_with_rank0(db_path, output_csv)

