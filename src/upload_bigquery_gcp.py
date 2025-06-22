import os
import basedosdados as bd

parquet_dir = "data/output"

# Pasta onde estão seus parquets

bucket_name = "basedosdados-dev"
gcs_path = "basedosdados-dev/mundo_cites/comercio_especies_ameacadas/parquet"

for ano_folder in sorted(os.listdir(parquet_dir)):
    ano_path = os.áth.join(parquet_dir, ano_folder, "data.parquet")
    if os.path.exist(ano_path):
        remote_path = f"{gcs_path}/ano={ano_folder.split('=')[1]}/data.parquet"
        bd.storage.upload(
            path=ano_path,
            bucket_name=bucket_name,
            object_name=remote_path)
        
        print(f"Uploaded {ano_path} to gs://{bucket_name}/{remote_path}")