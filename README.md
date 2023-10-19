
# Excel file Query 

This Python project utilizes the LLM (Language Model Layer) from Hugging Face to perform Excel file queries. It enables the use of natural language queries to interact with Excel files and extract relevant information.

## Libraries Used

- torch (PyTorch)
- transformers (Hugging Face Transformers)
- pipeline (Hugging Face)

## Features

- **Excel File Querying**: The project allows users to query Excel files using natural language.
- **Customizable Queries**: Users can specify their queries in plain language to extract specific data.
- **Integration with LLM**: It leverages the LLM model from Hugging Face to interpret and process natural language queries.
- **Ease of Use**: The pipeline from Hugging Face simplifies the interaction with LLM and Excel files.

## Prerequisites

Before running the script, make sure you have the following libraries installed:

- Python 3.x
- torch
- transformers
- pipeline

You can install these libraries using pip:

```bash
pip install torch transformers pipeline
```

## Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/mrnithish/excelfile-querys-llm-model.git
```

2. Navigate to the project directory:

```bash
cd excelfile-querys-llm-model
```

3. Run the Python script to perform Excel file queries:

```bash
python answerbot.py
```

4. Follow the prompts to specify your natural language query and the Excel file you want to query.

5. The script will provide the results of your query based on the LLM model's interpretation.

## Customization

You can customize the script to handle specific Excel files and queries by modifying the `excel_queries.py` script. Additionally, you can fine-tune the LLM model to improve its understanding of your queries.

## License

This project is licensed under the MIT License . See the [LICENSE.md](LICENSE.md) file for details.
