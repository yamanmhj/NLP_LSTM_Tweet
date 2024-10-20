import os


class GET_Data_From_GLOUD:

    def sync_folder_to_gcloud(gcp_bucket_url, filepath, filename) -> None:
        command = f"gsutil cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        # command = f"gcloud storage cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        os.system(command)

    def sync_folder_from_gcloud(gcp_bucket_url, filename, destination) -> None:
     

        command = f"gsutil cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
        # command = f"gcloud storage cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
        os.system(command)