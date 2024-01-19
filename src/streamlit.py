import streamlit as st
from pickle import load

#load the model
with open('models/tree_classifier_crit-entro_maxdepth-5_minleaf-4_minsplit2_28.sav', 'rb') as file:
    model = pickle.load(file)

