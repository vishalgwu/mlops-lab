from pathlib import Path


PROJECT_NAME = "mlops-learning-roadmap"

folders = [
    ".github/workflows",
    "config",
    "data/raw",
    "data/processed",
    "data/external",
    "artifacts",
    "notebooks",
    "src/components",
    "src/pipeline",
    "src/utils",
    "tests",
    "models",
    "logs",
    "monitoring/grafana",
    "deployment/kubernetes",
    "deployment/aws",
    "scripts",
]

files = [
    "README.md",
    ".gitignore",
    "requirements.txt",
    "setup.py",
    "pyproject.toml",
    "Dockerfile",
    "docker-compose.yml",
    "dvc.yaml",
    "params.yaml",

    ".github/workflows/ci.yml",

    "config/config.yaml",

    "notebooks/01_experimentation.ipynb",

    "src/__init__.py",

    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_validation.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",

    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",

    "src/utils/__init__.py",
    "src/utils/common.py",

    "src/logger.py",
    "src/exception.py",

    "tests/__init__.py",
    "tests/test_data.py",
    "tests/test_model.py",

    "scripts/train.py",
    "scripts/predict.py",

    "deployment/kubernetes/deployment.yaml",
    "deployment/kubernetes/service.yaml",

    "monitoring/grafana/README.md",

    "app.py",
]


def create_project_structure():
    root = Path(PROJECT_NAME)

    # Create root project directory
    root.mkdir(exist_ok=True)

    # Create folders
    for folder in folders:
        folder_path = root / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {folder_path}")

    # Create files
    for file in files:
        file_path = root / file

        # Make sure parent directory exists
        file_path.parent.mkdir(parents=True, exist_ok=True)

        if not file_path.exists():
            file_path.touch()
            print(f"Created file:   {file_path}")
        else:
            print(f"Already exists: {file_path}")

    print("\n✅ MLOps project structure created successfully!")
    print(f"📁 Project location: {root.resolve()}")


if __name__ == "__main__":
    create_project_structure()