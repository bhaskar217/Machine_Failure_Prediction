from huggingface_hub.utils import RepositoryNotFoundError
from huggingface_hub import HfApi, create_repo
import os

token = os.getenv("HF_TOKEN")
repo_id = "bhaskar217/machine-failure-prediction"
repo_type = "dataset"

api = HfApi(token=token)

try:
    api.repo_info(repo_id=repo_id, repo_type=repo_type)
    print(f"Dataset '{repo_id}' already exists. Using it.")
except RepositoryNotFoundError:
    print(f"Dataset '{repo_id}' not found. Creating...")
    create_repo(repo_id=repo_id, repo_type=repo_type, private=False, token=token)
    print(f"Dataset '{repo_id}' created.")

api.upload_folder(
    folder_path="week_2_mls/data",
    repo_id=repo_id,
    repo_type=repo_type,
)
