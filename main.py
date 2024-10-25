import os

from create_xml import create_xml


def main():
    file_names = os.listdir("2024")
    count =0
    for file_name in file_names:
        if file_name.endswith(".xlsx"):
            create_xml(f"2024/{file_name}")
            count += 1
            print(f"{count} files created")

    print("Done")


if __name__ == "__main__":
    main()