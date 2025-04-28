import streamlit as st
import tkinter as tk
from tkinter import filedialog

# Set up tkinter
root = tk.Tk()
root.withdraw()

# Make folder picker dialog appear on top of other windows
root.wm_attributes('-topmost', 1)

# Folder picker button
st.title('Selecione arquivos')
st.write('Selecione o arquivo desejado')

clickFiles = st.button('Selecionar arquivos')
if clickFiles:
    files = st.text_input("Seleção", filedialog.askopenfilenames(master=root,
                                                                filetypes = [('Text files', '*.TXT'),('All files', '*.*')]))

clickFiles = st.button('Selecionar arquivo')
if clickFiles:
    files = st.text_input("Seleção", filedialog.askopenfilename(master=root,
                                                                filetypes = [('Text files', '*.TXT'),('All files', '*.*')]))

