from zipfile import ZipFile
import os
import pathlib
from typing import List


def unzip_and_getfilepaths(zip_file: pathlib.Path, extract_to: pathlib.Path) -> List[pathlib.Path]:
    """
    Unzips the given zipfile to the specified directory and returns a list of extracted file paths.
    """

    extracted_files = []

    with ZipFile(zip_file) as zip_ref:
        zip_ref.extractall(extract_to)
        for file_info in zip_ref.infolist():
            extracted_files.append(extract_to / file_info.filename)

    return extracted_files