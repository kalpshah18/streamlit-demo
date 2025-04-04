import streamlit as st
import torch

GAMMA = {
    "params": lambda: {
        "alpha": st.sidebar.slider("Alpha (α)", 0.1, 10.0, 2.0, 0.1),
        "beta": st.sidebar.slider("Beta (β)", 0.1, 10.0, 2.0, 0.1),
    },
    "dist": lambda p: torch.distributions.Gamma(p["alpha"], p["beta"]),
    "support": lambda p: (0, None),
}