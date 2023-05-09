# Importing libraries
import json
import xmltodict
import os
import warnings
import pandas as pd

warnings.filterwarnings("ignore")


# Obtain names of the files in the path gived
def get_list_names(path):
    file_names = []

    for filename in os.listdir(path):
        f = os.path.join(path, filename)

        if os.path.isfile(f):
            if ".txt" not in filename:
                file_names.append(filename.split(".")[0])

    return file_names


# TODO: verify if it's necessary this function
# Function to check file names


def check_path(file_name):
    if file_name[0].isdigit():
        # return os.path.join(f'\', file_name)
        return file_name
    else:
        return file_name


# Convert XML files into JSON
def xml_to_json(path, file_names, path_to_save, encoding):
    for i, file_name in enumerate(file_names):
        file_name = check_path(file_name)
        final_path = f"{path}{file_name}.xml"

        # Reading XML file and converting it into text
        with open(final_path, encoding=encoding) as xml_file:
            data = xmltodict.parse(xml_file.read())

        # Converting text into JSON style
        data = json.dumps(data, indent=2)

        # Saving JSON file
        saving_path = f"{path_to_save}{file_name}.json"
        with open(saving_path, "w") as json_file:
            json_file.write(data)


# Get correct labels for the JSON file
def get_labels(labels_path, file_name):
    # Reading and creating a DF with correct JSON labels
    df_labels = pd.read_csv(
        labels_path, sep=":::", names=["id", "author", "gender"], engine="python"
    )

    # Obtaining author and gender labels
    author = df_labels[df_labels.id == file_name].author
    gender = df_labels[df_labels.id == file_name].gender

    return author.values[0], gender.values[0]


# JSON to CSV
def json_to_csv(path, labels_path, file_names, csv_name, encoding):
    data = pd.DataFrame(columns=["id", "tweet", "author", "gender"])

    for file_name in file_names:
        # Verify PATH
        file_name = check_path(file_name)

        # Reading JSON file based on file name
        with open(f"{path}{file_name}.json") as f:
            json_file = json.load(f)

        # Obtaining the amount of documents the JSON file has
        file_len = len(json_file["author"]["documents"]["document"])

        # Getting JSON labels
        author, gender = get_labels(labels_path, file_name)

        # Organizing data information in a dictionary
        dict = {
            "id": [file_name] * file_len,
            "tweet": json_file["author"]["documents"]["document"],
            "author": [author] * file_len,
            "gender": [gender] * file_len,
        }

        df = pd.DataFrame(data=dict)
        data = data.append(df)
        data.to_csv(f"{csv_name}.csv", encoding=encoding)


# Main function
def principal_function(selected_dataset, language, encoding):
    # Paths
    if selected_dataset == "original":
        dataset = "pan19-author-profiling-earlybirds-20190320"
    elif selected_dataset == "training":
        dataset = "pan19-author-profiling-training-2019-02-18"
    elif selected_dataset == "test":
        dataset = "pan19-author-profiling-test-2019-04-29"

    # Making paths
    files_path = f"{dataset}/{language}/"
    labels_path = f"{dataset}/{language}.txt"
    path_to_save = f"JSON/{dataset}/{language}/"

    # Process
    file_names = get_list_names(path=files_path)
    xml_to_json(
        path=files_path,
        file_names=file_names,
        path_to_save=path_to_save,
        encoding=encoding,
    )
    json_to_csv(
        path=path_to_save,
        labels_path=labels_path,
        file_names=file_names,
        csv_name=f"{dataset}-{language}",
        encoding=encoding,
    )


if __name__ == "__main__":
    # Variables
    print("\nDatasets avaible:")
    print("'original': pan19-author-profiling-earlybirds-20190320")
    print("'training': pan19-author-profiling-training-2019-02-18")
    print("'test': pan19-author-profiling-test-2019-04-29")
    selected_dataset = str(input("Selected dataset: "))

    print("\nLanguages:")
    print("'en' (for English)")
    print("'es' (for Spanish)")
    language = str(input("Selected langauge: "))

    print("\nTypes of encoding:")
    print("'ascii' (for English documents)")
    print("'utf-8' (for Spanish documents)")
    encoding = str(input("Encoding: "))

    principal_function(
        selected_dataset=selected_dataset, language=language, encoding=encoding
    )
