
# Streamlit Project

## Installation using `virtualenv`

1. **Clone the repository**:
    ```bash
    git clone https://github.com/duchung45644/Streamlit.git
    cd Streamlit
    ```
2. **Create a virtual environment**:
	- Use `virtualenv`:
	    ```bash
	    virtualenv env_name
	    ```
   	- Use `conda`:
	    ```bash
	    conda create --name env_name
	    ```

3. **Activate the virtual environment**:
    - Virtualenv:
	    - On Windows:
	      ```bash
	      env_name\Scripts\activate
	      ```
	    - On macOS and Linux:
	      ```bash
	      source env_name/bin/activate
	      ```
     - Conda:
	   ```bash
	   conda activate env_name
	   ```
4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

1. **Navigate to the project directory**:
    ```bash
    cd path/to/your/project
    ```

2. **Run the Streamlit application**:
    ```bash
    streamlit run home.py
    ```

## Dependencies

- **Streamlit**: A web app framework for Python.
- **OpenCV**: A library for computer vision tasks.
- **HugChat**: A library for building conversational AI.
- **Pillow**: A library for image processing.
- **NumPy**: A library for numerical computations.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [OpenCV](https://opencv.org/)
- [HugChat](https://github.com/author/hugchat)
- [Pillow](https://python-pillow.org/)
- [NumPy](https://numpy.org/)