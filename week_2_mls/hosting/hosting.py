from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path="/content/drive/My Drive/Colab Notebooks/Course 10 Advanced AI & ML Ops/Week 2/week_2_mls/deployment",     # the local folder containing your files
    repo_id="bhaskar217/Machine-Failure-Prediction",          # the target repo
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
