from dataclasses import dataclass
import streamlit as st


@dataclass
class Credentials:
    ACCESS_TOKEN: str = None
    AD_ACCOUNT_ID: str = None
    APP_ID: str = None
    APP_SECRET: str = None
