import streamlit as st
import pieces_os_client
from os import environ
from internal.environment.read_env import read_env_file	

def check_setup():
    # Set the IP and port of the Pieces OS you want to use
    read_env_file()
    ip = environ.get("PIECES_INSTANCE_HOST", "localhost")
    port = environ.get("PIECES_INSTANCE_PORT", "1000")
    
    # Set base configuration for the Pieces OS (set host to desired host)
    configuration = pieces_os_client.Configuration(host=f"http://{ip}:{port}")

    # Create an instance of the Pieces OS API client
    api_client = pieces_os_client.ApiClient(configuration)

    # chck if the Pieces OS is running and accessible
    with pieces_os_client.ApiClient(configuration) as api_client:
        # Create an instance of the WellKnownApi class
        api_instance = pieces_os_client.WellKnownApi(api_client)
        try:
            # Retrieve the (wellknown) health of the Pieces OS
            api_response = api_instance.get_well_known_health()
            st.success(f"The response of WellKnownApi().get_well_known_health: {api_response}")
            st.balloons()
        except Exception as e:
            st.error("Exception when calling WellKnownApi->get_well_known_health: %s\n" % e)
            st.write(f"IP: {ip}, Port: {port}")

def get_api_client():
    # Set the IP and port of the Pieces OS you want to use
    read_env_file()
    ip = environ.get("PIECES_INSTANCE_HOST", "localhost")
    port = environ.get("PIECES_INSTANCE_PORT", "1000")
    # Set base configuration for the Pieces OS (set host to desired host)
    configuration = pieces_os_client.Configuration(host=f"http://{ip}:{port}")

    # Create an instance of the Pieces OS API client
    api_client = pieces_os_client.ApiClient(configuration)
    return api_client