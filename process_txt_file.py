def lines_to_list(file_path):
    """
    Read a .txt file, convert each line into a separate list element, and return the list.

    Parameters:
    - file_path (str): Path to the input .txt file.

    Returns:
    - lines_list (list): List of lines as separate elements.
    """
    lines_list = []

    try:
        # Read the content of the .txt file
        with open(file_path, 'r') as file:
            lines_list = [line.strip() for line in file.readlines()]

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    return lines_list

# Example usage:
file_path =  "C:/Users/HP/Desktop/PASCAL VOC 2012/VOC2012/ImageSets/Segmentation/trainval.txt"
result = lines_to_list(file_path)
print(result)

