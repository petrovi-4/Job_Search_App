import sys

import pytest

from config import ROOT_DIR
from src.json_vacancy_data import JSONVacancyData

sys.path.append(ROOT_DIR)


@pytest.fixture
def json_vacancy_data(tmpdir):
    # Создаем временный файл для тенстов.
    temp_file = ROOT_DIR / "test_vacancies.json"
    return JSONVacancyData(temp_file)
