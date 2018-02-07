"""
This is the code for PDF Viewer
"""


def designer_pdf_viewer(height_letter, word_input):
    """
    Converts the letters to corresponding
    position checks for the presence and computes

    """
    lil, pip = [], []
    for i in word_input:
        lil.append(ord(i) - 97)

    for i, j in enumerate(height_letter):
        if i in lil:
            pip.append(j)
    print(max(pip) * len(word_input))
    # Complete this function


if __name__ == "__main__":

    HEIGHT_LETTER = list(map(int, input().strip().split(' ')))
    WORD_INPUT = input().strip()
    designer_pdf_viewer(HEIGHT_LETTER, WORD_INPUT)
