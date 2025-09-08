{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPiF2vxz6OduHgPiqri3l/t",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/vivekswamy021/Zomato-Data-Analysis/blob/main/Zomato__Data_Analysis_Project.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Import Libraries**"
      ],
      "metadata": {
        "id": "jb-dJeBzTNZB"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 171,
      "metadata": {
        "id": "QWlMejfaV_Sc"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "import warnings\n",
        "warnings.filterwarnings('ignore')"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Load the  Data**"
      ],
      "metadata": {
        "id": "JHeCovydXkSG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "uploaded = files.upload()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 73
        },
        "id": "9Vc4MHoTXsMb",
        "outputId": "c92682a7-d809-4547-ca4b-18926bc6ff42"
      },
      "execution_count": 172,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-22e13d6b-13eb-4c7f-899b-d65e074e926a\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-22e13d6b-13eb-4c7f-899b-d65e074e926a\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving Zomato-data-.csv to Zomato-data- (4).csv\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data=pd.read_csv('Zomato-data-.csv')\n",
        "data"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        },
        "id": "UuvNqG7rX1eK",
        "outputId": "2146a47f-660c-41e8-d2da-9d1e3819dcc8"
      },
      "execution_count": 173,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                      name online_order book_table   rate  votes  \\\n",
              "0                    Jalsa          Yes        Yes  4.1/5    775   \n",
              "1           Spice Elephant          Yes         No  4.1/5    787   \n",
              "2          San Churro Cafe          Yes         No  3.8/5    918   \n",
              "3    Addhuri Udupi Bhojana           No         No  3.7/5     88   \n",
              "4            Grand Village           No         No  3.8/5    166   \n",
              "..                     ...          ...        ...    ...    ...   \n",
              "143       Melting Melodies           No         No  3.3/5      0   \n",
              "144        New Indraprasta           No         No  3.3/5      0   \n",
              "145           Anna Kuteera          Yes         No  4.0/5    771   \n",
              "146                 Darbar           No         No  3.0/5     98   \n",
              "147          Vijayalakshmi          Yes         No  3.9/5     47   \n",
              "\n",
              "     approx_cost(for two people) listed_in(type)  \n",
              "0                            800          Buffet  \n",
              "1                            800          Buffet  \n",
              "2                            800          Buffet  \n",
              "3                            300          Buffet  \n",
              "4                            600          Buffet  \n",
              "..                           ...             ...  \n",
              "143                          100          Dining  \n",
              "144                          150          Dining  \n",
              "145                          450          Dining  \n",
              "146                          800          Dining  \n",
              "147                          200          Dining  \n",
              "\n",
              "[148 rows x 7 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-ba253621-e563-47a0-9035-7b1c004d24d7\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>name</th>\n",
              "      <th>online_order</th>\n",
              "      <th>book_table</th>\n",
              "      <th>rate</th>\n",
              "      <th>votes</th>\n",
              "      <th>approx_cost(for two people)</th>\n",
              "      <th>listed_in(type)</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Jalsa</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>4.1/5</td>\n",
              "      <td>775</td>\n",
              "      <td>800</td>\n",
              "      <td>Buffet</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Spice Elephant</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>4.1/5</td>\n",
              "      <td>787</td>\n",
              "      <td>800</td>\n",
              "      <td>Buffet</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>San Churro Cafe</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>3.8/5</td>\n",
              "      <td>918</td>\n",
              "      <td>800</td>\n",
              "      <td>Buffet</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Addhuri Udupi Bhojana</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>3.7/5</td>\n",
              "      <td>88</td>\n",
              "      <td>300</td>\n",
              "      <td>Buffet</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Grand Village</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>3.8/5</td>\n",
              "      <td>166</td>\n",
              "      <td>600</td>\n",
              "      <td>Buffet</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>143</th>\n",
              "      <td>Melting Melodies</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>3.3/5</td>\n",
              "      <td>0</td>\n",
              "      <td>100</td>\n",
              "      <td>Dining</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>144</th>\n",
              "      <td>New Indraprasta</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>3.3/5</td>\n",
              "      <td>0</td>\n",
              "      <td>150</td>\n",
              "      <td>Dining</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>145</th>\n",
              "      <td>Anna Kuteera</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>4.0/5</td>\n",
              "      <td>771</td>\n",
              "      <td>450</td>\n",
              "      <td>Dining</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>146</th>\n",
              "      <td>Darbar</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>3.0/5</td>\n",
              "      <td>98</td>\n",
              "      <td>800</td>\n",
              "      <td>Dining</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>147</th>\n",
              "      <td>Vijayalakshmi</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>3.9/5</td>\n",
              "      <td>47</td>\n",
              "      <td>200</td>\n",
              "      <td>Dining</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>148 rows × 7 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ba253621-e563-47a0-9035-7b1c004d24d7')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-ba253621-e563-47a0-9035-7b1c004d24d7 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-ba253621-e563-47a0-9035-7b1c004d24d7');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    <div id=\"df-b1c06200-65f9-488e-8b1a-cdf9f3f51d91\">\n",
              "      <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-b1c06200-65f9-488e-8b1a-cdf9f3f51d91')\"\n",
              "                title=\"Suggest charts\"\n",
              "                style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "      </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "      <script>\n",
              "        async function quickchart(key) {\n",
              "          const quickchartButtonEl =\n",
              "            document.querySelector('#' + key + ' button');\n",
              "          quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "          quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "          try {\n",
              "            const charts = await google.colab.kernel.invokeFunction(\n",
              "                'suggestCharts', [key], {});\n",
              "          } catch (error) {\n",
              "            console.error('Error during call to suggestCharts:', error);\n",
              "          }\n",
              "          quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "          quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "        }\n",
              "        (() => {\n",
              "          let quickchartButtonEl =\n",
              "            document.querySelector('#df-b1c06200-65f9-488e-8b1a-cdf9f3f51d91 button');\n",
              "          quickchartButtonEl.style.display =\n",
              "            google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "        })();\n",
              "      </script>\n",
              "    </div>\n",
              "\n",
              "  <div id=\"id_b5bbfe76-f5ed-4471-bb1b-7cf3e285626d\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('data')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_b5bbfe76-f5ed-4471-bb1b-7cf3e285626d button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('data');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "data",
              "summary": "{\n  \"name\": \"data\",\n  \"rows\": 148,\n  \"fields\": [\n    {\n      \"column\": \"name\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 145,\n        \"samples\": [\n          \"The Biryani Cafe\",\n          \"Melting Melodies\",\n          \"Cuppa\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"online_order\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"No\",\n          \"Yes\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"book_table\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"No\",\n          \"Yes\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"rate\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 20,\n        \"samples\": [\n          \"4.1/5\",\n          \"2.6/5\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"votes\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 653,\n        \"min\": 0,\n        \"max\": 4884,\n        \"num_unique_values\": 90,\n        \"samples\": [\n          244,\n          31\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"approx_cost(for two people)\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 223,\n        \"min\": 100,\n        \"max\": 950,\n        \"num_unique_values\": 18,\n        \"samples\": [\n          800,\n          300\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"listed_in(type)\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 4,\n        \"samples\": [\n          \"Cafes\",\n          \"Dining\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 173
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5sYpnISlYByO",
        "outputId": "922ddde1-1b48-4ebe-9414-4770db0dc679"
      },
      "execution_count": 174,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 148 entries, 0 to 147\n",
            "Data columns (total 7 columns):\n",
            " #   Column                       Non-Null Count  Dtype \n",
            "---  ------                       --------------  ----- \n",
            " 0   name                         148 non-null    object\n",
            " 1   online_order                 148 non-null    object\n",
            " 2   book_table                   148 non-null    object\n",
            " 3   rate                         148 non-null    object\n",
            " 4   votes                        148 non-null    int64 \n",
            " 5   approx_cost(for two people)  148 non-null    int64 \n",
            " 6   listed_in(type)              148 non-null    object\n",
            "dtypes: int64(2), object(5)\n",
            "memory usage: 8.2+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data.isnull().sum()       # no null values present"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 303
        },
        "id": "Lt9fshOgZQjX",
        "outputId": "5a5247b8-a4e0-4a05-a51b-1e97ea1a0214"
      },
      "execution_count": 175,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "name                           0\n",
              "online_order                   0\n",
              "book_table                     0\n",
              "rate                           0\n",
              "votes                          0\n",
              "approx_cost(for two people)    0\n",
              "listed_in(type)                0\n",
              "dtype: int64"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>0</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>name</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>online_order</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>book_table</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>rate</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>votes</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>approx_cost(for two people)</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>listed_in(type)</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> int64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 175
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "numerical column = [\"votes\"],[\"cost_for_two\"]\n",
        "\n",
        "categorical column = [\"name\"],[\"online_order\"]    [\"book_table\"],[\"rate\"] , [\"votes\"], [\"cost_for_two\"] ,[\"restaurant_type\"]"
      ],
      "metadata": {
        "id": "9jYf4Ij4xaTn"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Data cleaning**\n",
        "\n",
        "- let’s convert the data type of the “rate” column to float and remove the denominator."
      ],
      "metadata": {
        "id": "VxBZvdSqZoRw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data['rate'] = data['rate'].str.replace('/5', '', regex=True).astype(float)\n",
        "\n",
        "data.rename(columns={'approx_cost(for two people)': 'cost_for_two', 'listed_in(type)': 'restaurant_type'}, inplace=True)"
      ],
      "metadata": {
        "id": "P6rb736bZabE"
      },
      "execution_count": 176,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "maJPFBYjautd",
        "outputId": "ef1ca66e-a66a-4337-8929-267cc1c58fbd"
      },
      "execution_count": 177,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                    name online_order book_table  rate  votes  cost_for_two  \\\n",
              "0                  Jalsa          Yes        Yes   4.1    775           800   \n",
              "1         Spice Elephant          Yes         No   4.1    787           800   \n",
              "2        San Churro Cafe          Yes         No   3.8    918           800   \n",
              "3  Addhuri Udupi Bhojana           No         No   3.7     88           300   \n",
              "4          Grand Village           No         No   3.8    166           600   \n",
              "\n",
              "  restaurant_type  \n",
              "0          Buffet  \n",
              "1          Buffet  \n",
              "2          Buffet  \n",
              "3          Buffet  \n",
              "4          Buffet  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-a42f40e1-e45b-49d8-8cb4-6c06afdf8b23\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>name</th>\n",
              "      <th>online_order</th>\n",
              "      <th>book_table</th>\n",
              "      <th>rate</th>\n",
              "      <th>votes</th>\n",
              "      <th>cost_for_two</th>\n",
              "      <th>restaurant_type</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Jalsa</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>4.1</td>\n",
              "      <td>775</td>\n",
              "      <td>800</td>\n",
              "      <td>Buffet</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Spice Elephant</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>4.1</td>\n",
              "      <td>787</td>\n",
              "      <td>800</td>\n",
              "      <td>Buffet</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>San Churro Cafe</td>\n",
              "      <td>Yes</td>\n",
              "      <td>No</td>\n",
              "      <td>3.8</td>\n",
              "      <td>918</td>\n",
              "      <td>800</td>\n",
              "      <td>Buffet</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Addhuri Udupi Bhojana</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>3.7</td>\n",
              "      <td>88</td>\n",
              "      <td>300</td>\n",
              "      <td>Buffet</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Grand Village</td>\n",
              "      <td>No</td>\n",
              "      <td>No</td>\n",
              "      <td>3.8</td>\n",
              "      <td>166</td>\n",
              "      <td>600</td>\n",
              "      <td>Buffet</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a42f40e1-e45b-49d8-8cb4-6c06afdf8b23')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-a42f40e1-e45b-49d8-8cb4-6c06afdf8b23 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-a42f40e1-e45b-49d8-8cb4-6c06afdf8b23');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    <div id=\"df-e7d60f20-52f7-41e5-9e38-d2b03c1aa694\">\n",
              "      <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-e7d60f20-52f7-41e5-9e38-d2b03c1aa694')\"\n",
              "                title=\"Suggest charts\"\n",
              "                style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "      </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "      <script>\n",
              "        async function quickchart(key) {\n",
              "          const quickchartButtonEl =\n",
              "            document.querySelector('#' + key + ' button');\n",
              "          quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "          quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "          try {\n",
              "            const charts = await google.colab.kernel.invokeFunction(\n",
              "                'suggestCharts', [key], {});\n",
              "          } catch (error) {\n",
              "            console.error('Error during call to suggestCharts:', error);\n",
              "          }\n",
              "          quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "          quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "        }\n",
              "        (() => {\n",
              "          let quickchartButtonEl =\n",
              "            document.querySelector('#df-e7d60f20-52f7-41e5-9e38-d2b03c1aa694 button');\n",
              "          quickchartButtonEl.style.display =\n",
              "            google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "        })();\n",
              "      </script>\n",
              "    </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "data",
              "summary": "{\n  \"name\": \"data\",\n  \"rows\": 148,\n  \"fields\": [\n    {\n      \"column\": \"name\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 145,\n        \"samples\": [\n          \"The Biryani Cafe\",\n          \"Melting Melodies\",\n          \"Cuppa\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"online_order\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"No\",\n          \"Yes\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"book_table\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"No\",\n          \"Yes\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"rate\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.40227051403803343,\n        \"min\": 2.6,\n        \"max\": 4.6,\n        \"num_unique_values\": 19,\n        \"samples\": [\n          4.1,\n          4.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"votes\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 653,\n        \"min\": 0,\n        \"max\": 4884,\n        \"num_unique_values\": 90,\n        \"samples\": [\n          244,\n          31\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"cost_for_two\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 223,\n        \"min\": 100,\n        \"max\": 950,\n        \"num_unique_values\": 18,\n        \"samples\": [\n          800,\n          300\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"restaurant_type\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 4,\n        \"samples\": [\n          \"Cafes\",\n          \"Dining\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 177
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "- Here, '/5' is treated as a regex pattern.\n",
        "\n",
        "- It removes the \"/5\" from values like \"4.1/5\", leaving only \"4.1\".\n",
        "\n",
        "\n",
        "\n",
        "- with out regex=True, str.replace() treats the pattern as a plain string."
      ],
      "metadata": {
        "id": "8BTMEP87aheA"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "data.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3G79aaOjxlzJ",
        "outputId": "22373722-fe68-41fc-b722-029a430e36ca"
      },
      "execution_count": 178,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 148 entries, 0 to 147\n",
            "Data columns (total 7 columns):\n",
            " #   Column           Non-Null Count  Dtype  \n",
            "---  ------           --------------  -----  \n",
            " 0   name             148 non-null    object \n",
            " 1   online_order     148 non-null    object \n",
            " 2   book_table       148 non-null    object \n",
            " 3   rate             148 non-null    float64\n",
            " 4   votes            148 non-null    int64  \n",
            " 5   cost_for_two     148 non-null    int64  \n",
            " 6   restaurant_type  148 non-null    object \n",
            "dtypes: float64(1), int64(2), object(4)\n",
            "memory usage: 8.2+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"votes\"].skew()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZxRBmeLZnWIq",
        "outputId": "9f06b3a6-4f24-4844-8546-ad7781830f64"
      },
      "execution_count": 179,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "np.float64(4.936309828623457)"
            ]
          },
          "metadata": {},
          "execution_count": 179
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "nmgwNDtbxTvs",
        "outputId": "dda21584-6703-4ad4-860b-b68b6bdccd13"
      },
      "execution_count": 180,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "             rate        votes  cost_for_two\n",
              "count  148.000000   148.000000    148.000000\n",
              "mean     3.633108   264.810811    418.243243\n",
              "std      0.402271   653.676951    223.085098\n",
              "min      2.600000     0.000000    100.000000\n",
              "25%      3.300000     6.750000    200.000000\n",
              "50%      3.700000    43.500000    400.000000\n",
              "75%      3.900000   221.750000    600.000000\n",
              "max      4.600000  4884.000000    950.000000"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-add00436-cf5e-48d8-88a6-5a30ad107a9a\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>rate</th>\n",
              "      <th>votes</th>\n",
              "      <th>cost_for_two</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>148.000000</td>\n",
              "      <td>148.000000</td>\n",
              "      <td>148.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>3.633108</td>\n",
              "      <td>264.810811</td>\n",
              "      <td>418.243243</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>0.402271</td>\n",
              "      <td>653.676951</td>\n",
              "      <td>223.085098</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>2.600000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>100.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>3.300000</td>\n",
              "      <td>6.750000</td>\n",
              "      <td>200.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>3.700000</td>\n",
              "      <td>43.500000</td>\n",
              "      <td>400.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>3.900000</td>\n",
              "      <td>221.750000</td>\n",
              "      <td>600.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>4.600000</td>\n",
              "      <td>4884.000000</td>\n",
              "      <td>950.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-add00436-cf5e-48d8-88a6-5a30ad107a9a')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-add00436-cf5e-48d8-88a6-5a30ad107a9a button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-add00436-cf5e-48d8-88a6-5a30ad107a9a');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    <div id=\"df-4b15a8fb-f872-4a89-a83e-659a3410b452\">\n",
              "      <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-4b15a8fb-f872-4a89-a83e-659a3410b452')\"\n",
              "                title=\"Suggest charts\"\n",
              "                style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "      </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "      <script>\n",
              "        async function quickchart(key) {\n",
              "          const quickchartButtonEl =\n",
              "            document.querySelector('#' + key + ' button');\n",
              "          quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "          quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "          try {\n",
              "            const charts = await google.colab.kernel.invokeFunction(\n",
              "                'suggestCharts', [key], {});\n",
              "          } catch (error) {\n",
              "            console.error('Error during call to suggestCharts:', error);\n",
              "          }\n",
              "          quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "          quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "        }\n",
              "        (() => {\n",
              "          let quickchartButtonEl =\n",
              "            document.querySelector('#df-4b15a8fb-f872-4a89-a83e-659a3410b452 button');\n",
              "          quickchartButtonEl.style.display =\n",
              "            google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "        })();\n",
              "      </script>\n",
              "    </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"data\",\n  \"rows\": 8,\n  \"fields\": [\n    {\n      \"column\": \"rate\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 51.22334207556026,\n        \"min\": 0.40227051403803343,\n        \"max\": 148.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          3.6331081081081082,\n          3.7,\n          148.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"votes\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1672.63564274403,\n        \"min\": 0.0,\n        \"max\": 4884.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          264.81081081081084,\n          43.5,\n          148.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"cost_for_two\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 283.95391371814867,\n        \"min\": 100.0,\n        \"max\": 950.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          418.2432432432432,\n          400.0,\n          148.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 180
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Grouped Analysis\n",
        "online_rating = data.groupby('online_order')['rate'].mean()\n",
        "\n",
        "booking_rating = data.groupby('book_table')['rate'].mean()\n",
        "\n",
        "listing_counts = data['restaurant_type'].value_counts()\n",
        "\n",
        "correlation_cost_rating = data['rate'].corr(data['cost_for_two'])\n",
        "\n",
        "online_rating, booking_rating, listing_counts, correlation_cost_rating"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6l67A2dehON3",
        "outputId": "eff1d9ad-c01a-4db1-98b5-1a8fc262735f"
      },
      "execution_count": 181,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(online_order\n",
              " No     3.487778\n",
              " Yes    3.858621\n",
              " Name: rate, dtype: float64,\n",
              " book_table\n",
              " No     3.601429\n",
              " Yes    4.187500\n",
              " Name: rate, dtype: float64,\n",
              " restaurant_type\n",
              " Dining    110\n",
              " Cafes      23\n",
              " other       8\n",
              " Buffet      7\n",
              " Name: count, dtype: int64,\n",
              " np.float64(0.2752157461607433))"
            ]
          },
          "metadata": {},
          "execution_count": 181
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Data visualization**"
      ],
      "metadata": {
        "id": "xCkmCs4ncKXp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#count of restaurant type\n",
        "sns.countplot(x=data['restaurant_type'],palette='viridis')\n",
        "plt.xlabel(\"Distribution of restaurant type\")\n",
        "plt.show()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 449
        },
        "id": "bjJzM6FfeKaP",
        "outputId": "61cc912d-ad98-4673-fe3d-b38bbc98dbc3"
      },
      "execution_count": 182,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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ckn9VQcAAFBH5xR2rr76ajkcDjkcjmpvV/n7++uFF16ot+IAAADq6pzCTk5Ojowxuuyyy7Rlyxa1bt3atczX11dt2rRRkyZN6r1IAACA2jqnsBMVFSVJqqqqapBiAAAA6ts5hZ2T7d27V+vWrVNBQcEp4Wfy5Ml1LuyEb7/9VhMmTNDq1at19OhRxcbGauHCherWrZskyRijtLQ0zZ8/X4WFherVq5fmzp2r9u3b11sNAADgwlWrsDN//nyNHDlSrVq1UlhYmBwOh2uZw+Got7Bz+PBh9erVS3379tXq1avVunVr7d27V82bN3f1mT59umbPnq1FixYpJiZGkyZNUmJior744gv5+fnVSx0AAODCVauwM23aND311FOaMGFCfdfj5tlnn1VkZKQWLlzoaouJiXH92xijWbNm6fHHH9egQYMkSa+++qpCQ0O1YsUKDRs2rEHrAwAAnq9Wn7Nz+PBh3X777fVdyyneeecddevWTbfffrvatGmjrl27av78+a7lOTk5ysvLU0JCgqstJCREPXr00KZNm2oct6ysTMXFxW4TAACwU63Czu233641a9bUdy2n+Pe//+16/uaf//ynRo4cqbFjx2rRokWS5Pqcn9DQULf1QkND3T4D6OfS09MVEhLimiIjIxtuJwAAQKOq1W2s2NhYTZo0SR999JGuuuoq+fj4uC0fO3ZsvRRXVVWlbt266emnn5Ykde3aVZ999pnmzZun5OTkWo87ceJEpaamuuaLi4sJPAAAWKpWYefll19W06ZNlZWVpaysLLdlDoej3sJOeHi4rrjiCre2uLg4LVu2TJIUFhYmScrPz1d4eLirT35+vq6++uoax3U6nXI6nfVSIwAA8Gy1Cjs5OTn1XUe1evXqpd27d7u17dmzx/V5PzExMQoLC1NmZqYr3BQXF2vz5s0aOXLkeakRAAB4tlp/zs758Mgjj6hnz556+umndccdd2jLli16+eWX9fLLL0s6fhVp3LhxmjZtmtq3b+9663lERIQGDx7cuMUDAACPUKuwc9999512+YIFC2pVzM9dd911Wr58uSZOnKipU6cqJiZGs2bN0vDhw119Hn30UR05ckT333+/CgsLdf311ysjI4PP2AEAAJJqGXYOHz7sNl9RUaHPPvtMhYWF1X5BaF0MGDBAAwYMqHG5w+HQ1KlTNXXq1HrdLgAAsEOt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SclZjZuQkKD4+HgNHjxYa9as0f79+/Xhhx/qj3/8oz7++OMG3iv83Inf5d9++622b9+up59+WoMGDdKAAQN09913n5cagoKClJycrPHjx2vdunX6/PPPlZKSIi8vr9PeSrvQEHYuQBkZGQoPD1d4eLh69OihrVu3aunSperTp498fHz02muv6csvv1Tnzp317LPPatq0abXaTufOnZWVlaU9e/bohhtuUNeuXTV58mRFRES4+kydOlX79+9Xu3btuMffgC677DJt375dffv21e9+9zt16tRJN998szIzMzV37lx16dJFM2fO1LPPPqtOnTpp8eLFSk9PP+O4ZzrHzZo101tvvaV+/fopLi5O8+bN02uvvaYrr7yyoXf5ovfMM89oyJAhuuuuu3TNNdfoq6++0j//+U81b95cl1xyiaZMmaLHHntMoaGhbn+AnI7D4dD//d//qXfv3rr33nt1+eWXa9iwYfr6668VGhrawHuEnzvxuzw6OlpJSUlat26dZs+erbfffltNmjQ5b3XMnDlT8fHxGjBggBISEtSrVy/FxcXJz8/vvNXQ0BzmbJ9+BAAA1jty5IguueQSzZgxQykpKY1dTr3gmR0AAC5iO3bs0Jdffqnu3burqKhIU6dOlSQNGjSokSurP4QdAAAucn/605+0e/du+fr66tprr9X777+vVq1aNXZZ9YbbWAAAwGo8oAwAAKxG2AEAAFYj7AAAAKsRdgAAgNUIOwAAwGqEHeA8cjgcWrFiRb2P26dPH40bN841Hx0drVmzZtX7dqrbVmMxxuj+++9XixYt5HA4av0dcADsR9gB6uiee+6Rw+GQw+GQj4+PQkNDdfPNN2vBggWnfLNwbm6u+vfvf1bjnksweuutt/Tkk0+ea+mntX79ejkcDhUWFjb4tmojIyNDr7zyilauXKnc3Fx16tTpvGy3puPi6c627ldeeYVvtId1CDtAPUhKSlJubq7279+v1atXq2/fvnr44Yc1YMAAHTt2zNUvLCxMTqez3rZbXl4u6fg3owcFBdXbuKdzPrd1Ovv27VN4eLh69uypsLAweXuf+TNSKysrTwmgnuxCqxfwWAZAnSQnJ5tBgwad0p6ZmWkkmfnz57vaJJnly5cbY4wpKyszo0aNMmFhYcbpdJpLL73UPP3008YYY6Kioowk1xQVFWWMMSYtLc106dLFzJ8/30RHRxuHw2GMMebGG280Dz/8sGs7UVFRZurUqWbYsGEmICDAREREmL/85S+u5Tk5OUaS2bFjh6vt8OHDRpJZt26da/nJU3JycrXbOnTokLnrrrtMs2bNjL+/v0lKSjJ79uxxLV+4cKEJCQkxGRkZpmPHjiYwMNAkJiaa77777rTHdf369ea6664zvr6+JiwszEyYMMFUVFS4jnl1x+fnTmz77bffNnFxcaZJkyYmJyfHlJaWmt/97ncmIiLCBAQEmO7du5t169a51tu/f78ZMGCAadasmQkICDBXXHGFWbVq1WmPy+rVq02vXr1MSEiIadGihbn11lvNV1995Rpz3bp1RpI5fPiwq23Hjh1GksnJyTltvVu2bDEJCQmmZcuWJjg42PTu3dts27bNbV9P/F8bPHiw8ff3N7Gxsebtt992O9/V1X2yEzWePKWlpZkpU6aYK6+88pT+Xbp0MY8//rjrnAwaNMg88cQTplWrViYoKMg88MADpqyszNW/srLSPP300yY6Otr4+fmZzp07m6VLl1Z77oD6RNgB6qimsGPM8ReD/v37u+ZPDjvPPfeciYyMNBs2bDD79+8377//vlmyZIkxxpiCggIjySxcuNDk5uaagoICY8zxsBMYGGiSkpLM9u3bzSeffGKMqT7sBAUFmfT0dLN7924ze/Zs06RJE7NmzRpjzJnDzrFjx8yyZcuMJLN7926Tm5trCgsLq93W//zP/5i4uDizYcMGs3PnTpOYmGhiY2NNeXm5Meb4C7iPj49JSEgwW7duNdu2bTNxcXHmN7/5TY3H9D//+Y8JCAgwDz30kMnOzjbLly83rVq1MmlpacYYYwoLC83UqVNN27Zt3Y7Pz53Yds+ePc3GjRvNl19+aY4cOWJ++9vfmp49e5oNGzaYr776yjz33HPG6XS6Qtqtt95qbr75ZrNr1y6zb98+8+6775qsrKzTHpc333zTLFu2zOzdu9fs2LHDDBw40Fx11VWmsrLSGHP2Yae6ejMzM83f//53k52dbb744guTkpJiQkNDTXFxsdv/rbZt25olS5aYvXv3mrFjx5qmTZuaH3744bR1n6ysrMzMmjXLBAcHm9zcXJObm2t+/PFHc+DAAePl5WW2bNni6rt9+3bjcDjMvn37jDHHfw6aNm1qhg4daj777DOzcuVK07p1a/OHP/zBtc60adNMx44dTUZGhtm3b59ZuHChcTqdZv369TX+XwDqA2EHqKPThZ2hQ4eauLg41/zJYWfMmDGmX79+pqqqqtp1T+57QlpamvHx8Tnlxb26sJOUlHRKLSeC15nCjjHVvzj/fFt79uwxkszGjRtdy7///nvj7+9v3njjDWPM8RdwSW5XOebMmWNCQ0Or3W9jjPnDH/5gOnTo4HZs5syZY5o2beoKD88//3yNV3ROOLHtnTt3utq+/vpr06RJE/Ptt9+69b3pppvMxIkTjTHGXHXVVeaJJ56odsyajsvPHTx40Egyn376aY3rVRd2fl5vdSorK01QUJB59913XW2SXFdZjDGmpKTESDKrV68+p7pPXF36uf79+5uRI0e65seMGWP69Onjmk9OTjYtWrQwR44ccbXNnTvXdc5KS0tNQECA+fDDD93GTUlJMXfeeedpawLqimd2gAZkjJHD4ah22T333KOdO3eqQ4cOGjt2rNasWXNWY0ZFRal169Zn7BcfH3/KfHZ29llt42xlZ2fL29tbPXr0cLW1bNlSHTp0cNtWQECA2rVr55oPDw9XQUHBaceNj493O3a9evVSSUmJ/vOf/5xTjb6+vurcubNr/tNPP1VlZaUuv/xyNW3a1DVlZWVp3759kqSxY8dq2rRp6tWrl9LS0rRr164zbmfv3r268847ddlllyk4OFjR0dGSpG+++aZO9UpSfn6+RowYofbt2yskJETBwcEqKSk5ZeyT1wsMDFRwcPBpj/O5GDFihF577TWVlpaqvLxcS5Ys0X333efWp0uXLgoICHDNx8fHq6SkRAcOHNBXX32lo0eP6uabb3Y77q+++qrruAMNhW89BxpQdna2YmJiql12zTXXKCcnR6tXr9a//vUv3XHHHUpISNCbb7552jEDAwPrXJeX1/G/c8xJ3wNcUVFR53Fr4uPj4zbvcDjctt2Q/P393UJTSUmJmjRpom3btqlJkyZufZs2bSpJ+u1vf6vExEStWrVKa9asUXp6umbMmKExY8bUuJ2BAwcqKipK8+fPV0REhKqqqtSpUyfXQ+Rne8x/Xq8kJScn64cfftCf//xnRUVFyel0Kj4+3jX2CdUd5/p6wHngwIFyOp1avny5fH19VVFRodtuu+2s1y8pKZEkrVq1Spdcconbsvp8aB+oDmEHaCBr167Vp59+qkceeaTGPsHBwRo6dKiGDh2q2267TUlJSTp06JBatGghHx8fVVZW1nr7H3300SnzcXFxkuS6MpSbm6uuXbtK0imfU+Pr6ytJp60hLi5Ox44d0+bNm9WzZ09J0g8//KDdu3friiuuqHXtcXFxWrZsmduVsY0bNyooKEht27at9biS1LVrV1VWVqqgoEA33HBDjf0iIyP14IMP6sEHH9TEiRM1f/58jRkzptrjcmKf58+f7xrzgw8+cBvv5GPevHlzSace85ps3LhRL774om655RZJ0oEDB/T999+f3Q7/19mczxP9quvj7e2t5ORkLVy4UL6+vho2bJj8/f3d+nzyySf66aefXO0fffSRmjZtqsjISLVo0UJOp1PffPONbrzxxnOqHagrwg5QD8rKypSXl6fKykrl5+crIyND6enpGjBggO6+++5q15k5c6bCw8PVtWtXeXl5aenSpQoLC3N9xkl0dLQyMzPVq1cvOZ1O1wvk2dq4caOmT5+uwYMH67333tPSpUu1atUqScevHvziF7/QM888o5iYGBUUFOjxxx93Wz8qKkoOh0MrV67ULbfcIn9/f9eVjxPat2+vQYMGacSIEXrppZcUFBSkxx57TJdccokGDRp0TvWe7KGHHtKsWbM0ZswYjR49Wrt371ZaWppSU1NdV0hq6/LLL9fw4cN19913a8aMGeratasOHjyozMxMde7cWbfeeqvGjRun/v376/LLL9fhw4e1bt06V1Cs7rg0b95cLVu21Msvv6zw8HB98803euyxx9y2Gxsbq8jISD3xxBN66qmntGfPHs2YMeOsam7fvr3+/ve/q1u3biouLtb48eNPCRpncjbnUzr+/66kpESZmZmu21Inbk399re/dR2HjRs3nrJueXm5UlJS9Pjjj2v//v1KS0vT6NGj5eXlpaCgIP3+97/XI488oqqqKl1//fUqKirSxo0bFRwcrOTk5HPaH+CcNOoTQ4AFTn4btLe3t2ndurVJSEgwCxYscD1Me4JOeuj45ZdfNldffbUJDAw0wcHB5qabbjLbt2939X3nnXdMbGys8fb2PuWt5z9X3QPKU6ZMMbfffrsJCAgwYWFh5s9//rPbOl988YWJj483/v7+5uqrrzZr1qxxe0DZGGOmTp1qwsLCjMPhOONbz0NCQoy/v79JTEys9q3nJ1u+fLk506+f07313Jizf0C5uodty8vLzeTJk010dLTx8fEx4eHh5le/+pXZtWuXMcaY0aNHm3bt2hmn02lat25t7rrrLvP999+f9ri89957Ji4uzjidTtO5c2ezfv36Ux4y/+CDD8xVV11l/Pz8zA033GCWLl1a7VvPf2779u2mW7duxs/Pz7Rv394sXbrUREVFmeeff97V5+fbMsaYkJAQs3DhwtPWXZ0HH3zQtGzZ0vXW85PdcMMN1b4N/cSD+pMnTzYtW7Y0TZs2NSNGjDClpaWuPlVVVWbWrFmmQ4cOxsfHx7Ru3dokJiaarKysGmsB6oPDmPN04xwAcEEzxqh9+/Z66KGHlJqa6rbsnnvuUWFhYYN8HQpQV9zGAgCc0cGDB/X6668rLy9P9957b2OXA5wTwg4A4IzatGmjVq1a6eWXXz7n58eAxsZtLAAAYDU+VBAAAFiNsAMAAKxG2AEAAFYj7AAAAKsRdgAAgNUIOwAAwGqEHQAAYDXCDgAAsNr/AwEHp3vEkvSsAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "The majority of the restaurants fall into the dining category."
      ],
      "metadata": {
        "id": "OTY68I4Gef7c"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Distribution of Ratings\n",
        "sns.histplot(data['rate'], kde=True, color='blue')\n",
        "plt.title(\"Distribution of Restaurant Ratings\")\n",
        "plt.xlabel(\"Rating\")\n",
        "plt.ylabel(\"Count\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 472
        },
        "id": "k4OsMlgvl9_i",
        "outputId": "60bd3bb7-c86e-4ea7-e1d7-ea7b3b67dd29"
      },
      "execution_count": 183,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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CXEWQePHj6djx47cf//9XLhwgZkzZ9KtWzfmzp1L+/btU73G9T67u+++mx07djBjxgzeffddQkJCnMecUSnFyeWfwbp161i1ahU9evSgePHi7N27l4kTJ9KsWTP+/vtvAgICaNKkCU8++STvvfceQ4cOpUqVKgDOr1czZswY8uTJw3PPPUdsbCxvvvkm999/P2vXrnXuM3HiRAYMGEDjxo15+umn2bt3L507d6ZgwYIUL17cud8nn3zCk08+yT333MNTTz1FfHw8mzZtYu3atdx3330Z/lmIi7NEXMzkyZMtwFq3bt1V9wkKCrJq167tvD98+HDr8n/O7777rgVYx44du+prrFu3zgKsyZMnp3muadOmFmB99NFH6T7XtGlT5/2lS5dagFWsWDErLi7O+fisWbMswBo/frzzsVKlSlm9e/e+7mteK1vv3r2tUqVKOe9/9913FmC9+uqrqfa75557LIfDYe3atcv5GGD5+PikeuzPP/+0AOv9999P816XGzdunAVYX375pfOxCxcuWA0aNLDy58+f6thLlSpltW/f/pqvd/m+rVu3to4dO2YdO3bM2rx5s/XAAw9YgNW/f3/nfr/++qsFWNOmTUv1/fPnz0/1+Jw5c6777+fYsWMWYA0fPjzNc+fOnUvz2IwZMyzAWrFihfOxKz+HFFf+W7Qs83PPkyeP9ddff133/S5cuGBVr17datGiRZrXuJHP7q233rIAa8+ePWneKz29e/e28uXL5/z579q1y3r77bcth8NhVa9e3UpOTr5qVsuyrNWrV1uA9cUXXzgf+/rrry3AWrp0aZr9r3b+VKlSxUpISHA+Pn78eAuwNm/ebFmWZSUkJFiFCxe26tatayUmJjr3mzJligWkes1OnTpZ1apVu6HjF/enS0vilvLnz3/N0UspnRy///77THeM9fX1pW/fvje8/4MPPkiBAgWc9++55x4iIiKYN29ept7/Rs2bNw8vLy+efPLJVI8/++yzWJbFzz//nOrxVq1aUa5cOef9mjVrEhgYmOoSwtXeJzw8nJ49ezof8/b25sknn+TMmTMsX74808ewcOFCQkNDCQ0NpUaNGkydOpW+ffvy1ltvOff5+uuvCQoK4o477iAmJsZ5i4yMJH/+/CxduhS49NnPnTuXxMTEDGe5vPUsPj6emJgYbrvtNgA2bNiQ6WNs2rRpuv2G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2bp1K1WqVKFDhw5MnTqVoKAgqlatyurVq/nll1/SDNu/5ZZb8PLy4o033iA2NhZfX19atGhBkSJFMnVMYIqRESNGMHDgQFq0aEH37t3Zu3cvU6ZMoVy5cqlagVq3bk14eDiNGjUiLCyMrVu38sEHH9C+ffss/3cqLsC28VIiV5Ey/Drl5uPjY4WHh1t33HGHNX78+FTDfFNcOeR18eLFVqdOnayiRYtaPj4+VtGiRa2ePXtaO3bsSPV933//vVW1alUrb968qYY7N23a9KrDN682fHTGjBnWkCFDrCJFilj+/v5W+/btrX379qX5/nfeeccqVqyY5evrazVq1Mhav359mte8Vrb0hv2ePn3aevrpp62iRYta3t7eVoUKFay33nor1dBZy7LSDGlOcbVh4Vc6cuSI1bdvXyskJMTy8fGxatSoke4Q8YwOv77avilDay9/j//9739WZGSk5e/vbxUoUMCqUaOG9cILL1gHDx60LMuyNmzYYPXs2dMqWbKk5evraxUpUsTq0KGDtX79+lSvvWrVKisyMtLy8fFJNRT7wIEDVpcuXazg4GArKCjI6tatm3Xw4MF0h2svXLjQql69uuXj42NVqlTJ+vLLL686/Dq9n7tlWdakSZOsChUqWL6+vlblypWtyZMnZ+g10vvsXnnlFatYsWJWnjx5rjsUO2X4dXp2795teXl5OV//5MmTzs8/f/78Vps2baxt27alm+GTTz6xypYta3l5eaUain218+frr79O9f179uxJdwqC9957zypVqpTl6+tr1atXz1q5cqUVGRlptW3b1rnPxx9/bDVp0sQqXLiw5evra5UrV856/vnnrdjY2Kv+HMR9OSzLxh5+IiIiNyE5OZnQ0FDuvvtu52VIyV3UR0ZERNxCfHx8mj46X3zxBSdOnPC4xT/lxqlFRkRE3MKyZct4+umn6datG4ULF2bDhg1MmjSJKlWqEBUVpQUpcyl19hUREbdQunRpSpQowXvvvceJEycoVKgQDz74IGPGjFERk4upRUZERETclvrIiIiIiNtSISMiIiJuy+P7yCQnJ3Pw4EEKFCiQLdNmi4iISNazLIvTp09TtGjRNIvVXs7jC5mDBw9SokQJu2OIiIhIJuzfv5/ixYtf9XmPL2RSpqPev38/gYGBNqcRERGRGxEXF0eJEiWuu6yExxcyKZeTAgMDVciIiIi4met1C1FnXxEREXFbKmRERETEbamQEREREbelQkZERETclgoZERERcVsqZERERMRtqZARERERt6VCRkRERNyWChkRERFxWypkRERExG2pkBERERG3pUJGRERE3JYKGREREXFbKmRERETEbeW1O4CIeK7o6GhiYmLsjnHTQkJCKFmypN0xRCQdKmREJFtER0dTuXIVzp8/Z3eUm+bvH8C2bVtVzIi4IBUyIpItYmJiOH/+HF26fEloaBW742TasWNbmTOnFzExMSpkRFyQChkRyVahoVWIiLjV7hgi4qHU2VdERETclgoZERERcVsqZERERMRtqZARERERt6VCRkRERNyWChkRERFxWypkRERExG2pkBERERG3pUJGRERE3JZm9hURyWLnzsHJk3D6NISFQXAwOBx2pxLxTCpkRERu0sWL8OOP8NNPsGwZ7N6d+vnAQKhTBzp2hC5dQEs2iWQdXVoSEcmk+Hh4+20oVw7uvhsmTbpUxHh5mQIGIC4OliyBQYOgTBno1Qv++su22CIeRYWMiEgmLFgA1avD889DdDSEhMAzz8C8eXDiBCQmQmwsnD0LmzfDu+9CkyaQnAzTpkGNGqawOXvW7iMRcW8qZEREMiAhAfr1g7ZtTetL0aLw6aewfz+88w60awcFC17qExMQYAqeQYNg+XKIijKXlywLxo+HmjVh1SpbD0nErdlayEycOJGaNWsSGBhIYGAgDRo04Oeff3Y+Hx8fT//+/SlcuDD58+ena9euHDlyxMbEIpKbRUdD48bwv/+ZQuXpp2HbNnj4YfDzu7HXuPVW+PZbmD8fSpSAf/6BZs3gs8+yNbqIx7K1kClevDhjxowhKiqK9evX06JFCzp16sRf/3/x+Omnn+bHH3/k66+/Zvny5Rw8eJC7777bzsgikkv9848ft90G69ZBoULw888wdiwUKJC512vTBrZsga5dzWWohx82l6ksK2tzi3g6W0ct3XXXXanuv/baa0ycOJE1a9ZQvHhxJk2axPTp02nRogUAkydPpkqVKqxZs4bbbrvNjsgikivdyiOPVCQ21lwm+vFHKF365l81MBBmzYJXXoERI0zH4bNn4YMPII8u/IvcEJc5VZKSkpg5cyZnz56lQYMGREVFkZiYSKtWrZz7VK5cmZIlS7J69Wobk4pIbnL8uD+wmNjYvNSta/q5ZEURkyJP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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "- The majority of restaurants received ratings ranging from 3.5 to 4."
      ],
      "metadata": {
        "id": "mUx2cdMBs7kQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Online Order vs Rating\n",
        "sns.barplot(x='online_order', y='rate', data=data)\n",
        "plt.title(\"Impact of Online Ordering on Ratings\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 472
        },
        "id": "7SZFAEwHljNZ",
        "outputId": "1fc7e3d1-70a3-4b9c-8f2b-97bcf4a10ac0"
      },
      "execution_count": 200,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjcAAAHHCAYAAABDUnkqAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAPYdJREFUeJzt3Xt8j/X/x/Hnx8ZnbDZz2hxmDnNmDtNhc5g0zSFZB8q3mkkqUaT4thJGWUgokZJWSjqJXyXStHwd8kUIISRUNhKbDcP2/v3RbZ+vj23MzD7b1eN+u123W9f7el/vz+v67POxZ9f1vq7ZjDFGAAAAFlHG1QUAAAAUJcINAACwFMINAACwFMINAACwFMINAACwFMINAACwFMINAACwFMINAACwFMINAACwFMINUALNnz9fTZo0UdmyZVWpUiWX1WGz2TRu3DjHekJCgmw2m3799VeX1XQtJSUlyWazKSkpqUjHHTdunGw2W5GO+U9Xt25dxcTEuLoMlFCEGxSrnF+OGzdudHUpV23p0qVOv/iLyq5duxQTE6MGDRrozTff1BtvvHHZfdasWaPbb79dfn5+stvtqlu3rh5++GEdPHiwyOtzJWOM5s+fr06dOqlSpUqqUKGCWrZsqfHjxysjI8PV5f2jde7cWTabzbGUL19ewcHBmj59urKzsws15tq1azVu3DidOHGiaIuF5RFugEJaunSp4uLiinzcpKQkZWdna8aMGYqJiVHfvn0v2f/VV19Vx44dtW3bNj322GOaNWuW7rrrLn344YcKDg7W2rVri6y2+++/X6dPn1ZgYGCRjVlQWVlZuueeexQdHS3p77Mh06dPV+vWrRUXF6cbb7xRKSkpxV5XQYwePVqnT592dRnXXO3atTV//nzNnz9f8fHx8vDw0BNPPKHnnnuuUOOtXbtWcXFxeYab3bt3680337zKimFV7q4uAICzI0eOSFKBLketWbNGw4cPV4cOHbRs2TJVqFDBsW3w4MFq37697rrrLu3YsUO+vr5XXZubm5vc3NyuepzCmDx5sj766CM99dRTmjJliqP9oYceUt++fRUVFaWYmBh99dVX+Y5hjNGZM2dUvnz54ihZGRkZ8vT0lLu7u9zdrf/PrY+Pj+677z7H+iOPPKImTZro1Vdf1fjx44v0s2O324tsLFgPZ27gcjExMfLy8tLBgwd16623ysvLS7Vq1dJrr70mSdq2bZu6dOkiT09PBQYGasGCBU7751zqWrVqlR5++GFVqVJF3t7eio6O1vHjx536LlmyRD179lTNmjVlt9vVoEEDTZgwQVlZWbnqWr9+vXr06CFfX195enoqODhYM2bMcNScU9+Fp+IvZ9asWWrevLnsdrtq1qypIUOGOP1fad26dTV27FhJUrVq1XLNebnYhAkTZLPZ9M477zgFG0lq0KCBJk+erMOHD2vOnDmO9pz3+/fff1dUVJS8vLxUrVo1PfXUU3m+DxfKa85N3bp1deutt2r16tW6/vrr5eHhofr16+vdd9/Ntf+JEyc0fPhwBQQEyG63KygoSJMmTbrsZYvTp09rypQpatSokeLj43Nt79Wrl/r3769ly5bp+++/z1Xb8uXL1a5dO5UvX97xXvz222+KioqSp6enqlevrieeeEKZmZl5vv769evVrVs3+fj4qEKFCgoPD9eaNWuc+uTMq/npp5/0r3/9S76+vurQoYPTtgvZbDYNHTpUixcvVosWLWS329W8eXMtW7Ys1+snJSWpXbt28vDwUIMGDTRnzpwrmsfz8ccfKyQkROXLl1fVqlV133336ffff3fqczWfi/x4eHjouuuu08mTJx2hXZJ+/PFHxcTEqH79+vLw8JC/v78eeOABHTt2zNFn3LhxGjlypCSpXr16ju9Yzmfv4jk3OZ/NNWvWaMSIEapWrZo8PT11++236+jRo051ZWdna9y4capZs6YqVKigm266ST/99FOuMc+dO6e4uDg1bNhQHh4eqlKlijp06KAVK1YU6v1A8SHcoETIyspS9+7dFRAQoMmTJ6tu3boaOnSoEhIS1K1bN7Vr106TJk1SxYoVFR0drf379+caY+jQodq5c6fGjRun6Ohovf/++4qKipIxxtEnISFBXl5eGjFihGbMmKGQkBCNGTNGTz/9tNNYK1asUKdOnfTTTz9p2LBhmjp1qm666SZ98cUXkqSHH35YXbt2lSTHafj58+df8hjHjRunIUOGqGbNmpo6daruvPNOzZkzR7fccovOnTsnSZo+fbpuv/12SdLs2bM1f/583XHHHXmOd+rUKSUmJqpjx46qV69enn3uvvtu2e12R90Xvt+RkZGqUqWKXnrpJYWHh2vq1KkFmt+Tl7179+quu+5S165dNXXqVPn6+iomJkY7duxwqjc8PFzvvfeeoqOj9corr6h9+/aKjY3ViBEjLjn+6tWrdfz4cf3rX//K9wxIzuWqi4919+7d6tevn7p27aoZM2aodevWOn36tG6++WYtX75cQ4cO1bPPPqv//Oc/GjVqVK5xV65cqU6dOiktLU1jx47VxIkTdeLECXXp0kX//e9/c/Xv06ePTp06pYkTJ2rQoEGXPa5HH31U99xzjyZPnqwzZ87ozjvvdPolv3nzZnXr1k3Hjh1TXFycBg4cqPHjx2vx4sWXHDtHQkKC+vbtKzc3N8XHx2vQoEFatGiROnTokOtyT1F/LiTp119/lc1mczoTuWLFCv3yyy8aMGCAXn31Vd1zzz1auHChevTo4fi+3nHHHerXr58kadq0aY7vWLVq1S75eo899pi2bt2qsWPHavDgwfr88881dOhQpz6xsbGKi4tTu3btNGXKFDVs2FCRkZG55m2NGzdOcXFxuummmzRz5kw9++yzqlOnjn744YdCvx8oJgYoRm+//baRZDZs2OBo69+/v5FkJk6c6Gg7fvy4KV++vLHZbGbhwoWO9l27dhlJZuzYsbnGDAkJMWfPnnW0T5482UgyS5YscbSdOnUqV00PP/ywqVChgjlz5owxxpjz58+bevXqmcDAQHP8+HGnvtnZ2Y7/HjJkiCnoV+jIkSOmXLly5pZbbjFZWVmO9pkzZxpJZt68eY62sWPHGknm6NGjlxxzy5YtRpIZNmzYJfsFBwebypUrO9Zz3u/x48c79WvTpo0JCQlxasvvvd6/f7+jLTAw0Egyq1atcjpeu91unnzySUfbhAkTjKenp/n555+dXuPpp582bm5u5uDBg/kew/Tp040k89lnn+Xb56+//jKSzB133JGrtmXLluU53kcffeRoy8jIMEFBQUaS+fbbb40xf/+8GzZsaCIjI51+9qdOnTL16tUzXbt2dbTl/Nz69euXq7acbReSZMqVK2f27t3raNu6dauRZF599VVHW69evUyFChXM77//7mjbs2ePcXd3v+zn7+zZs6Z69eqmRYsW5vTp0472L774wkgyY8aMcbRdyeciL+Hh4aZJkybm6NGj5ujRo2bXrl1m5MiRRpLp2bOnU9+8vocffPBBrs/RlClTcn3ecgQGBpr+/fs71nM+mxEREU4/qyeeeMK4ubmZEydOGGOMSU5ONu7u7iYqKsppvHHjxhlJTmO2atUqV+0oHThzgxLjwQcfdPx3pUqV1LhxY3l6ejpNqG3cuLEqVaqkX375Jdf+Dz30kMqWLetYHzx4sNzd3bV06VJH24VzLU6ePKk///xTHTt21KlTp7Rr1y5Jf/+f8v79+zV8+PBc814KezvvN998o7Nnz2r48OEqU+Z/X7tBgwbJ29tbX3755RWPefLkSUlSxYoVL9mvYsWKSktLy9X+yCOPOK137Ngxz/e1IJo1a6aOHTs61qtVq6bGjRs7jffxxx+rY8eO8vX11Z9//ulYIiIilJWVpVWrVuU7fkGONWfbxcdar149RUZGOrUtXbpUNWrU0F133eVoq1Chgh566CGnflu2bNGePXv0r3/9S8eOHXPUnJGRoZtvvlmrVq3KdUnt4vf1UiIiItSgQQPHenBwsLy9vR3vW1ZWlr755htFRUWpZs2ajn5BQUHq3r37ZcffuHGjjhw5okcffVQeHh6O9p49e6pJkyZ5fu6u5nOxa9cuVatWTdWqVVOTJk00ZcoU3XbbbUpISHDqd+H38MyZM/rzzz914403StJVnxV56KGHnL6nHTt2VFZWlg4cOCBJSkxM1Pnz5/Xoo4867ffYY4/lGqtSpUrasWOH9uzZc1U1ofhZf4YbSgUPD49cp5t9fHxUu3btXIHCx8cn11waSWrYsKHTupeXl2rUqOE0P2THjh0aPXq0Vq5cmeuXYGpqqiRp3759kqQWLVoU+ngulvMPa+PGjZ3ay5Urp/r16zu2X4mcX+Y5v/jzc/LkyVyhIK/329fXN8/3tSDq1KmTq+3i8fbs2aMff/wx38sKF87JuFhBjjW/AJTXJbsDBw4oKCgo12fr4p9Pzi+1/v375/u6qampTpO187tEmJfLvW9HjhzR6dOnFRQUlKtfXm0Xy+9zJ0lNmjTR6tWrndqu9nNRt25dvfnmm8rOzta+ffv0wgsv6OjRo07BSpL++usvxcXFaeHChbl+7jnfw8K6+D3N+dnkHEPOe3Lx+1e5cuVck+7Hjx+v3r17q1GjRmrRooW6deum+++/X8HBwVdVI649wg1KhPzuosiv3Vwwj6agTpw4ofDwcHl7e2v8+PFq0KCBPDw89MMPP+jf//53oZ/F4SpBQUFyd3fXjz/+mG+fzMxM7d69W+3atXNqL+o7ngryc8rOzlbXrl3znNciSY0aNcp3/KZNm0r6eyJqVFRUnn1y3odmzZo5tV/NnVE5n4kpU6aodevWefbx8vIq9OsV5ee7KFzt58LT01MRERGO9fbt26tt27Z65pln9Morrzja+/btq7Vr12rkyJFq3bq1vLy8lJ2drW7dul3197Ao39NOnTpp3759WrJkib7++mvNnTtX06ZN0+uvv+50phklD+EGlrFnzx7ddNNNjvX09HQdPnxYPXr0kPT3HSfHjh3TokWL1KlTJ0e/iycn51wm2L59u9M/1Be7kktUOc+F2b17t+rXr+9oP3v2rPbv33/J18mPp6enbrrpJq1cuVIHDhzI89kzH330kTIzM3Xrrbde8fhFrUGDBkpPTy/UsXbo0EGVKlXSggUL9Oyzz+b5Cyzn7qyCHGtgYKC2b98uY4zTz3H37t25apYkb2/vQtV9tapXry4PDw/t3bs317a82i524eeuS5cuTtt27959zZ9XFBwcrPvuu09z5szRU089pTp16uj48eNKTExUXFycxowZ4+ib16Wfa/FU55xj3rt3r9NZtmPHjuV5hqpy5coaMGCABgwYoPT0dHXq1Enjxo0j3JRwzLmBZbzxxhuOu46kv+82On/+vGNuQs4vxAv/D+7s2bOaNWuW0zht27ZVvXr1NH369Fx3k1y4r6enpyQV6OmpERERKleunF555RWnMd566y2lpqaqZ8+eBTvIi4wePVrGGMXExOR6SNz+/fs1atQo1ahRQw8//HChxi9Kffv21bp167R8+fJc206cOKHz58/nu2+FChX01FNPaffu3Xr22Wdzbf/yyy+VkJCgyMhIx9yNS+nRo4f++OMPffLJJ462U6dO5borKCQkRA0aNNBLL72k9PT0XONcfItxUXNzc1NERIQWL16sP/74w9G+d+/eSz7PJ0e7du1UvXp1vf766063uX/11VfauXNnoT93V2LUqFE6d+6cXn75ZUl5fw+lv+8UvNiVfMcK6uabb5a7u7tmz57t1D5z5sxcfS+8a036+yxdUFBQvo8MQMnBmRtYxtmzZ3XzzTerb9++2r17t2bNmqUOHTrotttukySFhYXJ19dX/fv31+OPPy6bzab58+fn+ke2TJkymj17tnr16qXWrVtrwIABqlGjhnbt2qUdO3Y4fjmHhIRIkh5//HFFRkbKzc1N99xzT561VatWzXH7abdu3XTbbbc5arzuuuucHnx2JTp16qSXXnpJI0aMUHBwsGJiYhy15sx9WLp0aZE8wO9qjRw5Uv/3f/+nW2+9VTExMQoJCVFGRoa2bdumTz75RL/++quqVq2a7/5PP/20Nm/erEmTJmndunW68847Vb58ea1evVrvvfeemjZtqnfeeadAtQwaNEgzZ85UdHS0Nm3apBo1amj+/Pm5nhVUpkwZzZ07V927d1fz5s01YMAA1apVS7///ru+/fZbeXt76/PPP7+q9+Vyxo0bp6+//lrt27fX4MGDlZWVpZkzZ6pFixbasmXLJfctW7asJk2apAEDBig8PFz9+vVTSkqKZsyYobp16+qJJ564prVLf18m7NGjh+bOnavnnntOVapUUadOnTR58mSdO3dOtWrV0tdff53n4x1yvmPPPvus7rnnHpUtW1a9evVyhJ7C8PPzczze4bbbblO3bt20detWffXVV6patarT2aJmzZqpc+fOCgkJUeXKlbVx40Z98sknuW4tRwnkoru08A+V363gnp6eufqGh4eb5s2b52oPDAx0uj0zZ8zvvvvOPPTQQ8bX19d4eXmZe++91xw7dsxp3zVr1pgbb7zRlC9f3tSsWdOMGjXKLF++3On23xyrV682Xbt2NRUrVjSenp4mODjY6Rbd8+fPm8cee8xUq1bN2Gy2At0WPnPmTNOkSRNTtmxZ4+fnZwYPHpzrdvOC3gp+oVWrVpnevXubqlWrmrJly5o6deqYQYMGmV9//TVX3/ze7/xuVy7IreB53S4bHh5uwsPDndpOnjxpYmNjTVBQkClXrpypWrWqCQsLMy+99JLTbfz5ycrKMm+//bZp37698fb2Nh4eHqZ58+YmLi7OpKen5+qfX23GGHPgwAFz2223mQoVKpiqVauaYcOGmWXLluX5Wdi8ebO54447TJUqVYzdbjeBgYGmb9++JjEx0dHnUj+3/N7bIUOG5FnzhbcjG2NMYmKiadOmjSlXrpxp0KCBmTt3rnnyySeNh4dHfm+Vkw8//NC0adPG2O12U7lyZXPvvfea3377zanPlXwu8pLf99UYY5KSkpw+S7/99pu5/fbbTaVKlYyPj4/p06eP+eOPP3J93oz5+xECtWrVMmXKlHH67OV3K/iF/7YYY8y3336b62d6/vx589xzzxl/f39Tvnx506VLF7Nz505TpUoV88gjjzj6Pf/88+b66683lSpVMuXLlzdNmjQxL7zw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STp48KDKlPnfyaXjx49r0KBBSk5Olq+vr0JCQrR27dp8JyADAIB/HpeGm7feeuuS25OSkpzWp02bpmnTpl3DigAAQGlX4ubcAAAAXA3CDQAAsBTCDQAAsBSXP6EYAIArZdzKKjW4n9M6kINwAwAofWw2HtqHfHFZCgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWArhBgAAWIpLw83s2bMVHBwsb29veXt7KzQ0VF999dUl9/n444/VpEkTeXh4qGXLllq6dGkxVQsAAEoDl4ab2rVr68UXX9SmTZu0ceNGdenSRb1799aOHTvy7L927Vr169dPAwcO1ObNmxUVFaWoqCht3769mCsHAAAllUvDTa9evdSjRw81bNhQjRo10gsvvCAvLy99//33efafMWOGunXrppEjR6pp06aaMGGC2rZtq5kzZxZz5QAAoKQqMXNusrKytHDhQmVkZCg0NDTPPuvWrVNERIRTW2RkpNatW5fvuJmZmUpLS3NaAACAdbk83Gzbtk1eXl6y2+165JFH9Nlnn6lZs2Z59k1OTpafn59Tm5+fn5KTk/MdPz4+Xj4+Po4lICCgSOsHAAAli8vDTePGjbVlyxatX79egwcPVv/+/fXTTz8V2fixsbFKTU11LIcOHSqysQEAQMnj7uoCypUrp6CgIElSSEiINmzYoBkzZmjOnDm5+vr7+yslJcWpLSUlRf7+/vmOb7fbZbfbi7ZoAABQYrn8zM3FsrOzlZmZmee20NBQJSYmOrWtWLEi3zk6AADgn8elZ25iY2PVvXt31alTRydPntSCBQuUlJSk5cuXS5Kio6NVq1YtxcfHS5KGDRum8PBwTZ06VT179tTChQu1ceNGvfHGG648DAAAUIK4NNwcOXJE0dHROnz4sHx8fBQcHKzly5era9eukqSDBw+qTJn/nVwKCwvTggULNHr0aD3zzDNq2LChFi9erBYtWrjqEAAAQAnj0nDz1ltvXXJ7UlJSrrY+ffqoT58+16giAABQ2pW4OTcAAABXg3ADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAsxaXhJj4+Xtddd50qVqyo6tWrKyoqSrt3777kPgkJCbLZbE6Lh4dHMVUMAABKOpeGm++++05DhgzR999/rxUrVujcuXO65ZZblJGRccn9vL29dfjwYcdy4MCBYqoYAACUdO6ufPFly5Y5rSckJKh69eratGmTOnXqlO9+NptN/v7+17o8AABQCpWoOTepqamSpMqVK1+yX3p6ugIDAxUQEKDevXtrx44d+fbNzMxUWlqa0wIAAKyrxISb7OxsDR8+XO3bt1eLFi3y7de4cWPNmzdPS5Ys0Xvvvafs7GyFhYXpt99+y7N/fHy8fHx8HEtAQMC1OgQAAFAClJhwM2TIEG3fvl0LFy68ZL/Q0FBFR0erdevWCg8P16JFi1StWjXNmTMnz/6xsbFKTU11LIcOHboW5QMAgBLCpXNucgwdOlRffPGFVq1apdq1a1/RvmXLllWbNm20d+/ePLfb7XbZ7faiKBMAAJQCLj1zY4zR0KFD9dlnn2nlypWqV6/eFY+RlZWlbdu2qUaNGtegQgAAUNq49MzNkCFDtGDBAi1ZskQVK1ZUcnKyJMnHx0fly5eXJEVHR6tWrVqKj4+XJI0fP1433nijgoKCdOLECU2ZMkUHDhzQgw8+6LLjAAAAJYdLw83s2bMlSZ07d3Zqf/vttxUTEyNJOnjwoMqU+d8JpuPHj2vQoEFKTk6Wr6+vQkJCtHbtWjVr1qy4ygYAACWYS8ONMeayfZKSkpzWp02bpmnTpl2jigAAQGlXYu6WAgAAKAqEGwAAYCmEGwAAYCmEGwAAYCmEGwAAYCmEGwAAYCmEGwAAYCmEGwAAYCmEGwAAYCmEGwAAYCmEGwAAYCmEGwAAYCmEGwAAYCmEGwAAYCmEGwAAYCmEGwAAYCmEGwAAYCmEGwAAYCmEGwAAYCmEGwAAYCmF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drvsdnsxVgQAAFypVF2WysuWLVtUo0YNV5cBAABKCJeeuUlPT9fevXsd6/v379eWLVtUuXJl1alTR7Gxsfr999/17rvvSpKmT5+uevXqqXnz5jpz5ozmzp2rlStX6uuvv3bVIQAAgBLGpeFm48aNuummmxzrOXNj+vfvr4SEBB0+fFgHDx50bD979qyefPJJ/f7776pQoYKCg4P1zTffOI0BAAD+2Vwabjp37ixjTL7bExISnNZHjRqlUaNGXeOqAABAaVbq59wAAABciHADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAsxaXhZtWqVerVq5dq1qwpm82mxYsXX3afpKQktW3bVna7XUFBQUpISLjmdQIAgNLDpeEmIyNDrVq10muvvVag/vv371fPnj110003acuWLRo+fLgefPBBLV++/BpXCgAASgt3V7549+7d1b179wL3f/3111WvXj1NnTpVktS0aVOtXr1a06ZNU2Rk5LUqEwAAlCKlas7NunXrFBER4dQWGRmpdevW5btPZmam0tLSnBYAAGBdpSrcJCcny8/Pz6nNz89PaWlpOn36dJ77xMfHy8fHx7EEBAQUR6kAAMBFSlW4KYzY2FilpqY6lkOHDrm6JAAAcA25dM7NlfL391dKSopTW0pKiry9vVW+fPk897Hb7bLb7cVRHgAAKAFK1Zmb0NBQJSYmOrWtWLFCoaGhLqoIAACUNC4NN+np6dqyZYu2bNki6e9bvbds2aKDBw9K+vuSUnR0tKP/I488ol9++UWjRo3Srl27NGvWLH300Ud64oknXFE+AAAogVwabjZu3Kg2bdqoTZs2kqQRI0aoTZs2GjNmjCTp8OHDjqAjSfXq1dOXX36pFStWqFWrVpo6darmzp3LbeAAAMDBpXNuOnfuLGNMvtvzevpw586dtXnz5mtYFQAAKM1K1ZwbAACAyyHcAAAASyHcAAAASyHcAAAASyHcAAAA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aN+/f79GjRqlV199VbVr13ZhhQCKioeHhyZNmqTjx4+7uhSUEoQblFoBAQGaMWOGnnrqKe3fv1/GGA0cOFC33HKL2rRpo+7du8vLy0t+fn66//779eeffzr2/eSTT9SyZUuVL19eVapUUUREhDIyMlx4NADyExERIX9/f8eT6vPy6aefqnnz5rLb7apbt66mTp1ajBWipCHcoFTr37+/br75Zj3wwAOaOXOmtm/frjlz5qhLly5q06aNNm7cqGXLliklJUV9+/aVJB0+fFj9+vXTAw88oJ07dyopKUl33HGHeOQTUDK5ublp4sSJevXVV/O83Lxp0yb17dtX99xzj7Zt26Zx48bpueeeU0JCQvEXixKBh/ih1Dty5IiaN2+uv/76S59++qm2b9+u//znP1q+fLmjz2+//aaAgADt3r1b6enpCgkJ0a+//qrAwEAXVg7gcmJiYnTixAktXrxYoaGhatasmd566y0tXrxYt99+u4wxuvfee3X06FF9/fXXjv1GjRqlL7/8Ujt27HBh9XAVztyg1KtevboefvhhNW3aVFFRUdq6dau+/fZbeXl5OZYmTZpIkvbt26dWrVrp5ptvVsuWLdWnTx+9+eabXMsHSoFJkybpnXfe0c6dO53ad+7cqfbt2zu1tW/fXnv27FFWVlZxlogSgnADS3B3d5e7+99/BzY9PV29evXSli1bnJY9e/aoU6dOcnNz04oVK/TVV1+pWbNmevXVV9W4cWPt37/fxUcB4FI6deqkyMhIxcbGuroUlHAu/6vgQFFr27atPv30U9WtW9cReC5ms9nUvn17tW/fXmPGjFFgYKA+++wzjRgxopirBXAlXnzxRbVu3VqNGzd2tDVt2lRr1qxx6rdmzRo1atRIbm5uxV0iSgDO3MByhgwZor/++kv9+vXThg0btG/fPi1fvlwDBgxQVlaW1q9fr4kTJ2rjxo06ePCgFi1apKNHj6pp06auLh3AZbRs2VL33nuvXnnlFUfbk08+qcTERE2YMEE///yz3nnnHc2cOVNPPfWUCyuFKxFuYDk1a9bUmjVrlJWVpVtuuUUtW7bU8OHDValSJZUpU0be3t5atWqVevTooUaNGmn06NGaOnWqunfv7urSARTA+PHjlZ2d7Vhv27atPvroIy1cuFAtWrTQmDFjNH78eMXExLiuSLgUd0sBAABL4cwNAACwFMINAACwFMINAACwFMINAACwFMINAACwFMINAACwFMINAACwFMINgGIzbtw4tW7d2rEeExOjqKgol9VzNS4+FgAlB39bCoDLzJgxQzxHFEBRI9wAcBkfHx9Xl3BZ586dU9myZUvd2MA/GZelABRYZmamHn/8cVWvXl0eHh7q0KGDNmzYIElKSkqSzWZTYmKi2rVrpwoVKigsLEy7d+/Od7yLL0t17txZjz/+uEaNGqXKlSvL399f48aNc9rnxIkTevDBB1WtWjV5e3urS5cu2rp1a4GPYfbs2WrQoIHKlSunxo0ba/78+U7bbTabZs+erdtuu02enp564YUXJP3916j9/PxUsWJFDRw4UGfOnMk19ty5c9W0aVN5eHioSZMmmjVrlmPbr7/+KpvNpg8//FDh4eHy8PDQ+++/X+C6AVwBAwAF9Pjjj5uaNWuapUuXmh07dpj+/fsbX19fc+zYMfPtt98aSeaGG24wSUlJZseOHaZjx44mLCzMsf/YsWNNq1atHOv9+/c3vXv3dqyHh4cbb29vM27cOPPzzz+bd955x9hsNvP11187+kRERJhevXqZDRs2mJ9//tk8+eSTpkqVKubYsWOXrX/RokWmbNmy5rXXXjO7d+82U6dONW5ubmblypWOPpJM9erVzbx588y+ffvMgQMHzIcffmjsdruZO3eu2bVrl3n22WdNxYoVnY7lvffeMzVq1DCffvqp+eWXX8ynn35qKleubBISEowxxuzfv99IMnXr1nX0+eOPPwrxUwBwOYQbAAWSnp5uypYta95//31H29mzZ03NmjXN5MmTHeHmm2++cWz/8ssvjSRz+vRpY0zBwk2HDh2cXve6664z//73v40xxvznP/8x3t7e5syZM059GjRoYObMmXPZYwgLCzODBg1yauvTp4/p0aOHY12SGT58uFOf0NBQ8+ijjzq13XDDDU7H0qBBA7NgwQKnPhMmTDChoaHGmP+Fm+nTp1+2TgBXh8tSAApk3759OnfunNq3b+9oK1u2rK6//nrt3LnT0RYcHOz47xo1akiSjhw5UuDXuXD/nDFy9t+6davS09NVpUoVeXl5OZb9+/dr3759lx17586dTvVLUvv27Z3ql6R27drl2u+GG25wagsNDXX8d0ZGhvbt26eBAwc61fX888/nquvisQEUPSYUAyhSF06QtdlskqTs7OxC7Z8zRs7+6enpqlGjhpKSknLtV6lSpSsvNh+enp5X1D89PV2S9Oabb+YKQW5ublc1NoArx5kbAAWSMwl3zZo1jrZz585pw4YNatasWbHU0LZtWyUnJ8vd3V1BQUFOS9WqVS+7f9OmTZ3ql6Q1a9Zctv6mTZtq/fr1Tm3ff/+947/9/PxUs2ZN/fLLL7nqqlev3hUcIYCiwJkbAAXi6empwYMHa+TIkapcubLq1KmjyZMn69SpUxo4cOAV3bFUWBEREQoNDVVUVJQmT56sRo0a6Y8//tCXX36p22+//bKXfEaOHKm+ffuqTZs2ioiI0Oeff65Fixbpm2++ueR+w4YNU0xMjNq1a6f27dvr/fff144dO1S/fn1Hn7i4OD3++OPy8fFRt27dlJmZqY0bN+r48eMaMWJEkRw/gIIh3AAosBdffFHZ2dm6//77dfLkSbVr107Lly+Xr69vsby+zWbT0qVL9eyzz2rAgAE6evSo/P391alTJ/n5+V12/6ioKM2YMUMvvfSShg0bpnr16untt99W586dL7nf3XffrX379mnUqFE6c+aM7rzzTg0ePFjLly939HnwwQdVoUIFTZkyRSNHjpSnp6datmyp4cOHX+VRA7hSNmN4PCgAALAO5twAAABLIdwAsIzmzZs73Yp94cLTgIF/Di5LAbCMAwcO6Ny5c3luy/nTCQCsj3ADAAAshctSAADAUgg3AADAUgg3AADAUgg3AADAUgg3AADAUgg3AADAUgg3AADAUgg3AADAUv4fAVabJR7JYbEAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Offline orders received lower ratings in comparison to online orders, which obtained excellent ratings."
      ],
      "metadata": {
        "id": "Lb0tQE3NmxHd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Table Booking Impact\n",
        "plt.figure(figsize=(6, 4))\n",
        "sns.barplot(x='book_table', y='rate', data=data)\n",
        "plt.title(\"Impact of Table Booking on Ratings\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 410
        },
        "id": "eWic_8_rt7ip",
        "outputId": "9df4091d-ba95-456f-9122-83cd541ed66f"
      },
      "execution_count": 185,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 600x400 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAgsAAAGJCAYAAAAEz3CAAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAALqxJREFUeJzt3Xl8TPf+x/H3yDKJRBZqF4l9X8rtgsaaiqXoRimVaKvaWou20trSarVcSi2pqq0upbeUVmmq1vKwtxS1tBpLW4oiJEia5Pv7ozfzMyaOiDDB6/l4zOPhfOd7zvnMMZN5zznf74zNGGMEAABwBfncXQAAAMjbCAsAAMASYQEAAFgiLAAAAEuEBQAAYImwAAAALBEWAACAJcICAACwRFgAAACWCAvAdZo9e7YqV64sLy8vBQUF3fD92Ww29erV66r9Zs6cKZvNpoMHD97wmm6Gxo0bq3r16lftFxYWpujo6Btf0B1i9erVstlsWr16tbtLgRsRFnBFmW82W7dudXcp123p0qUaPnx4rm937969io6OVrly5TR16lR9+OGHLn0OHjwom82WrVtefmPPfNO49FawYEHdf//9mjNnjrvLu2Nc/nzKly+fChYsqJYtW2rDhg053u7kyZM1c+bM3CsUtxVPdxcA3AxLly7VpEmTcj0wrF69WhkZGRo/frzKly+fZZ/ChQtr9uzZTm1jxozRb7/9pvfee8+lb17Xp08f3XPPPZKkv/76S/Pnz1eXLl105swZ9ezZ083VSfv27VO+fLf/56BOnTqpVatWSk9P1/79+zV58mQ1adJEW7ZsUY0aNa55e5MnT9Zdd93lclamYcOGunDhgry9vXOpctyKCAvAdTh+/LgkWV5+8PPzU5cuXZza5s2bp9OnT7u03wrCw8P1+OOPO5ZfeOEFlS1bVnPnzs0TYcFut7u7hJuiTp06Ts+f8PBwtWzZUnFxcZo8eXKu7Sdfvnzy8fHJte3h1nT7x2/kqujoaPn7++vw4cN66KGH5O/vr5IlS2rSpEmSpJ07d6pp06by8/NTaGio5s6d67R+5qWNtWvXqkePHipUqJACAgLUtWtXnT592qnv4sWL1bp1a5UoUUJ2u13lypXTm2++qfT0dJe6Nm3apFatWik4OFh+fn6qWbOmxo8f76g5s75LT99ezeTJk1WtWjXZ7XaVKFFCPXv21JkzZxz3h4WFadiwYZL+OSNgs9mu68zFv//9b9WvX1+FChWSr6+v6tatq88+++yK/efMmaNKlSrJx8dHdevW1dq1a7O1n2XLlik8PFx+fn4qUKCAWrdurd27d+e4bm9vbwUHB8vT0/mzR1pamt58802VK1dOdrtdYWFheu2115SSkuKyjasd6yv55ptvlD9/fnXq1ElpaWmSXMcsZD7n1q9fr/79+6tw4cLy8/PTI488ohMnTjhtLyMjQ8OHD1eJEiWUP39+NWnSRD/99FO2x0EkJydrwIABCgkJkd1uV6VKlfTvf/9bl/+4b+a4k0WLFql69eqy2+2qVq2avv7666vu40rCw8MlSQcOHHBqnzFjhpo2baoiRYrIbreratWqiouLc+oTFham3bt3a82aNY7XR+PGjSVlPWYhc/zITz/9pCZNmih//vwqWbKkRo0a5VLXoUOH1LZtW/n5+alIkSJ66aWXFB8f77LNn3/+WY899piKFSsmHx8flSpVSh07dlRiYmKOjwlyD2cWcM3S09PVsmVLNWzYUKNGjdKcOXPUq1cv+fn56fXXX1fnzp316KOP6oMPPlDXrl1Vr149lSlTxmkbvXr1UlBQkIYPH659+/YpLi5Ohw4dcvxhkv75I+/v76/+/fvL399fK1eu1NChQ3X27FmNHj3asa3ly5froYceUvHixdW3b18VK1ZMe/bs0ZIlS9S3b1/16NFDf/zxh5YvX+5yOeBKhg8frtjYWEVEROiFF15w1LhlyxatX79eXl5eGjdunD7++GN9/vnniouLk7+/v2rWrJnj4zp+/Hi1bdtWnTt3VmpqqubNm6f27dtryZIlat26tVPfNWvWaP78+erTp4/sdrsmT56sFi1aaPPmzZaDAGfPnq2oqChFRkbq3Xff1fnz5xUXF6cHHnhAP/zwg8LCwq5a57lz53Ty5ElJ0qlTpzR37lzt2rVL06ZNc+r37LPPatasWXr88cc1YMAAbdq0SSNHjtSePXv0+eefO/pl51hnZcmSJXr88cf1xBNPaPr06fLw8LCsu3fv3goODtawYcN08OBBjRs3Tr169dL8+fMdfWJiYjRq1Ci1adNGkZGR2rFjhyIjI3Xx4sWrHhdjjNq2batVq1bpmWeeUe3atRUfH6+XX35Zv//+u8slp3Xr1mnhwoV68cUXVaBAAb3//vt67LHHdPjwYRUqVOiq+7tc5niX4OBgp/a4uDhVq1ZNbdu2laenp7788ku9+OKLysjIcJwJGjdunHr37i1/f3+9/vrrkqSiRYta7u/06dNq0aKFHn30UXXo0EGfffaZXn31VdWoUUMtW7aU9E94atq0qY4ePep4bc6dO1erVq1y2lZqaqoiIyOVkpKi3r17q1ixYvr999+1ZMkSnTlzRoGBgdd8PJDLDHAFM2bMMJLMli1bHG1RUVFGknn77bcdbadPnza+vr7GZrOZefPmOdr37t1rJJlhw4a5bLNu3bomNTXV0T5q1CgjySxevNjRdv78eZeaevToYfLnz28uXrxojDEmLS3NlClTxoSGhprTp0879c3IyHD8u2fPnia7T/fjx48bb29v07x5c5Oenu5onzhxopFkpk+f7mgbNmyYkWROnDiRrW1nat26tQkNDXVqu/zxpqammurVq5umTZs6tUsykszWrVsdbYcOHTI+Pj7mkUcecbRlHuuEhARjjDHnzp0zQUFBpnv37k7bO3bsmAkMDHRpv9yqVasc+770li9fPvPWW2859d2+fbuRZJ599lmn9oEDBxpJZuXKlcaYazvWjRo1MtWqVTPGGLNgwQLj5eVlunfv7rSeMcaEhoaaqKgol+MQERHh9Jx46aWXjIeHhzlz5ozjOHh6epqHH37YaXvDhw83kpy2mZVFixYZSWbEiBFO7Y8//rix2Wzml19+cbRJMt7e3k5tO3bsMJLMhAkTLPeTkJBgJJnY2Fhz4sQJc+zYMfPdd9+Ze+65x0gy//3vf536Z/U6ioyMNGXLlnVqq1atmmnUqJFL38z/91WrVjnaGjVqZCSZjz/+2NGWkpJiihUrZh577DFH25gxY4wks2jRIkfbhQsXTOXKlZ22+cMPP2RZO/IOLkMgR5599lnHv4OCglSpUiX5+fmpQ4cOjvZKlSopKChIv/76q8v6zz33nNMnxhdeeEGenp5aunSpo83X19fx78xPs+Hh4Tp//rz27t0rSfrhhx+UkJCgfv36uYwbyM6lhqx8++23Sk1NVb9+/ZwGynXv3l0BAQH66quvcrTdq7n08Z4+fVqJiYkKDw/X999/79K3Xr16qlu3rmO5dOnSateuneLj47O8TCP9cwbmzJkz6tSpk06ePOm4eXh46L777nP5tHclQ4cO1fLly7V8+XLNnz9fnTp10uuvv+647CPJ8f/Yv39/p3UHDBggSY5jmJNj/cknn+iJJ55Qjx49NGXKlGwPZnzuueecnhPh4eFKT0/XoUOHJEkrVqxQWlqaXnzxRaf1evfuna3tL126VB4eHurTp49T+4ABA2SM0bJly5zaIyIiVK5cOcdyzZo1FRAQkOXrJSvDhg1T4cKFVaxYMYWHh2vPnj0aM2aM03gSyfl5lZiYqJMnT6pRo0b69ddfr+sUv7+/v9OYCW9vb917771O9X/99dcqWbKk2rZt62jz8fFR9+7dnbaVeeYgPj5e58+fz3FNuHG4DIFr5uPj4zJqPzAwUKVKlXJ5gw4MDHQZiyBJFSpUcFr29/dX8eLFnaYO7t69W4MHD9bKlSt19uxZp/6Zf+Qyr89mZ/59dmW+eVSqVMmp3dvbW2XLlnXcn9uWLFmiESNGaPv27U7X9bMKPZcfP0mqWLGizp8/rxMnTqhYsWIu9//888+SpKZNm2a5/4CAgGzVWaNGDUVERDiWO3TooMTERA0aNEhPPvmkChcurEOHDilfvnwuM0SKFSumoKAgxzG81mOdkJCgLl26qH379powYUK26s1UunRpp+XM0/WZz8/MfV1ec8GCBV1O7Wfl0KFDKlGihAoUKODUXqVKFaftX6mezJqyer1k5bnnnlP79u118eJFrVy5Uu+//36WQXH9+vUaNmyYNmzY4PJGnJiYmONT/Fm93oODg/Xjjz86lg8dOqRy5cq59Lv8GJcpU0b9+/fX2LFjNWfOHIWHh6tt27bq0qULlyDyCMICrtmVrg1fqd1cNrgrO86cOaNGjRopICBAb7zxhsqVKycfHx99//33evXVV5WRkXHN28zLvvvuO7Vt21YNGzbU5MmTVbx4cXl5eWnGjBkug0RzKvOYzZ49O8swcfkAxWvRrFkzLVmyRJs3b3YaX5HTsztXUrx4cRUvXlxLly7V1q1b9a9//Svb6+bm8zM3XG89FSpUcIS2hx56SB4eHho0aJCaNGniOC4HDhxQs2bNVLlyZY0dO1YhISHy9vbW0qVL9d57713X6yi3j+eYMWMUHR2txYsX65tvvlGfPn00cuRIbdy4UaVKlcpxncgdXIaAW2R+ys2UlJSko0ePOgbYrV69Wn/99Zdmzpypvn376qGHHlJERITLJ7zM07i7du2y3N+1vGmFhoZK+me+/qVSU1OVkJDguD83LViwQD4+PoqPj9fTTz+tli1bOn16v9zlx0+S9u/fr/z581/xuxoyj1WRIkUUERHhcssc/Z4TmTMRkpKSJP1zDDMyMlzq/PPPP3XmzBnHMbzWY+3j46MlS5aoQoUKatGixXXN4rhc5r5++eUXp/a//vorW5/2Q0ND9ccff+jcuXNO7ZmXzG7E8+ZSr7/+ugoUKKDBgwc72r788kulpKToiy++UI8ePdSqVStFREQ4XZrIlNvBTvrnMR84cMAlQFx+jDPVqFFDgwcP1tq1a/Xdd9/p999/1wcffJDrdeHaERbgFh9++KH+/vtvx3JcXJzS0tIco6gzP7Vc+kcmNTXVZf54nTp1VKZMGY0bN85lqt2l6/r5+UlStqbjRUREyNvbW++//77TNqZNm6bExESXmQm5wcPDQzabzek08sGDB7Vo0aIs+2/YsMFpLMORI0e0ePFiNW/e/Iqf+CIjIxUQEKC3337b6dhnunwa4bVYsmSJJKlWrVqSpFatWkn6Z5T9pcaOHStJjmOYk2MdGBio+Ph4FSlSRA8++KDLVMGcatasmTw9PV2mFU6cODFb62d+QdLl/d977z3ZbDbHc/tGCQoKUo8ePRQfH6/t27dLyvp1lJiYqBkzZris7+fnl63Xx7WIjIzU77//ri+++MLRdvHiRU2dOtWp39mzZx2BM1ONGjWUL1++LKfa4ubjMgTcIjU1Vc2aNVOHDh20b98+TZ48WQ888IBjIFT9+vUVHBysqKgo9enTRzabTbNnz3b5hJIvXz7FxcWpTZs2ql27trp166bixYtr79692r17t+Lj4yXJMRiwT58+ioyMlIeHhzp27JhlbYULF1ZMTIxiY2PVokULtW3b1lHjPffcc0O+SKl169YaO3asWrRooSeffFLHjx/XpEmTVL58eadrwJmqV6+uyMhIp6mTkhQbG3vFfQQEBCguLk5PPfWU6tSpo44dO6pw4cI6fPiwvvrqKzVo0CBbb4zfffedYyrhqVOn9MUXX2jNmjXq2LGjKleuLOmf0BAVFaUPP/zQcUlp8+bNmjVrlh5++GE1adJEUs6P9V133aXly5frgQceUEREhNatW6eSJUtetXYrRYsWVd++fTVmzBi1bdtWLVq00I4dO7Rs2TLdddddV/3k3aZNGzVp0kSvv/66Dh48qFq1aumbb77R4sWL1a9fP6fBjDdK3759NW7cOL3zzjuaN2+emjdvLm9vb7Vp00Y9evRQUlKSpk6dqiJFiujo0aNO69atW1dxcXEaMWKEypcvryJFilxxfEt29ejRQxMnTlSnTp3Ut29fFS9eXHPmzHF8yVPmMV25cqV69eql9u3bq2LFikpLS9Ps2bPl4eGhxx577LpqQC5xzyQM3AquNHXSz8/Ppe+l09ouFRoaalq3bu2yzTVr1pjnnnvOBAcHG39/f9O5c2fz119/Oa27fv16c//99xtfX19TokQJ88orr5j4+HiXaVzGGLNu3Trz4IMPmgIFChg/Pz9Ts2ZNpyloaWlppnfv3qZw4cLGZrNlaxrlxIkTTeXKlY2Xl5cpWrSoeeGFF1ymZ+bm1Mlp06aZChUqGLvdbipXrmxmzJjh2P6lJJmePXua//znP47+d999t8sxuXzqZKZVq1aZyMhIExgYaHx8fEy5cuVMdHS001TMrGQ1ddLb29tUrlzZvPXWW05TYY0x5u+//zaxsbGmTJkyxsvLy4SEhJiYmBjHtNdLZedYZ/Uc++WXX0zx4sVNlSpVHP8HV5o6eenz+NLHc+lxS0tLM0OGDDHFihUzvr6+pmnTpmbPnj2mUKFC5vnnn7c8Psb8Mz31pZdeMiVKlDBeXl6mQoUKZvTo0U5TNo35///Dy11ee1Yyp06OHj06y/ujo6ONh4eHY1rmF198YWrWrGl8fHxMWFiYeffdd8306dNdnhvHjh0zrVu3NgUKFDCSHNMorzR1MqvXe1RUlMvz+tdffzWtW7c2vr6+pnDhwmbAgAFmwYIFRpLZuHGjo8/TTz9typUrZ3x8fEzBggVNkyZNzLfffmt5LHDz2Ixx0+ge3JFmzpypbt26acuWLdc0OA1wlzNnzig4OFgjRoxwfGERrs+4ceP00ksv6bfffrvuM0K4ORizAAD/c+HCBZe2zHEX1zMA9E52+TG9ePGipkyZogoVKhAUbiGMWQCA/5k/f75mzpypVq1ayd/fX+vWrdMnn3yi5s2bq0GDBu4u75b06KOPqnTp0qpdu7YSExP1n//8R3v37uVnzW8xhAUA+J+aNWvK09NTo0aN0tmzZx2DHkeMGOHu0m5ZkZGR+uijjzRnzhylp6eratWqmjdvnp544gl3l4ZrwJgFAABgiTELAADAEmEBAABYuqXHLGRkZOiPP/5QgQIFbshXlQIAcLsyxujcuXMqUaLEVX+99ZYOC3/88YdCQkLcXQYAALesI0eOXPXHum7psJD5U7BHjhzJ9s/rAgCAf36TIyQkxOVn1bNyS4eFzEsPAQEBhAUAAHIgO5fxGeAIAAAsERYAAIAlwgIAALBEWAAAAJYICwAAwBJhAQAAWCIsAAAAS4QFAABgibAAAAAs3dLf4IjbhzFGycnJjmU/Pz9+HAwA8gjCAvKE5ORktWvXzrG8ePFi+fv7u7EiAEAmLkMAAABLhAUAAGCJsAAAACwRFgAAgCXCAgAAsERYAAAAlggLAADAEmEBAABYIiwAAABLhAUAAGCJsAAAACwRFgAAgCXCAgAAsMSvTlqo+/LH7i7hjmFLS1XgJcuNh8yT8fR2Wz13km2ju7q7BAB5HGcWAACAJcICAACwRFgAAACWCAsAAMASYQEAAFgiLAAAAEuEBQAAYImwAAAALOWZsPDOO+/IZrOpX79+7i4FAABcIk+EhS1btmjKlCmqWbOmu0sBAACXcXtYSEpKUufOnTV16lQFBwdb9k1JSdHZs2edbgAA4MZye1jo2bOnWrdurYiIiKv2HTlypAIDAx23kJCQm1AhAAB3NreGhXnz5un777/XyJEjs9U/JiZGiYmJjtuRI0ducIUAAMBtvzp55MgR9e3bV8uXL5ePj0+21rHb7bLb7Te4MgAAcCm3hYVt27bp+PHjqlOnjqMtPT1da9eu1cSJE5WSkiIPDw93lQcAAP7HbWGhWbNm2rlzp1Nbt27dVLlyZb366qsEhTuM8fBSYs1OTssAgLzBbWGhQIECql69ulObn5+fChUq5NKOO4DNJuPp7e4qAABZcPtsCAAAkLe57cxCVlavXu3uEgAAwGU4swAAACwRFgAAgCXCAgAAsERYAAAAlggLAADAEmEBAABYIiwAAABLhAUAAGCJsAAAACwRFgAAgCXCAgAAsERYAAAAlggLAADAUp761UkAQN5kjFFycrJj2c/PTzabzY0V4WYiLAAArio5OVnt2rVzLC9evFj+/v5urAg3E5chAACAJcICAACwRFgAAACWCAsAAMASAxwB3LLqvvyxu0u4Y9jSUhV4yXLjIfNkPL3dVs+dZNvoru4ugTMLAADAGmEBAABYIiwAAABLhAUAAGCJsAAAACwxGwIAcFXGw0uJNTs5LePOQVgAAFydzcZUyTsYlyEAAIAlwgIAALBEWAAAAJYICwAAwBJhAQAAWCIsAAAAS4QFAABgibAAAAAsERYAAIAlwgIAALBEWAAAAJYICwAAwBJhAQAAWCIsAAAAS4QFAABgibAAAAAsERYAAIAlwgIAALBEWAAAAJYICwAAwBJhAQAAWCIsAAAAS4QFAABgibAAAAAsERYAAIAlwgIAALBEWAAAAJYICwAAwBJhAQAAWHJrWIiLi1PNmjUVEBCggIAA1atXT8uWLXNnSQAA4DJuDQulSpXSO++8o23btmnr1q1q2rSp2rVrp927d7uzLAAAcAlPd+68TZs2TstvvfWW4uLitHHjRlWrVs2lf0pKilJSUhzLZ8+eveE1AgBwp8szYxbS09M1b948JScnq169eln2GTlypAIDAx23kJCQm1wlAAB3HreHhZ07d8rf3192u13PP/+8Pv/8c1WtWjXLvjExMUpMTHTcjhw5cpOrBQDgzuPWyxCSVKlSJW3fvl2JiYn67LPPFBUVpTVr1mQZGOx2u+x2uxuqBADgzuX2sODt7a3y5ctLkurWrastW7Zo/PjxmjJlipsrAwAAUh64DHG5jIwMp0GMAADAvdx6ZiEmJkYtW7ZU6dKlde7cOc2dO1erV69WfHy8O8sCAACXcGtYOH78uLp27aqjR48qMDBQNWvWVHx8vB588EF3lgUAAC7h1rAwbdo0d+4eAABkQ54bswAAAPIWwgIAALBEWAAAAJYICwAAwBJhAQAAWCIsAAAAS4QFAABgibAAAAAsERYAAIAlwgIAALBEWAAAAJYICwAAwBJhAQAAWCIsAAAAS4QFAABgibAAAAAsERYAAIAlwgIAALBEWAAAAJYICwAAwBJhAQAAWCIsAAAAS4QFAABgibAAAAAsERYAAIAlwgIAALBEWAAAAJYICwAAwBJhAQAAWCIsAAAASzkOCwcOHNDgwYPVqVMnHT9+XJK0bNky7d69O9eKAwAA7pejsLBmzRrVqFFDmzZt0sKFC5WUlCRJ2rFjh4YNG5arBQIAAPfKUVgYNGiQRowYoeXLl8vb29vR3rRpU23cuDHXigMAAO6Xo7Cwc+dOPfLIIy7tRYoU0cmTJ6+7KAAAkHfkKCwEBQXp6NGjLu0//PCDSpYsed1FAQCAvCNHYaFjx4569dVXdezYMdlsNmVkZGj9+vUaOHCgunbtmts1AgAAN8pRWHj77bdVuXJlhYSEKCkpSVWrVlXDhg1Vv359DR48OLdrBAAAbuSZk5W8vb01depUDR06VDt37lRSUpLuvvtuVahQIbfrAwAAbpajMwtvvPGGzp8/r5CQELVq1UodOnRQhQoVdOHCBb3xxhu5XSMAAHCjHIWF2NhYx3crXOr8+fOKjY297qIAAEDekaOwYIyRzWZzad+xY4cKFix43UUBAIC845rGLAQHB8tms8lms6lixYpOgSE9PV1JSUl6/vnnc71IAADgPtcUFsaNGydjjJ5++mnFxsYqMDDQcZ+3t7fCwsJUr169XC8SAAC4zzWFhaioKElSmTJlVL9+fXl5ed2QogAAQN6Ro6mTjRo1cvz74sWLSk1Ndbo/ICDg+qoCAAB5Ro4GOJ4/f169evVSkSJF5Ofnp+DgYKcbAAC4feQoLLz88stauXKl4uLiZLfb9dFHHyk2NlYlSpTQxx9/nNs1AgAAN8rRZYgvv/xSH3/8sRo3bqxu3bopPDxc5cuXV2hoqObMmaPOnTvndp0AAMBNcnRm4dSpUypbtqykf8YnnDp1SpL0wAMPaO3atblXHQAAcLschYWyZcsqISFBklS5cmV9+umnkv454xAUFJRrxQEAAPfLUVjo1q2bduzYIUkaNGiQJk2aJB8fH7300kt6+eWXc7VAAADgXtc8ZuHvv//WkiVL9MEHH0iSIiIitHfvXm3btk3ly5dXzZo1c71IAADgPtccFry8vPTjjz86tYWGhio0NDTXigIAAHlHji5DdOnSRdOmTcvtWgAAQB6Uo6mTaWlpmj59ur799lvVrVtXfn5+TvePHTs2V4oDAADul6OwsGvXLtWpU0eStH//fqf7svrpagAAcOvKUVhYtWpVrux85MiRWrhwofbu3StfX1/Vr19f7777ripVqpQr2wcAANcvR2MWcsuaNWvUs2dPbdy4UcuXL9fff/+t5s2bKzk52Z1lAQCAS+TozEJu+frrr52WZ86cqSJFimjbtm1q2LChS/+UlBSlpKQ4ls+ePXvDawQA4E7n1jMLl0tMTJQkFSxYMMv7R44cqcDAQMctJCTkZpYHAMAdKc+EhYyMDPXr108NGjRQ9erVs+wTExOjxMREx+3IkSM3uUoAAO48br0McamePXtq165dWrdu3RX72O122e32m1gVAADIE2GhV69eWrJkidauXatSpUq5uxwAAHAJt4YFY4x69+6tzz//XKtXr1aZMmXcWQ4AAMiCW8NCz549NXfuXC1evFgFChTQsWPHJEmBgYHy9fV1Z2kAAOB/3DrAMS4uTomJiWrcuLGKFy/uuM2fP9+dZQEAgEu4/TIEAADI2/LM1EkAAJA3ERYAAIAlwgIAALBEWAAAAJYICwAAwBJhAQAAWCIsAAAAS4QFAABgibAAAAAsERYAAIAlwgIAALBEWAAAAJYICwAAwBJhAQAAWCIsAAAAS4QFAABgibAAAAAsERYAAIAlwgIAALBEWAAAAJYICwAAwBJhAQAAWCIsAAAAS4QFAABgibAAAAAsERYAAIAlwgIAALBEWAAAAJYICwAAwBJhAQAAWCIsAAAAS4QFAABgibAAAAAsERYAAIAlwgIAALBEWAAAAJYICwAAwBJhAQAAWCIsAAAAS4QFAABgibAAAAAsERYAAIAlwgIAALBEWAAAAJYICwAAwBJhAQAAWCIsAAAAS4QFAABgibAAAAAsERYAAIAlwgIAALBEWAAAAJYICwAAwBJhAQAAWCIsAAAAS4QFAABgya1hYe3atWrTpo1KlCghm82mRYsWubMcAACQBbeGheTkZNWqVUuTJk1yZxkAAMCCpzt33rJlS7Vs2dKdJQAAgKtwa1i4VikpKUpJSXEsnz171o3VAABwZ7ilBjiOHDlSgYGBjltISIi7SwIA4LZ3S4WFmJgYJSYmOm5Hjhxxd0kAANz2bqnLEHa7XXa73d1lAABwR7mlziwAAICbz61nFpKSkvTLL784lhMSErR9+3YVLFhQpUuXdmNlAAAgk1vDwtatW9WkSRPHcv/+/SVJUVFRmjlzppuqAgAAl3JrWGjcuLGMMe4sAQAAXAVjFgAAgCXCAgAAsERYAAAAlggLAADAEmEBAABYIiwAAABLhAUAAGCJsAAAACwRFgAAgCXCAgAAsERYAAAAlggLAADAEmEBAABYIiwAAABLhAUAAGCJsAAAACwRFgAAgCXCAgAAsERYAAAAlggLAADAEmEBAABYIiwAAABLhAUAAGCJsAAAACwRFgAAgCXCAgAAsERYAAAAlggLAADAEmEBAABYIiwAAABLhAUAAGCJsAAAACwRFgAAgCXCAgAAsERYAAAAlggLAADAEmEBAABYIiwAAABLhAUAAGCJsAAAACwRFgAAgCXCAgAAsERYAAAAlggLAADAEmEBAABYIiwAAABLhAUAAGCJsAAAACwRFgAAgCXCAgAAsERYAAAAlggLAADAEmEBAABYIiwAAABLhAUAAGCJsAAAACzlibAwadIkhYWFycfHR/fdd582b97s7pIAAMD/uD0szJ8/X/3799ewYcP0/fffq1atWoqMjNTx48fdXRoAAFAeCAtjx45V9+7d1a1bN1WtWlUffPCB8ufPr+nTp7u7NAAAIMnTnTtPTU3Vtm3bFBMT42jLly+fIiIitGHDBpf+KSkpSklJcSwnJiZKks6ePXtD6ktPuXBDtgvkJTfq9XMz8BrFneBGvUYzt2uMuWpft4aFkydPKj09XUWLFnVqL1q0qPbu3evSf+TIkYqNjXVpDwkJuWE1Are7wAnPu7sEABZu9Gv03LlzCgwMtOzj1rBwrWJiYtS/f3/HckZGhk6dOqVChQrJZrO5sTLkhrNnzyokJERHjhxRQECAu8sBcBleo7cXY4zOnTunEiVKXLWvW8PCXXfdJQ8PD/35559O7X/++aeKFSvm0t9ut8tutzu1BQUF3cgS4QYBAQH8IQLyMF6jt4+rnVHI5NYBjt7e3qpbt65WrFjhaMvIyNCKFStUr149N1YGAAAyuf0yRP/+/RUVFaV//etfuvfeezVu3DglJyerW7du7i4NAAAoD4SFJ554QidOnNDQoUN17Ngx1a5dW19//bXLoEfc/ux2u4YNG+ZyqQlA3sBr9M5lM9mZMwEAAO5Ybv9SJgAAkLcRFgAAgCXCAgAAsERYAAAAlggLuOGMMYqIiFBkZKTLfZMnT1ZQUJB+++03N1QG4HLR0dGy2Wx65513nNoXLVrEN+XewQgLuOFsNptmzJihTZs2acqUKY72hIQEvfLKK5owYYJKlSrlxgoBXMrHx0fvvvuuTp8+7e5SkEcQFnBThISEaPz48Ro4cKASEhJkjNEzzzyj5s2b6+6771bLli3l7++vokWL6qmnntLJkycd63722WeqUaOGfH19VahQIUVERCg5OdmNjwa4vUVERKhYsWIaOXLkFfssWLBA1apVk91uV1hYmMaMGXMTK8TNRljATRMVFaVmzZrp6aef1sSJE7Vr1y5NmTJFTZs21d13362tW7fq66+/1p9//qkOHTpIko4ePapOnTrp6aef1p49e7R69Wo9+uij2fpJVQA54+HhobffflsTJkzI8hLhtm3b1KFDB3Xs2FE7d+7U8OHDNWTIEM2cOfPmF4ubgi9lwk11/PhxVatWTadOndKCBQu0a9cufffdd4qPj3f0+e233xQSEqJ9+/YpKSlJdevW1cGDBxUaGurGyoE7Q3R0tM6cOaNFixapXr16qlq1qqZNm6ZFixbpkUcekTFGnTt31okTJ/TNN9841nvllVf01Vdfaffu3W6sHjcKZxZwUxUpUkQ9evRQlSpV9PDDD2vHjh1atWqV/P39HbfKlStLkg4cOKBatWqpWbNmqlGjhtq3b6+pU6dyHRW4Sd59913NmjVLe/bscWrfs2ePGjRo4NTWoEED/fzzz0pPT7+ZJeImISzgpvP09JSn5z8/S5KUlKQ2bdpo+/btTreff/5ZDRs2lIeHh5YvX65ly5apatWqmjBhgipVqqSEhAQ3Pwrg9tewYUNFRkYqJibG3aXAzdz+Q1K4s9WpU0cLFixQWFiYI0BczmazqUGDBmrQoIGGDh2q0NBQff755+rfv/9Nrha487zzzjuqXbu2KlWq5GirUqWK1q9f79Rv/fr1qlixojw8PG52ibgJOLMAt+rZs6dOnTqlTp06acuWLTpw4IDi4+PVrVs3paena9OmTXr77be1detWHT58WAsXLtSJEydUpUoVd5cO3BFq1Kihzp076/3333e0DRgwQCtWrNCbb76p/fv3a9asWZo4caIGDhzoxkpxIxEW4FYlSpTQ+vXrlZ6erubNm6tGjRrq16+fgoKClC9fPgUEBGjt2rVq1aqVKlasqMGDB2vMmDFq2bKlu0sH7hhvvPGGMjIyHMt16tTRp59+qnnz5ql69eoaOnSo3njjDUVHR7uvSNxQzIYAAACWOLMAAAAsERYAAIAlwgIAALBEWAAAAJYICwAAwBJhAQAAWCIsAAAAS4QFAABgibAA3EYaN26sfv363dB9hIWFady4cTd0H5eLjo7Www8/bNnnZjx24E5FWABw0/CGDtyaCAsAAMASYQG4zaSlpalXr14KDAzUXXfdpSFDhijzJ2BOnz6trl27Kjg4WPnz51fLli31888/O62/YMECVatWTXa7XWFhYRozZozl/j766CMFBQVpxYoVlv2io6O1Zs0ajR8/XjabTTabTQcPHlR6erqeeeYZlSlTRr6+vqpUqZLGjx+f5TZiY2NVuHBhBQQE6Pnnn1dqauoV95eSkqKBAweqZMmS8vPz03333afVq1db1ggga4QF4DYza9YseXp6avPmzRo/frzGjh2rjz76SNI/b9hbt27VF198oQ0bNsgYo1atWunvv/+WJG3btk0dOnRQx44dtXPnTg0fPlxDhgzRzJkzs9zXqFGjNGjQIH3zzTdq1qyZZV3jx49XvXr11L17dx09elRHjx5VSEiIMjIyVKpUKf33v//VTz/9pKFDh+q1117Tp59+6rT+ihUrtGfPHq1evVqffPKJFi5cqNjY2Cvur1evXtqwYYPmzZunH3/8Ue3bt1eLFi1cwhGAbDAAbhuNGjUyVapUMRkZGY62V1991VSpUsXs37/fSDLr16933Hfy5Enj6+trPv30U2OMMU8++aR58MEHnbb58ssvm6pVqzqWQ0NDzXvvvWdeeeUVU7x4cbNr165rqq9v375X7dezZ0/z2GOPOZajoqJMwYIFTXJysqMtLi7O+Pv7m/T0dJdtHzp0yHh4eJjff//dabvNmjUzMTEx2a4XwD883R1WAOSu+++/XzabzbFcr149jRkzRj/99JM8PT113333Oe4rVKiQKlWqpD179kiS9uzZo3bt2jltr0GDBho3bpzS09Pl4eEhSRozZoySk5O1detWlS1b9rprnjRpkqZPn67Dhw/rwoULSk1NVe3atZ361KpVS/nz53d6XElJSTpy5IhCQ0Od+u7cuVPp6emqWLGiU3tKSooKFSp03fUCdxrCAoBrFh4erq+++kqffvqpBg0adF3bmjdvngYOHKgxY8aoXr16KlCggEaPHq1NmzbleJtJSUny8PDQtm3bHAEnk7+//3XVC9yJCAvAbebyN9mNGzeqQoUKqlq1qtLS0rRp0ybVr19fkvTXX39p3759qlq1qiSpSpUqWr9+vdP669evV8WKFZ3edO+991716tVLLVq0kKenpwYOHJit2ry9vZWenu6y/fr16+vFF190tB04cMBl3R07dujChQvy9fV1PC5/f3+FhIS49L377ruVnp6u48ePKzw8PFu1AbgyBjgCt5nDhw+rf//+2rdvnz755BNNmDBBffv2VYUKFdSuXTt1795d69at044dO9SlSxeVLFnScelhwIABWrFihd58803t379fs2bN0sSJE7MMA/Xr19fSpUsVGxub7S9pCgsL06ZNm3Tw4EGdPHlSGRkZqlChgrZu3ar4+Hjt379fQ4YM0ZYtW1zWTU1N1TPPPKOffvpJS5cu1bBhw9SrVy/ly+f6Z6xixYrq3LmzunbtqoULFyohIUGbN2/WyJEj9dVXX13bAQXAAEfgdtKoUSPz4osvmueff94EBASY4OBg89prrzkGPJ46dco89dRTJjAw0Pj6+prIyEizf/9+p2189tlnpmrVqsbLy8uULl3ajB492un+zAGOmdasWWP8/PzM+++/f9X69u3bZ+6//37j6+trJJmEhARz8eJFEx0dbQIDA01QUJB54YUXzKBBg0ytWrUc60VFRZl27dqZoUOHmkKFChl/f3/TvXt3c/HiRafHfungydTUVDN06FATFhZmvLy8TPHixc0jjzxifvzxx2s4ogCMMcZmzP8mYAMAAGSByxAAAMASYQFArjh8+LD8/f2veDt8+LC7SwSQQ1yGAJAr0tLSdPDgwSveHxYWJk9PJmABtyLCAgAAsMRlCAAAYImwAAAALBEWAACAJcICAACwRFgAAACWCAsAAMASYQEAAFj6PzKQhvwhx2UJAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "- Restaurants with table booking  have higher ratings, possibly due to better service and dining experience.\n",
        "\n",
        "- Non-booking restaurants show mixed ratings, meaning their service quality is less predictable."
      ],
      "metadata": {
        "id": "0fQN0uo8v6Jn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Cost vs Rating Scatter Plot\n",
        "plt.figure(figsize=(8, 5))\n",
        "sns.scatterplot(x='cost_for_two', y='rate', hue='online_order', data=data)\n",
        "plt.title(\"Cost for Two vs. Ratings\")\n",
        "plt.xlabel(\"Cost for Two\")\n",
        "plt.ylabel(\"Rating\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 487
        },
        "id": "sAAsRFzpm9Dh",
        "outputId": "a02a854d-a142-49af-c16e-2405647f4047"
      },
      "execution_count": 186,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x500 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAArsAAAHWCAYAAAB34UGbAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAkXxJREFUeJzs3WeYk2X69/FvJtN7bzDAUKV3qYIKUtQVLKioC9jX8hddFcUKtgF1d0V9xI7oiljRdVUQUVAEUcRCE+l9CtNrJpPcz4ssI2GSoUgKk9/nOHLAXOed5Ew/c+UqJsMwDEREREREmqAgXycgIiIiIuIpKnZFREREpMlSsSsiIiIiTZaKXRERERFpslTsioiIiEiTpWJXRERERJosFbsiIiIi0mSp2BURERGRJkvFroiIiIg0WSp2RUQOsXnzZkaMGEFcXBwmk4kPP/zQ1ynJCTZp0iRatWrl6zRExEtU7IqI12zdupXrr7+e1q1bEx4eTmxsLIMGDWLWrFlUV1ef8Ourqqpi2rRpLF269KjPM3HiRNauXcujjz7KG2+8QZ8+fU54XgCnn346JpPpiKdp06Z55Pr9ybRp05xuc0hICK1ateKWW26hpKTkuC5z3759TJs2jZ9//vmE5ioiJ59gXycgIoHhk08+Ydy4cYSFhTFhwgS6dOlCbW0ty5cv584772T9+vW8+OKLJ/Q6q6qqmD59OuAoLo+kurqalStXcu+993LzzTef0FwOd++993LNNdfU//3DDz/w9NNPc88999CxY8f69m7dunk0D38ye/ZsoqOjqaysZMmSJTzzzDOsWbOG5cuXH/Nl7du3j+nTp9OqVSt69OjhFHvppZew2+0nKGsR8XcqdkXE47Zv386ll15Ky5Yt+fLLL8nIyKiP3XTTTWzZsoVPPvnEhxk6FBQUABAfH3/CLrOyspKoqKgG7WeddZbT3+Hh4Tz99NOcddZZR1WYN0UXXXQRycnJAFx//fVceumlvP3223z//feceuqpJ+x6QkJCTthliYj/0zAGEfG4xx9/nIqKCl555RWnQvegtm3bMnny5Pq/6+rqePjhh2nTpg1hYWG0atWKe+65B4vF4nS+1atXM3LkSJKTk4mIiCA7O5urrroKgB07dpCSkgLA9OnTjzgsYNq0abRs2RKAO++8E5PJ5DSu86effmL06NHExsYSHR3NsGHD+O6775wu47XXXsNkMrFs2TJuvPFGUlNTad68+THfXwBPP/00ZrPZ6Wf8f/zjH5hMJv7+97/Xt9lsNmJiYrjrrrvq2yorK7n99tvJysoiLCyMDh068OSTT2IYRqPXefPNNxMdHU1VVVWD2Pjx40lPT8dmswGN3/cnymmnnQY4hr8cVFRUxB133EHXrl2Jjo4mNjaW0aNH88svv9Qfs3TpUvr27QvAlVdeWf/Yv/baa0DDMbs7duzAZDLx5JNP8uKLL9Y/7/r27csPP/zQIK93332XTp06ER4eTpcuXViwYIHLccDz58+nd+/exMTEEBsbS9euXZk1a9YJundE5GipZ1dEPO7jjz+mdevWDBw48KiOv+aaa5g7dy4XXXQRt99+O6tWrSInJ4eNGzeyYMECAPLz8xkxYgQpKSncfffdxMfHs2PHDj744AMAUlJSmD17NjfccAPnn38+F1xwAeB+WMAFF1xAfHw8t912G+PHj+fss88mOjoagPXr13PaaacRGxvLlClTCAkJ4YUXXuD0009n2bJl9OvXz+mybrzxRlJSUnjggQeorKw8rvvstNNOw263s3z5cs4991wAvvnmG4KCgvjmm2/qj/vpp5+oqKhgyJAhABiGwXnnncdXX33F1VdfTY8ePVi0aBF33nkne/fu5V//+pfb67zkkkv4f//v/9UPOTmoqqqKjz/+mEmTJmE2m494358oO3bsACAhIaG+bdu2bXz44YeMGzeO7Oxs8vLyeOGFFxg6dCgbNmwgMzOTjh078tBDD/HAAw9w3XXX1RfNR3r+zZs3j/Lycq6//npMJhOPP/44F1xwAdu2bavvDf7kk0+45JJL6Nq1Kzk5ORQXF3P11VfTrFkzp8tavHgx48ePZ9iwYcycOROAjRs38u233zp9sRMRLzBERDyotLTUAIwxY8Yc1fE///yzARjXXHONU/sdd9xhAMaXX35pGIZhLFiwwACMH374we1lFRQUGIDx4IMPHtV1b9++3QCMJ554wql97NixRmhoqLF169b6tn379hkxMTHGkCFD6tvmzJljAMbgwYONurq6o7rOg959910DML766ivDMAzDZrMZsbGxxpQpUwzDMAy73W4kJSUZ48aNM8xms1FeXm4YhmH885//NIKCgozi4mLDMAzjww8/NADjkUcecbr8iy66yDCZTMaWLVvc5mC3241mzZoZF154oVP7O++8YwDG119/bRjG0d33x+LBBx80AGPTpk1GQUGBsWPHDuPVV181IiIijJSUFKOysrL+2JqaGsNmszmdf/v27UZYWJjx0EMP1bf98MMPBmDMmTOnwfVNnDjRaNmypdP5ASMpKckoKiqqb//oo48MwPj444/r27p27Wo0b968/v43DMNYunSpAThd5uTJk43Y2Nhjfh6IyImnYQwi4lFlZWUAxMTEHNXxn376KYDTT/UAt99+O0D92N6D42r/+9//YrVaT0SqLtlsNj7//HPGjh1L69at69szMjK47LLLWL58ef1tPOjaa6/FbDb/qesNCgpi4MCBfP3114CjV7CwsJC7774bwzBYuXIl4Ojt7dKlS/398emnn2I2m7nlllucLu/222/HMAw+++wzt9dpMpkYN24cn376KRUVFfXtb7/9Ns2aNWPw4MGA5+77Dh06kJKSQqtWrbjqqqto27Ytn332GZGRkfXHhIWFERTk+Oiy2WwUFhYSHR1Nhw4dWLNmzZ+6/ksuucSpF/lgj/C2bdsAx6S3tWvXMmHChPpef4ChQ4fStWtXp8uKj4+nsrKSxYsX/6mcROTPU7ErIh4VGxsLQHl5+VEdv3PnToKCgmjbtq1Te3p6OvHx8ezcuRNwFBgXXngh06dPJzk5mTFjxjBnzpwG43r/rIKCAqqqqujQoUODWMeOHbHb7ezevdupPTs7+4Rc92mnncaPP/5IdXU133zzDRkZGfTq1Yvu3bvXD2VYvnx5fVEGjvsvMzOzwZeLgys8HLz/3Lnkkkuorq7mP//5DwAVFRV8+umnjBs3DpPJBHjuvn///fdZvHgx8+bNo3///uTn5xMREeF0jN1u51//+hft2rUjLCyM5ORkUlJS+PXXXyktLf1T19+iRQunvw8WvsXFxcAf993hz01XbTfeeCPt27dn9OjRNG/enKuuuoqFCxf+qfxE5Pio2BURj4qNjSUzM5N169Yd0/kOFlaNxd977z1WrlzJzTffzN69e7nqqqvo3bu3U6+kLxxeoB2vwYMHY7VaWblyJd988019UXvaaafxzTff8Ntvv1FQUOBU7P5Z/fv3p1WrVrzzzjuAY7x1dXU1l1xySf0xnrrvhwwZwvDhwxk/fjyLFy8mIiKCyy+/3GmZsMcee4y///3vDBkyhH//+98sWrSIxYsX07lz5z+9nJi73njjCBP7XElNTeXnn3/mP//5T/0Y6tGjRzNx4sQ/laOIHDsVuyLiceeeey5bt26t/+m9MS1btsRut7N582an9ry8PEpKSupXTDiof//+PProo6xevZo333yT9evXM3/+fODIBfPRSElJITIykk2bNjWI/fbbbwQFBZGVlfWnr8eVU089ldDQUL755hunYnfIkCGsWrWKJUuW1P99UMuWLdm3b1+DnvTffvutPn4kF198MQsXLqSsrIy3336bVq1a0b9//wbHNXbf/1nR0dE8+OCD/Pzzz/WFN8B7773HGWecwSuvvMKll17KiBEjGD58eIPNJ07EY3+4g/fdli1bGsRctYWGhvKXv/yF5557rn5Dlddff93lsSLiOSp2RcTjpkyZQlRUFNdccw15eXkN4lu3bq1fkunss88G4KmnnnI65p///CcA55xzDuD4afnwHreDmwcc/Dn94FjP492FCxy9fSNGjOCjjz6qXx0AHMX3vHnzGDx4cP1QjRMtPDycvn378tZbb7Fr1y6nnt3q6mqefvpp2rRp47Sc29lnn43NZuPZZ591uqx//etfmEwmRo8efcTrveSSS7BYLMydO5eFCxdy8cUXO8WP5r4Hx+N66LJhx+ryyy+nefPm9asZgOPxOPy63333Xfbu3evUdnBt4z/z2B8uMzOTLl268Prrrzv1YC9btoy1a9c6HVtYWOj0d1BQUP1KICd6qI2INE5Lj4mIx7Vp04Z58+ZxySWX0LFjR6cd1FasWMG7777LpEmTAOjevTsTJ07kxRdfpKSkhKFDh/L9998zd+5cxo4dyxlnnAHA3Llzee655zj//PNp06YN5eXlvPTSS8TGxtYXzBEREXTq1Im3336b9u3bk5iYSJcuXejSpcsx5f/II4+wePFiBg8ezI033khwcDAvvPACFouFxx9//ITeV4c77bTTmDFjBnFxcfWToFJTU+nQoQObNm2qv98O+stf/sIZZ5zBvffey44dO+jevTuff/45H330Ebfeeitt2rQ54nX26tWLtm3bcu+992KxWJyGMMDR3fcAw4YNA3D6knAsQkJCmDx5MnfeeScLFy5k1KhRnHvuuTz00ENceeWVDBw4kLVr1/Lmm286TR4Ex3MuPj6e559/npiYGKKioujXr9+fHk/92GOPMWbMGAYNGsSVV15JcXExzz77LF26dHEqgK+55hqKioo488wzad68OTt37uSZZ56hR48eTjvkiYgX+HIpCBEJLL///rtx7bXXGq1atTJCQ0ONmJgYY9CgQcYzzzxj1NTU1B9ntVqN6dOnG9nZ2UZISIiRlZVlTJ061emYNWvWGOPHjzdatGhhhIWFGampqca5555rrF692uk6V6xYYfTu3dsIDQ094jJk7pYeO3h9I0eONKKjo43IyEjjjDPOMFasWOF0zMGlx45nSa7Dlx476JNPPjEAY/To0U7t11xzjQEYr7zySoPLKi8vN2677TYjMzPTCAkJMdq1a2c88cQTht1uP+p87r33XgMw2rZt2yB2tPd9y5YtnZbjcufg0mMFBQUNYqWlpUZcXJwxdOhQwzAcS4/dfvvtRkZGhhEREWEMGjTIWLlypTF06ND6Yw766KOPjE6dOhnBwcFOy5C5W3rM1ePu6jkzf/5845RTTjHCwsKMLl26GP/5z3+MCy+80DjllFPqj3nvvfeMESNGGKmpqUZoaKjRokUL4/rrrzf2799/xPtDRE4sk2Ecx8h7ERERqdejRw9SUlK01JiIH9KYXRERkaNktVqpq6tzalu6dCm//PILp59+um+SEpFGqWdXRETkKO3YsYPhw4dzxRVXkJmZyW+//cbzzz9PXFwc69atIykpydcpishhNEFNRETkKCUkJNC7d29efvllCgoKiIqK4pxzzmHGjBkqdEX8lHp2RURERKTJ0phdEREREWmyVOyKiIiISJOlMbsu2O129u3bR0xMjEe2nBQRERGRP8cwDMrLy8nMzCQoyH3/rYpdF/bt2+exve5FRERE5MTZvXs3zZs3dxtXsetCTEwM4LjzPLXnvYiIiIgcv7KyMrKysurrNndU7LpwcOhCbGysil0RERERP3akIaeaoCYiIiIiTZaKXRERERFpslTsioiIiEiTpTG7IiIiIm4YhkFdXR02m83XqQQcs9lMcHDwn14GVsWuiIiIiAu1tbXs37+fqqoqX6cSsCIjI8nIyCA0NPS4L0PFroiIiMhh7HY727dvx2w2k5mZSWhoqDaa8iLDMKitraWgoIDt27fTrl27RjeOaIyKXREREZHD1NbWYrfbycrKIjIy0tfpBKSIiAhCQkLYuXMntbW1hIeHH9flaIKaiIiIiBvH25soJ8aJuP/1CIqIiIhIk6ViV0RERESaLBW7IiLi93YWVvLfX/cx7T/reWX5NrbkV1BdW+frtET+lGnTptGjR4/6vydNmsTYsWN9ls+fcfht8SeaoCYiIn5tS34FE15Zxb7Smvq2meZNvDShN6e2SiQiTB9l0jTMmjULwzB8nUaTo55dERHxW/nlNdz/0TqnQheg1mbnhjfXkFtu8VFmIideXFwc8fHxvk6jUVar9aS7bBW7IiLit0qqrKzcWugyVlVrY0t+uZczEvmDxWLhlltuITU1lfDwcAYPHswPP/wAwNKlSzGZTCxZsoQ+ffoQGRnJwIED2bRpk9vLO3wYw+mnn84tt9zClClTSExMJD09nWnTpjmdp6SkhGuuuYaUlBRiY2M588wz+eWXX476NsyePZs2bdoQGhpKhw4deOONN5ziJpOJ2bNnc9555xEVFcWjjz4KwIwZM0hLSyMmJoarr76ampqaBpf98ssv07FjR8LDwznllFN47rnn6mM7duzAZDLx9ttvM3ToUMLDw3nzzTePOu9joWJXRET8Vm2dvdF4cZXneplEjmTKlCm8//77zJ07lzVr1tC2bVtGjhxJUVFR/TH33nsv//jHP1i9ejXBwcFcddVVx3Qdc+fOJSoqilWrVvH444/z0EMPsXjx4vr4uHHjyM/P57PPPuPHH3+kV69eDBs2zCkHdxYsWMDkyZO5/fbbWbduHddffz1XXnklX331ldNx06ZN4/zzz2ft2rVcddVVvPPOO0ybNo3HHnuM1atXk5GR4VTIArz55ps88MADPProo2zcuJHHHnuM+++/n7lz5zodd/fddzN58mQ2btzIyJEjj+m+OWqGNFBaWmoARmlpqa9TEREJaDsOVBh9Hl5stLzrvy5P6/aW+DpFaaKqq6uNDRs2GNXV1S7jFRUVRkhIiPHmm2/Wt9XW1hqZmZnG448/bnz11VcGYHzxxRf18U8++cQA6i/zwQcfNLp3714fnzhxojFmzJj6v4cOHWoMHjzY6Xr79u1r3HXXXYZhGMY333xjxMbGGjU1NU7HtGnTxnjhhReOeBsHDhxoXHvttU5t48aNM84+++z6vwHj1ltvdTpmwIABxo033ujU1q9fP6fb0qZNG2PevHlOxzz88MPGgAEDDMMwjO3btxuA8dRTTzWaY2OPw9HWa+rZFRERv9UsLoIpozu4jI3slEZyVKiXMxJx2Lp1K1arlUGDBtW3hYSEcOqpp7Jx48b6tm7dutX/PyMjA4D8/Pyjvp5Dz3/wMg6e/5dffqGiooKkpCSio6PrT9u3b2fr1q1HvOyNGzc65Q8waNAgp/wB+vTp0+B8/fr1c2obMGBA/f8rKyvZunUrV199tVNejzzySIO8Dr9sT9AUVhER8VvBwUEMbZfC81f04olFv7O1oIKEyBAmDmzFuN7NSYuL8HWKIo0KCQmp/7/JZALAbm98eI678x+8jIPnr6ioICMjg6VLlzY434mc6BYVFXVMx1dUVADw0ksvNSiKzWbzn7rs46FiV0RE/FpqbDijumTQpVkctXV2goNMZMRHEGLWj5PiOwcndX377be0bNkScKwm8MMPP3Drrbd6JYdevXqRm5tLcHAwrVq1Oubzd+zYkW+//ZaJEyfWt3377bd06tTpiOdbtWoVEyZMqG/77rvv6v+flpZGZmYm27Zt4/LLLz/mvE40FbsiInJSaJ4Q6esUROpFRUVxww03cOedd5KYmEiLFi14/PHHqaqq4uqrrz6mFRGO1/DhwxkwYABjx47l8ccfp3379uzbt49PPvmE888//4hDBO68804uvvhievbsyfDhw/n444/54IMP+OKLLxo93+TJk5k0aRJ9+vRh0KBBvPnmm6xfv57WrVvXHzN9+nRuueUW4uLiGDVqFBaLhdWrV1NcXMzf//73E3L7j5aKXREREZHjMGPGDOx2O3/9618pLy+nT58+LFq0iISEBK9cv8lk4tNPP+Xee+/lyiuvpKCggPT0dIYMGUJaWtoRzz927FhmzZrFk08+yeTJk8nOzmbOnDmcfvrpjZ7vkksuYevWrUyZMoWamhouvPBCbrjhBhYtWlR/zDXXXENkZCRPPPEEd955J1FRUXTt2tVrvd6HMv1vpp0coqysjLi4OEpLS4mNjfV1OiIiIuJlNTU1bN++nezsbMLDw32dTsBq7HE42npNA55EREREpMlSsSsiIiLSBHXu3Nlp6a9DT57arcwfacyuiIiISBP06aefYrW63mXwaMb0NhUqdkVERESaoINLogU6DWMQERERkSZLxa6IiIiINFl+U+zOmDEDk8nU6Pprr732GiaTyel0+DIUhmHwwAMPkJGRQUREBMOHD2fz5s0ezl5ERERE/JFfFLs//PADL7zwAt26dTvisbGxsezfv7/+tHPnTqf4448/ztNPP83zzz/PqlWriIqKYuTIkdTU1HgqfRERERHxUz4vdisqKrj88st56aWXjmrHEZPJRHp6ev3p0NmEhmHw1FNPcd999zFmzBi6devG66+/zr59+/jwww89eCtERERExB/5vNi96aabOOeccxg+fPhRHV9RUUHLli3JyspizJgxrF+/vj62fft2cnNznS4rLi6Ofv36sXLlSreXabFYKCsrczqJiIiIyMnPp8Xu/PnzWbNmDTk5OUd1fIcOHXj11Vf56KOP+Pe//43dbmfgwIHs2bMHgNzcXKDh2nFpaWn1MVdycnKIi4urP2VlZR3nLRIRERH580qratmaX8FPu4rZWlBBaVWtx67LMAyGDx/OyJEjG8See+454uPj62utk5HP1tndvXs3kydPZvHixUe95/SAAQMYMGBA/d8DBw6kY8eOvPDCCzz88MPHncvUqVP5+9//Xv93WVmZCl4RERHxiX0l1dz1/q98s/lAfduQdsnMuLAbmfERJ/z6TCYTc+bMoWvXrrzwwgtcf/31gOMX8ylTpjB79myaN29+wq/XW3zWs/vjjz+Sn59Pr169CA4OJjg4mGXLlvH0008THByMzWY74mWEhITQs2dPtmzZAkB6ejoAeXl5Tsfl5eXVx1wJCwsjNjbW6SQiIiLibaVVtQ0KXYCvNx/g7vd/9VgPb1ZWFrNmzeKOO+5g+/btGIbB1VdfzYgRI+jZsyejR48mOjqatLQ0/vrXv3LgwB/5vffee3Tt2pWIiAiSkpIYPnw4lZWVHsnzePis2B02bBhr167l559/rj/16dOHyy+/nJ9//hmz2XzEy7DZbKxdu5aMjAwAsrOzSU9PZ8mSJfXHlJWVsWrVKqceYRERERF/dKCitkGhe9DXmw9woMJzwxkmTpzIsGHDuOqqq3j22WdZt24dL7zwAmeeeSY9e/Zk9erVLFy4kLy8PC6++GIA9u/fz/jx47nqqqvYuHEjS5cu5YILLsAwDI/leax8NowhJiaGLl26OLVFRUWRlJRU3z5hwgSaNWtWP6b3oYceon///rRt25aSkhKeeOIJdu7cyTXXXANQv07vI488Qrt27cjOzub+++8nMzOTsWPHevX2iYiIiByrshpro/HyI8T/rBdffJHOnTvz9ddf8/777/PCCy/Qs2dPHnvssfpjXn31VbKysvj999+pqKigrq6OCy64oH574q5du3o0x2Pls2L3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888/b3CZZrOZX3/9lblz51JSUkJmZiYjRozg4Ycf1lq7IiIiIgHGbyao+RNtFywiIiLi306qCWoiIiIiIp6gYldEREREmiwVuyIiIiLSZKnYFREREZEmS8WuiIiIiDRZKnZFREREpMlSsSsiIiIiTZaKXRERERFpslTsioiIiEiTpWJXRERERJosFbsiIiIi0mSp2BURERGRJkvFroiIiIg0WSp2RURERKTJUrErIiIiIk1WsK8TEBEROaLSvbD/F9i5AhKzoc2ZENcMzKG+zkxE/JyKXRER8W9F22HuuVC65482cyhc8R5kDYTgEN/lJiJ+T8MYRETEf1WXwMe3Ohe6ALZaeGs8VOT6IisROYmo2BUREf9VVQjbl7qO1VbCgd+9mo6InHxU7IqIiP+y1TYery72Th4ictJSsSsiIv4rPA6iU93H07p4LxcROSmp2BUREf8VnQ4jc1zHOp/feCEsIoKKXRER8WdBQdD2LLjsHUhu72iLTIRh02D0TMf/RUQaoaXHRETEv0XEQfuRkNkT6mogKBii0yDI7OvMROQkoGJXRERODhqyICLHQcMYRERERKTJUrErIiIiIk2Wil0RERERabJU7IqIiIhIk6ViV0RERESaLBW7IiIiItJkqdgVERERkSZLxa6IiIiINFk+LXZzcnLo27cvMTExpKamMnbsWDZt2tToeV577TVMJpPTKTw83OkYwzB44IEHyMjIICIiguHDh7N582ZP3hQRERER8UM+LXaXLVvGTTfdxHfffcfixYuxWq2MGDGCysrKRs8XGxvL/v376087d+50ij/++OM8/fTTPP/886xatYqoqChGjhxJTU2NJ2+OiIiIiPgZn24XvHDhQqe/X3vtNVJTU/nxxx8ZMmSI2/OZTCbS09NdxgzD4KmnnuK+++5jzJgxALz++uukpaXx4Ycfcumll564GyAiIiIifs2nxe7hSktLAUhMTGz0uIqKClq2bIndbqdXr1489thjdO7cGYDt27eTm5vL8OHD64+Pi4ujX79+rFy50mWxa7FYsFgsDfIoKyv707dJRERERE68g3WaYRiNHuc3xa7dbufWW29l0KBBdOnSxe1xHTp04NVXX6Vbt26Ulpby5JNPMnDgQNavX0/z5s3Jzc0FIC0tzel8aWlp9bHD5eTkMH369AbtWVlZf+IWiYiIiIinlZeXExcX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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "- Online Ordering Impact:\n",
        "\n",
        "Restaurants that offer online ordering seem to have a wide spread of ratings, indicating that online availability does not guarantee higher ratings.\n",
        "\n",
        "- High-Rated Restaurants (4.0+):\n",
        "\n",
        "Exist across different price ranges, from 500 to 850 .\n",
        "\n",
        " both budget-friendly and premium restaurants can achieve high ratings.\n",
        "\n",
        "- Low-Cost Restaurants (< 400):\n",
        "\n",
        "Mostly clustered around average ratings (3.0 - 4.0). maximum they don't have online order in their restaurant.\n",
        "\n",
        "Indicates that lower-cost restaurants generally maintain moderate customer satisfaction.\n",
        "\n",
        "- Expensive Restaurants (700 - 950):\n",
        "\n",
        "Tend to have ratings above 3.5, suggesting that higher-cost restaurants maintain a certain level of quality."
      ],
      "metadata": {
        "id": "3SX6hiManDB0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#cost of restaurant prefer by couples\n",
        "couple_data=data['cost_for_two']\n",
        "sns.countplot(x=couple_data)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 467
        },
        "id": "OsDc2UR5RzI4",
        "outputId": "b8a0c758-41d0-4ce5-9353-8ce4b351d97c"
      },
      "execution_count": 187,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: xlabel='cost_for_two', ylabel='count'>"
            ]
          },
          "metadata": {},
          "execution_count": 187
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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AAD15tVrZAAAAAKBV1dkJkyYUOP2F154watmAAAA6sOrIPPtt9963L548aL279+vkpKSKr9MEgAAwBe8CjKrVq2qtK6iokKTJ09W586dG9wUAABAXTj2GpkmTZpoxowZeuqpp5w6JAAAQI28/tLIqhw6dEiXLl1y8pAAADim/6zlPjnu7ifH+eS4qJ1XQWbGjBket40xKioq0ttvv62MjAxHGgMAAKiNV0Fmz549HrebNGmi6Oho/fu//3ut72gCAABwildBZtOmTU73AQAAUG8Neo3M119/rby8PElS9+7dFR0d7UhTAAAAdeHVu5bOnj2rCRMmKD4+XoMHD9bgwYOVkJCg++67T+fOnXO6RwAAgCp5FWRmzJih7OxsvfnmmyopKVFJSYnWrFmj7OxszZw50+keAQAAquTVU0uvvfaa/vKXvyglJcW97rbbblNYWJjuvvtuLVmyxKn+AAAAquXVFZlz584pNja20vqYmBieWgIAAI3GqyCTnJysefPm6fz58+513333nebPn6/k5GTHmgMAAKiJV08tPf3000pLS9PVV1+tpKQkSdLevXsVGhqq9evXO9ogAABAdbwKMn379lV+fr5WrFihzz77TJI0ZswYjR07VmFhYY42CAAAUB2vgszChQsVGxuriRMneqx/4YUX9PXXX2vOnDmONAcAAFATr14j89///d/q0aNHpfW9e/fWM8880+CmAAAA6sKrIFNcXKz4+PhK66Ojo1VUVNTgpgAAAOrCqyCTmJiorVu3Vlq/detWJSQkNLgpAACAuvDqNTITJ07U9OnTdfHiRQ0dOlSStHHjRs2ePZtP9gUAAI3GqyAza9YsnThxQr/61a904cIFSVKzZs00Z84cZWZmOtogAABAdbwKMi6XS//6r/+quXPn6tNPP1VYWJi6du2q0NBQp/sDAAColldB5rIWLVro+uuvd6oXAACAevHqxb4AAACBgCADAACsRZABAADWIsgAAABrEWQAAIC1CDIAAMBafg0ymzdv1h133KGEhAS5XC6tXr3aY7sxRo888oji4+MVFham1NRU5efn+6dZAAAQcPwaZM6ePaukpCQtXry4yu2///3v9cc//lHPPPOMtm/frquuukrDhw/X+fPnG7lTAAAQiBr0gXgNlZ6ervT09Cq3GWP09NNP65//+Z81YsQISdLy5csVGxur1atX65577mnMVgEAQAAK2NfIFBQUqLi4WKmpqe51ERERGjhwoHJycvzYGQAACBR+vSJTk+LiYklSbGysx/rY2Fj3tqqUlZWprKzMfbu0tNQ3DQIAAL8L2Csy3lq4cKEiIiLcS2Jior9bAgAAPhKwQSYuLk6SdOzYMY/1x44dc2+rSmZmpk6dOuVeCgsLfdonAADwn4ANMh07dlRcXJw2btzoXldaWqrt27crOTm52vuFhoYqPDzcYwEAAFcmv75G5syZMzp48KD7dkFBgXJzcxUVFaV27dpp+vTp+t3vfqeuXbuqY8eOmjt3rhISEjRy5Ej/NQ0AAAKGX4PMrl27dMstt7hvz5gxQ5KUkZGhZcuWafbs2Tp79qwmTZqkkpIS3XTTTVq7dq2aNWvmr5YBAEAA8WuQSUlJkTGm2u0ul0uPPfaYHnvssUbsCgAA2CJgXyMDAABQG4IMAACwFkEGAABYiyADAACsRZABAADWIsgAAABrEWQAAIC1CDIAAMBaBBkAAGAtggwAALAWQQYAAFiLIAMAAKxFkAEAANYiyAAAAGsRZAAAgLUIMgAAwFoEGQAAYC2CDAAAsBZBBgAAWIsgAwAArEWQAQAA1iLIAAAAaxFkAACAtQgyAADAWgQZAABgLYIMAACwFkEGAABYiyADAACsRZABAADWIsgAAABrEWQAAIC1CDIAAMBaBBkAAGAtggwAALAWQQYAAFiLIAMAAKxFkAEAANYiyAAAAGsRZAAAgLUIMgAAwFoEGQAAYC2CDAAAsBZBBgAAWIsgAwAArEWQAQAA1iLIAAAAaxFkAACAtQgyAADAWgQZAABgLYIMAACwFkEGAABYiyADAACsRZABAADWIsgAAABrEWQAAIC1gv3dQGPrP2u5T467+8lxPjluoOLv0V6cOwBXEq7IAAAAaxFkAACAtQgyAADAWgQZAABgLYIMAACwFkEGAABYiyADAACsRZABAADWIsgAAABrEWQAAIC1AjrIPProo3K5XB5Ljx49/N0WAAAIEAH/XUu9e/fWe++9574dHBzwLQMAgEYS8KkgODhYcXFx/m4DAAAEoIB+akmS8vPzlZCQoE6dOmns2LE6cuRIjfuXlZWptLTUYwEAAFemgL4iM3DgQC1btkzdu3dXUVGR5s+fr5tvvln79+9Xy5Ytq7zPwoULNX/+/EbuFACuHP1nLffJcXc/Oc4nx8XftoC+IpOenq677rpL/fr10/Dhw/XOO++opKREr7zySrX3yczM1KlTp9xLYWFhI3YMAAAaU0BfkfmxyMhIdevWTQcPHqx2n9DQUIWGhjZiVwAAwF8C+orMj505c0aHDh1SfHy8v1sBAAABIKCDzAMPPKDs7GwdPnxYH374oX76058qKChIY8aM8XdrAAAgAAT0U0tHjx7VmDFjdOLECUVHR+umm27Stm3bFB0d7e/WAABAAAjoIPPSSy/5uwUAABDAAvqpJQAAgJoQZAAAgLUIMgAAwFoEGQAAYC2CDAAAsBZBBgAAWIsgAwAArEWQAQAA1iLIAAAAaxFkAACAtQgyAADAWgQZAABgLYIMAACwFkEGAABYiyADAACsRZABAADWIsgAAABrEWQAAIC1CDIAAMBaBBkAAGAtggwAALAWQQYAAFiLIAMAAKxFkAEAANYK9ncDQKDpP2u5T467+8lxPjku/j/OnZ04b2gIrsgAAABrEWQAAIC1CDIAAMBaBBkAAGAtggwAALAWQQYAAFiLIAMAAKxFkAEAANYiyAAAAGsRZAAAgLUIMgAAwFoEGQAAYC2CDAAAsBZBBgAAWCvY3w0AAGrXf9Zynxx395PjfHJcfK+xz9vf4s8JV2QAAIC1CDIAAMBaBBkAAGAtggwAALAWQQYAAFiLIAMAAKxFkAEAANYiyAAAAGsRZAAAgLUIMgAAwFoEGQAAYC2CDAAAsBZBBgAAWIsgAwAArBXs7wYAAIB9+s9a7pPj7n5yXL3254oMAACwFkEGAABYiyADAACsRZABAADWIsgAAABrEWQAAIC1CDIAAMBaBBkAAGAtggwAALAWQQYAAFjLiiCzePFidejQQc2aNdPAgQO1Y8cOf7cEAAACQMAHmZdfflkzZszQvHnz9NFHHykpKUnDhw/X8ePH/d0aAADws4APMn/4wx80ceJE3XvvverVq5eeeeYZNW/eXC+88IK/WwMAAH4W0EHmwoUL2r17t1JTU93rmjRpotTUVOXk5PixMwAAEAiC/d1ATb755huVl5crNjbWY31sbKw+++yzKu9TVlamsrIy9+1Tp05JkkpLSyVJ5WXf+aTXy8f/ocas1dj1mM2ZWld6PWZzplZj12M2Z2pd6fV8Xevyf40xNd/BBLAvv/zSSDIffvihx/pZs2aZG264ocr7zJs3z0hiYWFhYWFhuQKWwsLCGrNCQF+RadOmjYKCgnTs2DGP9ceOHVNcXFyV98nMzNSMGTPctysqKnTy5Em1bt1aLperzrVLS0uVmJiowsJChYeHezdAANZq7HrMRr1Aq9XY9ZjNznpX8myNXc/bWsYYnT59WgkJCTXuF9BBJiQkRP3799fGjRs1cuRISd8Hk40bN2rq1KlV3ic0NFShoaEe6yIjI73uITw8vFF+qBq7VmPXYzbqBVqtxq7HbHbWu5Jna+x63tSKiIiodZ+ADjKSNGPGDGVkZGjAgAG64YYb9PTTT+vs2bO69957/d0aAADws4APMqNHj9bXX3+tRx55RMXFxbrmmmu0du3aSi8ABgAAf3sCPshI0tSpU6t9KslXQkNDNW/evEpPU9leq7HrMRv1Aq1WY9djNjvrXcmzNXY9X9dyGVPb+5oAAAACU0B/IB4AAEBNCDIAAMBaBBkAAGCtv6kgs3nzZt1xxx1KSEiQy+XS6tWrPbYbY/TII48oPj5eYWFhSk1NVX5+vsc+J0+e1NixYxUeHq7IyEjdd999OnPmjFf1xo8fL5fL5bGkpaV5VW/hwoW6/vrr1bJlS8XExGjkyJHKy8vz2Of8+fOaMmWKWrdurRYtWmjUqFGVPmzwyJEjuv3229W8eXPFxMRo1qxZunTpUr1rpaSkVJrt/vvvr3ctSVqyZIn69evn/gyC5ORkvfvuu47PVZdaTs5VlSeeeEIul0vTp0/3yXy11XJyvkcffbTSsXr06OGzuWqr5/S5+/LLL/Xzn/9crVu3VlhYmPr27atdu3a5tzv9eFJbPaceTzp06FDpOC6XS1OmTJHk/HmrrZ6T5628vFxz585Vx44dFRYWps6dO+vxxx/3+Ah8J89bXeo5+Xvg9OnTmj59utq3b6+wsDDdeOON2rlzp09mq0s9J2erUUO/RsAm77zzjnn44YfN66+/biSZVatWeWx/4oknTEREhFm9erXZu3ev+Yd/+AfTsWNH891337n3SUtLM0lJSWbbtm3mgw8+MF26dDFjxozxql5GRoZJS0szRUVF7uXkyZMe+9S13vDhw83SpUvN/v37TW5urrnttttMu3btzJkzZ9z73H///SYxMdFs3LjR7Nq1y/zkJz8xN954o3v7pUuXTJ8+fUxqaqrZs2ePeeedd0ybNm1MZmZmvWsNGTLETJw40WO2U6dO1buWMca88cYb5u233zYHDhwweXl55qGHHjJNmzY1+/fvd3SuutRycq4f27Fjh+nQoYPp16+fmTZtmuPnrS61nJxv3rx5pnfv3h7H+vrrr302V231nJzt5MmTpn379mb8+PFm+/bt5vPPPzfr1q0zBw8edO/j5ONJXeo59Xhy/Phxj2Ns2LDBSDKbNm3yyXmrrZ6T523BggWmdevW5q233jIFBQXm1VdfNS1atDCLFi3yyXmrSz0nfw/cfffdplevXiY7O9vk5+ebefPmmfDwcHP06FHHZ6tLPSdnq8nfVJD5oR8Hi4qKChMXF2eefPJJ97qSkhITGhpqXnzxRWOMMZ988omRZHbu3One59133zUul8t8+eWX9apnzPcnecSIEdXepyH1jh8/biSZ7Oxs9yxNmzY1r776qnufTz/91EgyOTk5xpjvg1eTJk1McXGxe58lS5aY8PBwU1ZWVudaxnz/4PPDX5A/5m2ty1q1amX+9Kc/+XSuH9fy5VynT582Xbt2NRs2bPCo4Yv5qqvl9Hzz5s0zSUlJVR7HF3PVVM/p2ebMmWNuuummao/l9ONJbfWM8d3jybRp00znzp1NRUVFo/x7+2E9Y5w9b7fffruZMGGCx7o777zTjB071hjj/HmrrZ4xzp23c+fOmaCgIPPWW2953P+6664zDz/8sOOz1VbPydlq8zf11FJNCgoKVFxcrNTUVPe6iIgIDRw4UDk5OZKknJwcRUZGasCAAe59UlNT1aRJE23fvt2rullZWYqJiVH37t01efJknThxwr2tIfUuf+t3VFSUJGn37t26ePGix3w9evRQu3btPObr27evx4cNDh8+XKWlpfrrX/9a51qXrVixQm3atFGfPn2UmZmpc+fOeczmTa3y8nK99NJLOnv2rJKTk306149r+XKuKVOm6Pbbb/eYQ/LNeauuli/my8/PV0JCgjp16qSxY8fqyJEjPpurpnpOz/bGG29owIABuuuuuxQTE6Nrr71Wzz33nHu7048ntdW7zOnHkwsXLujPf/6zJkyYIJfL5dN/b1XVu8yp83bjjTdq48aNOnDggCRp79692rJli9LT0yU5f95qq3eZE+ft0qVLKi8vV7NmzTyOHRYWpi1btjg+W231nJytNlZ8IF5jKC4ulqRKnxgcGxvr3lZcXKyYmBiP7cHBwYqKinLvUx9paWm688471bFjRx06dEgPPfSQ0tPTlZOTo6CgIK/rVVRUaPr06Ro0aJD69Onj7j0kJKTS9079eL6q5r+8ra61JOlnP/uZ2rdvr4SEBO3bt09z5sxRXl6eXn/9da9qffzxx0pOTtb58+fVokULrVq1Sr169VJubq7jc1VXyxdzSdJLL72kjz76yOO55cucPm811XJ6voEDB2rZsmXq3r27ioqKNH/+fN18883av3+/T34ea6rXsmVLR2f7/PPPtWTJEs2YMUMPPfSQdu7cqd/85jcKCQlRRkaG448ntdWTfPN4snr1apWUlGj8+PHunn3xOFJdPcnZn8kHH3xQpaWl6tGjh4KCglReXq4FCxZo7NixHvs7dd5qqyc5d95atmyp5ORkPf744+rZs6diY2P14osvKicnR126dHF8ttrqOTlbbQgyfnTPPfe4/9y3b1/169dPnTt3VlZWloYNG+b1cadMmaL9+/d7pGJfqa7WpEmT3H/u27ev4uPjNWzYMB06dEidO3eud53u3bsrNzdXp06d0l/+8hdlZGQoOzu7wf3Xp1avXr0cn6uwsFDTpk3Thg0bKv2fjdPqUsvJ+X74f539+vXTwIED1b59e73yyisKCwvzbggv6913332OzlZRUaEBAwboX/7lXyRJ1157rfbv369nnnnGHSycVJd6vng8ef7555Wenl7rtw87pap6Tp63V155RStWrNDKlSvVu3dv5ebmavr06UpISPDJeatLPSfP2//+7/9qwoQJatu2rYKCgnTddddpzJgx2r17t6Nz1bWer37H/RhPLf2fuLg4Sar06vtjx465t8XFxen48eMe2y9duqSTJ0+692mITp06qU2bNjp48KDX9aZOnaq33npLmzZt0tVXX+1eHxcXpwsXLqikpMRj/x/PV9X8l7fVtVZVBg4cKEkes9WnVkhIiLp06aL+/ftr4cKFSkpK0qJFi3wyV3W1fDHX7t27dfz4cV133XUKDg5WcHCwsrOz9cc//lHBwcGKjY11bL7aapWXlzs+3w9FRkaqW7duOnjwoE/OW031qtKQ2eLj491X6S7r2bOn+6kspx9PaqtXlYY+nnzxxRd677339Mtf/tK9zpfnrap6VWnIeZs1a5YefPBB3XPPPerbt69+8Ytf6Le//a0WLlzosb9T5622elVpyHnr3LmzsrOzdebMGRUWFmrHjh26ePGiOnXq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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "observation = The majority of couples prefer restaurants with an approximate cost of 300 rupees.\n",
        "\n"
      ],
      "metadata": {
        "id": "LYj_oa30Sm4q"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Correlation Matrix\n",
        "corr_matrix = data[['rate', 'votes', 'cost_for_two']].corr()\n",
        "\n",
        "\n",
        "plt.figure(figsize=(6, 4))\n",
        "sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')\n",
        "plt.title(\"Correlation Matrix\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 391
        },
        "id": "XXkcHtKsq9t7",
        "outputId": "eafecd28-5425-4b80-b79f-b0330d6cadf0"
      },
      "execution_count": 188,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 600x400 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "Observations:\n",
        "\n",
        "##**Rate vs Votes → 0.49**\n",
        "\n",
        "- Moderate positive correlation\n",
        "\n",
        "- Highly rated restaurants tend to get more votes.\n",
        "\n",
        "##**Votes vs Cost for Two → 0.32**\n",
        "\n",
        "- Mild correlation\n",
        "\n",
        "- Slight trend that expensive restaurants get more votes.\n",
        "\n",
        "##**Rate vs Cost for Two → 0.28**\n",
        "\n",
        "- Weak correlation\n",
        "\n",
        "- More expensive restaurants tend to have slightly better ratings, but not strongly.\n",
        "\n"
      ],
      "metadata": {
        "id": "6BxxBru7rRcW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Top 10 Rated Restaurants\n",
        "top_rated = data[data['rate'] >= 4.0][['name', 'rate', 'votes', 'cost_for_two']].sort_values(by='rate', ascending=False)\n",
        "print(\"Top Rated Restaurants:\")\n",
        "print(top_rated.head(10))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uGdxb2kDr8MY",
        "outputId": "262febf6-7126-428a-847b-2412398efdb7"
      },
      "execution_count": 189,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Top Rated Restaurants:\n",
            "                      name  rate  votes  cost_for_two\n",
            "44                  Onesta   4.6   2556           600\n",
            "7                   Onesta   4.6   2556           600\n",
            "38       Empire Restaurant   4.4   4884           750\n",
            "86           Meghana Foods   4.4   4401           600\n",
            "52  Corner House Ice Cream   4.3    345           400\n",
            "81           Frozen Bottle   4.2    146           400\n",
            "37         Szechuan Dragon   4.2   1647           600\n",
            "34                  Faasos   4.2    415           500\n",
            "12        The Coffee Shack   4.2    164           500\n",
            "9                Smacznego   4.2    504           550\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**The restaurant’s name that received the maximum votes in dataframe.**"
      ],
      "metadata": {
        "id": "9lBN8L6TsHJZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Top 10 Most Voted Restaurants\n",
        "most_voted = data.sort_values(by='votes', ascending=False).head(10)\n",
        "print(\"Top 10 Most Voted Restaurants:\")\n",
        "print(most_voted[['name', 'rate', 'votes']], \"\\n\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fNJ6MRtnlZ3S",
        "outputId": "5b88439d-ec5e-4fc9-9863-9b933de3c3aa"
      },
      "execution_count": 190,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Top 10 Most Voted Restaurants:\n",
            "                  name  rate  votes\n",
            "38   Empire Restaurant   4.4   4884\n",
            "86       Meghana Foods   4.4   4401\n",
            "7               Onesta   4.6   2556\n",
            "44              Onesta   4.6   2556\n",
            "65         Kabab Magic   4.1   1720\n",
            "37     Szechuan Dragon   4.2   1647\n",
            "54        Roving Feast   4.0   1047\n",
            "2      San Churro Cafe   3.8    918\n",
            "14     San Churro Cafe   3.8    918\n",
            "67  Gustoes Beer House   4.1    868 \n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(10, 6))\n",
        "sns.barplot(x='votes', y='name', data=most_voted, palette='viridis')\n",
        "plt.title(\"Top 10 Most Voted Restaurants\")\n",
        "plt.xlabel(\"Votes\")\n",
        "plt.ylabel(\"Restaurant Name\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 581
        },
        "id": "HKjRi44ymIRj",
        "outputId": "9dde4f8c-af62-412c-971f-1a7126a43570"
      },
      "execution_count": 191,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0, 0.5, 'Restaurant Name')"
            ]
          },
          "metadata": {},
          "execution_count": 191
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA8QAAAIjCAYAAADFmtJ5AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAfeRJREFUeJzs3Xl4Def///HXSSL7JoRYIkFij30pWjtJLUUptdRa1FJLbdWqrUhRVLVKN0EpLUo/1L4LtcdeO1GisSZiSSKZ3x9+zrengkQToef5uK5zXZmZe+55zznz6ff7cs/cYzIMwxAAAAAAAFbGJrMLAAAAAAAgMxCIAQAAAABWiUAMAAAAALBKBGIAAAAAgFUiEAMAAAAArBKBGAAAAABglQjEAAAAAACrRCAGAAAAAFglAjEAAAAAwCoRiAEAAJ7A399fHTp0yOwyAADpjEAMAPjPMZlMqfps3Lgxw2v56quv9MYbbyhfvnwymUyPDVU3btxQ165d5e3tLRcXF9WsWVN79+5N1XFq1Kghk8mkwMDAFLevWbPGfN4LFy58mlN5ot9++00jRox4Yrvo6GjZ2dmpbdu2j2xz8+ZNOTk56fXXX0/342ekf15j7u7uql69upYvX55hx7x48aJGjBihiIiIDDtGZnkeflMA/212mV0AAADpbc6cORbLs2fP1po1ax5aX7Ro0QyvZdy4cbp586YqVqyoqKioR7ZLTk5WgwYNtH//fg0cOFDZs2fXtGnTVKNGDe3Zs+eRQffvHB0ddfLkSe3cuVMVK1a02DZ37lw5Ojrq7t27//qcHuW3337Tl19++cQAkyNHDtWtW1dLly7V7du35ezs/FCbxYsX6+7du48NzU97/IxWt25dtWvXToZh6Ny5c/rqq6/UqFEjrVixQsHBwel+vIsXL2rkyJHy9/dX6dKl073/zPS8/KYA/rsIxACA/5x/hqjff/9da9asSVO4Si+bNm0yjw67uro+st3ChQu1bds2/fzzz2revLkkqUWLFipUqJCGDx+uefPmPfFYBQsW1L179/Tjjz9aBOK7d+/ql19+UYMGDbRo0aJ/f1LpoE2bNlq5cqV+/fVXvfnmmw9tnzdvnjw8PNSgQYNMqO7fKVSokMW11qxZMxUrVkxTpkzJkECc2e7du6fk5GTZ29tndikAkGbcMg0AsEq3bt1S//795evrKwcHBxUuXFiffvqpDMOwaGcymdSrVy/NnTtXhQsXlqOjo8qVK6fNmzen6jh+fn4ymUxPbLdw4ULlzJnT4hZhb29vtWjRQkuXLlV8fHyqjteqVSstWLBAycnJ5nX/+9//dPv2bbVo0SLFffbt26dXX31V7u7ucnV1Ve3atfX7779btElMTNTIkSMVGBgoR0dHZcuWTS+//LLWrFkjSerQoYO+/PJLSZa3DT9K06ZN5eLikmLQj46O1rp169S8eXM5ODhIkn7++WeVK1dOTk5Oyp49u9q2basLFy6Y93nS8ZOTk/XZZ5+pePHicnR0VM6cOdWtWzddv37d4tiGYWj06NHKmzevnJ2dVbNmTR0+fPiR55EaRYsWVfbs2XXq1CmL9fHx8Ro+fLgCAgLk4OAgX19fDRo06KHfes2aNXr55Zfl6ekpV1dXFS5cWB988IEkaePGjapQoYIkqWPHjubzDgsLkyRt2bLFfMv+g2P069dPd+7csThGjRo1VKNGjYdq79Chg/z9/c3LZ8+elclk0qeffqrPPvtMBQsWlIODg44cOaKEhAQNGzZM5cqVk4eHh1xcXPTKK69ow4YNFn3+vY+vv/7a3EeFChW0a9cui2M/7jedP3++ypUrJzc3N7m7uysoKEhTpkxJxS8CAP+HEWIAgNUxDEOvvfaaNmzYoM6dO6t06dJatWqVBg4cqAsXLmjy5MkW7Tdt2qQFCxaod+/ecnBw0LRp0xQSEqKdO3eqRIkS6VLTvn37VLZsWdnYWP5bdcWKFfX111/r+PHjCgoKemI/rVu31ogRI7Rx40bVqlVL0v3R1tq1aytHjhwPtT98+LBeeeUVubu7a9CgQcqSJYtmzJihGjVqaNOmTapUqZIkacSIEQoNDdXbb7+tihUrKjY2Vrt379bevXtVt25ddevWTRcvXkzx1vSUuLi4qHHjxlq4cKGuXbsmLy8v87YFCxYoKSlJbdq0kSSFhYWpY8eOqlChgkJDQ/XXX39pypQpCg8P1759++Tp6fnE43fr1s3cT+/evXXmzBl98cUX2rdvn8LDw5UlSxZJ0rBhwzR69GjVr19f9evX1969e1WvXj0lJCQ88ZweJSYmRtevX1fBggXN65KTk/Xaa69p69at6tq1q4oWLaqDBw9q8uTJOn78uJYsWWL+fRo2bKiSJUtq1KhRcnBw0MmTJxUeHi7pftgeNWqUhg0bpq5du+qVV16RJFWpUkXS/X9IuH37trp3765s2bJp586dmjp1qv7880/9/PPPT31OM2fO1N27d9W1a1c5ODjIy8tLsbGx+vbbb9WqVSt16dJFN2/e1Hfffafg4GDt3Lnzodu5582bp5s3b6pbt24ymUwaP368Xn/9dZ0+fVpZsmR57G+6Zs0atWrVSrVr19a4ceMkSUePHlV4eLj69Onz1OcFwAoZAAD8x/Xs2dP4+//JW7JkiSHJGD16tEW75s2bGyaTyTh58qR5nSRDkrF7927zunPnzhmOjo5G06ZN01SHi4uL0b59+0du69Sp00Prly9fbkgyVq5c+di+q1evbhQvXtwwDMMoX7680blzZ8MwDOP69euGvb29MWvWLGPDhg2GJOPnn38279ekSRPD3t7eOHXqlHndxYsXDTc3N6NatWrmdaVKlTIaNGjw2Br++T0/yYNzmzFjhsX6l156yciTJ4+RlJRkJCQkGDly5DBKlChh3Llzx9xm2bJlhiRj2LBhTzz+li1bDEnG3LlzLdavXLnSYn10dLRhb29vNGjQwEhOTja3++CDDwxJj/zt/k6S0blzZ+Py5ctGdHS0sXv3biMkJMSQZEyYMMHcbs6cOYaNjY2xZcsWi/2nT59uSDLCw8MNwzCMyZMnG5KMy5cvP/KYu3btMiQZM2fOfGjb7du3H1oXGhpqmEwm49y5c+Z11atXN6pXr/5Q2/bt2xt+fn7m5TNnzhiSDHd3dyM6Otqi7b1794z4+HiLddevXzdy5sxpcW0/6CNbtmzGtWvXzOuXLl1qSDL+97//mdc96jft06eP4e7ubty7d++hbQCQFtwyDQCwOr/99ptsbW3Vu3dvi/X9+/eXYRhasWKFxfrKlSurXLly5uV8+fKpcePGWrVqlZKSktKlpjt37phvD/47R0dH8/bUat26tRYvXqyEhAQtXLhQtra2atq06UPtkpKStHr1ajVp0kQFChQwr8+VK5dat26trVu3KjY2VpLk6empw4cP68SJE2k9tUeqV6+evL29LW6bPnPmjH7//Xe1atVKNjY22r17t6Kjo9WjRw/zdyFJDRo0UJEiRVI1e/PPP/8sDw8P1a1bV1euXDF/ypUrJ1dXV/MtvWvXrlVCQoLeffddi1tz+/btm6bz+u677+Tt7a0cOXKofPnyWrdunQYNGqT33nvPoqaiRYuqSJEiFjU9GNV/UJOnp6ckaenSpRa3waeWk5OT+e9bt27pypUrqlKligzD0L59+9Lc3wPNmjWTt7e3xTpbW1vzc8TJycm6du2a7t27p/Lly6c4W3rLli2VNWtW8/KD0e3Tp08/8fienp66deuW+ZZ9AHhaBGIAgNU5d+6ccufOLTc3N4v1D2adPnfunMX6lGZ4LlSokG7fvq3Lly+nS01OTk4pPif8YFbovwebJ3nzzTcVExOjFStWaO7cuWrYsOFD5ypJly9f1u3bt1W4cOGHthUtWlTJyck6f/68JGnUqFG6ceOGChUqpKCgIA0cOFAHDhxIdU0psbOzU8uWLbVlyxbz88APwvGD26Uf/BYp1VikSJGHfquUnDhxQjExMcqRI4e8vb0tPnFxcYqOjrY41j9/b29vb4vg9iSNGzfWmjVrtHz5co0YMUImk0m3b9+2uB3+xIkTOnz48EP1FCpUSJLMNbVs2VJVq1bV22+/rZw5c+rNN9/UTz/9lOpwHBkZqQ4dOsjLy0uurq7y9vZW9erVJd2/lftp5c+fP8X1s2bNUsmSJc3PmXt7e2v58uUpHitfvnwWyw++438+152SHj16qFChQnr11VeVN29ederUSStXrnyKMwFg7XiGGACA50CuXLlSfC3Tg3W5c+dOU181atTQxIkTFR4eni4zS1erVk2nTp3S0qVLtXr1an377beaPHmypk+frrfffvup+23btq2++OIL/fjjjxowYIB+/PFHFStWLF1fH5ScnKwcOXJo7ty5KW7/50jnv5U3b17VqVNHklS/fn1lz55dvXr1Us2aNc2TpiUnJysoKEiTJk1KsQ9fX19J9/8hZPPmzdqwYYOWL1+ulStXasGCBapVq5ZWr14tW1vbR9aRlJSkunXr6tq1axo8eLCKFCkiFxcXXbhwQR06dLAI1SaT6aEJ5R70kZKU/oHmhx9+UIcOHdSkSRMNHDhQOXLkkK2trUJDQx+aUEzSI2tPqY5/ypEjhyIiIrRq1SqtWLFCK1as0MyZM9WuXTvNmjXrifsDwAMEYgCA1fHz89PatWt18+ZNi5HTP/74w7z971K6Tfj48eNydnZOtzBVunRpbdmyRcnJyRYjiTt27JCzs7N55DC1Wrdurbfffluenp6qX79+im28vb3l7OysY8eOPbTtjz/+kI2NjTmYSZKXl5c6duyojh07Ki4uTtWqVdOIESPMgTg1s2n/U6VKlVSwYEHNmzdPdevW1eHDhzVmzBjz9ge/xbFjx8y3Ez9w7Ngxi9/qUccvWLCg1q5dq6pVqz52pP1BXydOnLC4hfzy5cupGrV8lG7dumny5MkaOnSomjZtKpPJpIIFC2r//v2qXbv2E783Gxsb1a5dW7Vr19akSZM0duxYffjhh9qwYYPq1KnzyP0PHjyo48ePa9asWWrXrp15fUq3GWfNmjXFW5VTMwL/wMKFC1WgQAEtXrzYoqbhw4enuo9/etx3Y29vr0aNGqlRo0ZKTk5Wjx49NGPGDH300UcKCAh46mMCsC7cMg0AsDr169dXUlKSvvjiC4v1kydPlslk0quvvmqxfvv27RbPQJ4/f15Lly5VvXr1HjtClxbNmzfXX3/9pcWLF5vXXblyRT///LMaNWqU4vPFT+pv+PDhmjZt2iPfD2tra6t69epp6dKlOnv2rHn9X3/9pXnz5unll1+Wu7u7JOnq1asW+7q6uiogIMDiNm8XFxdJ0o0bN9JUa5s2bbRv3z4NHz5cJpNJrVu3Nm8rX768cuTIoenTp1sca8WKFTp69KjFe4ofdfwWLVooKSlJH3/88UPHvnfvnrl9nTp1lCVLFk2dOtVilPKzzz5L0/n8k52dnfr376+jR49q6dKl5pouXLigb7755qH2d+7c0a1btyRJ165de2j7g9HzB9/Ho877wbX593MxDCPFVxMVLFhQf/zxh8UjAPv37zfPZp0aKR1vx44d2r59e6r7+KdHnds/r0cbGxuVLFlSklL9ijIAkBghBgBYoUaNGqlmzZr68MMPdfbsWZUqVUqrV6/W0qVL1bdvX4vX40hSiRIlFBwcbPHaJUkaOXLkE4/1v//9T/v375d0/12+Bw4c0OjRoyVJr732mvn/iW/evLleeukldezYUUeOHFH27Nk1bdo0JSUlpeo4/+Th4aERI0Y8sd3o0aPN77nt0aOH7OzsNGPGDMXHx2v8+PHmdsWKFVONGjVUrlw5eXl5affu3Vq4cKF69eplbvNg4rHevXsrODhYtra2evPNN59YQ9u2bTVq1CgtXbpUVatWtXjvbZYsWTRu3Dh17NhR1atXV6tWrcyvXfL391e/fv2eePzq1aurW7duCg0NVUREhOrVq6csWbLoxIkT+vnnnzVlyhQ1b95c3t7eGjBggEJDQ9WwYUPVr19f+/bt04oVK5Q9e/YnnsfjdOjQQcOGDdO4cePUpEkTvfXWW/rpp5/0zjvvaMOGDapataqSkpL0xx9/6KefftKqVatUvnx5jRo1Sps3b1aDBg3k5+en6OhoTZs2TXnz5tXLL78s6X6Y9fT01PTp0+Xm5iYXFxdVqlRJRYoUUcGCBTVgwABduHBB7u7uWrRoUYqj3Z06ddKkSZMUHByszp07Kzo6WtOnT1fx4sXNE6s9ScOGDbV48WI1bdpUDRo00JkzZzR9+nQVK1ZMcXFxT/W9Peo3ffvtt3Xt2jXVqlVLefPm1blz5zR16lSVLl3aPBcAAKRK5k1wDQDAs5HSq1tu3rxp9OvXz8idO7eRJUsWIzAw0JgwYYLF63YM4/5rdHr27Gn88MMPRmBgoOHg4GCUKVPG2LBhQ6qO3b59e/Orm/75+edrcq5du2Z07tzZyJYtm+Hs7GxUr17d2LVrV6qO8/fXLj1KSq9dMgzD2Lt3rxEcHGy4uroazs7ORs2aNY1t27ZZtBk9erRRsWJFw9PT03BycjKKFClijBkzxkhISDC3uXfvnvHuu+8a3t7ehslkStMrmCpUqGBIMqZNm5bi9gULFhhlypQxHBwcDC8vL6NNmzbGn3/+adHmScf/+uuvjXLlyhlOTk6Gm5ubERQUZAwaNMi4ePGiuU1SUpIxcuRII1euXIaTk5NRo0YN49ChQ4afn1+qX7vUs2fPFLeNGDHCkGS+dhISEoxx48YZxYsXNxwcHIysWbMa5cqVM0aOHGnExMQYhmEY69atMxo3bmzkzp3bsLe3N3Lnzm20atXKOH78uEXfS5cuNYoVK2bY2dlZXFtHjhwx6tSpY7i6uhrZs2c3unTpYuzfvz/F6++HH34wChQoYNjb2xulS5c2Vq1a9cjXLv39FVIPJCcnG2PHjjX8/PzM/ztZtmxZmvqQZAwfPty8/KjfdOHChUa9evWMHDlyGPb29ka+fPmMbt26GVFRUSl+9wDwKCbDSMXMBQAAWCmTyaSePXs+dHs1AAB48fEMMQAAAADAKhGIAQAAAABWiUAMAAAAALBKzDINAMBjMNUGAAD/XYwQAwAAAACsEoEYAAAAAGCVuGUa/xnJycm6ePGi3NzcZDKZMrscAAAAAJnEMAzdvHlTuXPnlo3No8eBCcT4z7h48aJ8fX0zuwwAAAAAz4nz588rb968j9xOIMZ/hpubm6T7F727u3smVwMAAAAgs8TGxsrX19ecER6FQIz/jAe3Sbu7uxOIAQAAADzxUUom1QIAAAAAWCUCMQAAAADAKnHLNP5zmlcbpCy2DpldBgAAAGA1lu+ZktklPBVGiAEAAAAAVolADAAAAACwSgRiAAAAAIBVIhADAAAAAKwSgRgAAAAAYJUIxAAAAAAAq0QgBgAAAABYJQIxAAAAAMAqEYgBAAAAAFaJQAwAAAAAsEoEYgAAAACAVSIQAwAAAACsEoEYAAAAAGCVCMQAAAAAAKtEIAYAAAAAWCUCMQAAAADAKhGIAQAAAABWiUAMAAAAALBKBOJU6NChg5o0aZLZZQAAAAAA0tELE4g7dOggk8n00CckJCTDjz1lyhSFhYWle78bN260OBdvb2/Vr19fBw8eTLdj1KhRQ3379k23/p6VF7VuAAAAAC+OFyYQS1JISIiioqIsPj/++GOGH9fDw0Oenp6P3J6QkPCv+j927JiioqK0atUqxcfHq0GDBv+6z8zwItYMAAAAwHq9UIHYwcFBPj4+Fp+sWbOat5tMJs2YMUMNGzaUs7OzihYtqu3bt+vkyZOqUaOGXFxcVKVKFZ06dcq8z4gRI1S6dGnNmDFDvr6+cnZ2VosWLRQTE2Nu889bpmvUqKFevXqpb9++yp49u4KDgyVJhw4d0quvvipXV1flzJlTb731lq5cufLE88qRI4d8fHxUtmxZ9e3bV+fPn9cff/xh3r5161a98sorcnJykq+vr3r37q1bt26Zt0+bNk2BgYFydHRUzpw51bx5c3PdmzZt0pQpU8yj0GfPnlVSUpI6d+6s/Pnzy8nJSYULF9aUKVMsakpphLZJkybq0KGDednf318ff/yx2rVrJ3d3d3Xt2lWSNHjwYBUqVEjOzs4qUKCAPvroIyUmJj70nc+ZM0f+/v7y8PDQm2++qZs3bz62bgAAAABITy9UIE6NBwEtIiJCRYoUUevWrdWtWzcNGTJEu3fvlmEY6tWrl8U+J0+e1E8//aT//e9/Wrlypfbt26cePXo89jizZs2Svb29wsPDNX36dN24cUO1atVSmTJltHv3bq1cuVJ//fWXWrRokeraY2JiNH/+fEmSvb29JOnUqVMKCQlRs2bNdODAAS1YsEBbt241n8Pu3bvVu3dvjRo1SseOHdPKlStVrVo1Sfdv9a5cubK6dOliHlH39fVVcnKy8ubNq59//llHjhzRsGHD9MEHH+inn35Kda0PfPrppypVqpT27dunjz76SJLk5uamsLAwHTlyRFOmTNE333yjyZMnW+x36tQpLVmyRMuWLdOyZcu0adMmffLJJ4+t+5/i4+MVGxtr8QEAAACA1LLL7ALSYtmyZXJ1dbVY98EHH+iDDz4wL3fs2NEcQgcPHqzKlSvro48+Mo/i9unTRx07drTo4+7du5o9e7by5MkjSZo6daoaNGigiRMnysfHJ8VaAgMDNX78ePPy6NGjVaZMGY0dO9a87vvvv5evr6+OHz+uQoUKPfK88ubNK0nmUd/XXntNRYoUkSSFhoaqTZs25tHawMBAff7556pevbq++uorRUZGysXFRQ0bNpSbm5v8/PxUpkwZSfdv9ba3t5ezs7PFedja2mrkyJHm5fz582v79u366aef0hTgJalWrVrq37+/xbqhQ4ea//b399eAAQM0f/58DRo0yLw+OTlZYWFhcnNzkyS99dZbWrduncaMGfPIuv8pNDTU4jwAAAAAIC1eqEBcs2ZNffXVVxbrvLy8LJZLlixp/jtnzpySpKCgIIt1d+/eVWxsrNzd3SVJ+fLlM4dhSapcubKSk5N17NixRwaycuXKWSzv379fGzZseCiwS/dHQx8XiLds2SJnZ2f9/vvvGjt2rKZPn27R74EDBzR37lzzOsMwlJycrDNnzqhu3bry8/NTgQIFFBISopCQEDVt2lTOzs6PPJ4kffnll/r+++8VGRmpO3fuKCEhQaVLl37sPikpX778Q+sWLFigzz//XKdOnVJcXJzu3btn/q4f8Pf3N4dhScqVK5eio6PTdOwhQ4bovffeMy/HxsamOJIMAAAAACl5oQKxi4uLAgICHtsmS5Ys5r9NJtMj1yUnJ//rWv4uLi5OjRo10rhx4x5qmytXrsf2lT9/fnl6eqpw4cKKjo5Wy5YttXnzZnO/3bp1U+/evR/aL1++fLK3t9fevXu1ceNGrV69WsOGDdOIESO0a9euR04ENn/+fA0YMEATJ05U5cqV5ebmpgkTJmjHjh3mNjY2NjIMw2K/vz8H/KjvYfv27WrTpo1Gjhyp4OBgeXh4aP78+Zo4caJFu7//JtL93yWtv4mDg4McHBzStA8AAAAAPPBCBeKMEhkZqYsXLyp37tySpN9//102NjYqXLhwqvsoW7asFi1aJH9/f9nZPf3X2rNnT4WGhuqXX35R06ZNVbZsWR05cuSx/xBgZ2enOnXqqE6dOho+fLg8PT21fv16vf7667K3t1dSUpJF+/DwcFWpUsXiOem/TzQmSd7e3oqKijIvJyUl6dChQ6pZs+Zj69+2bZv8/Pz04YcfmtedO3cuVef+dynVDQAAAADp6YWaVCs+Pl6XLl2y+KRmFucncXR0VPv27bV//35t2bJFvXv3VosWLR77/Oo/9ezZU9euXVOrVq20a9cunTp1SqtWrVLHjh3TFOycnZ3VpUsXDR8+XIZhaPDgwdq2bZt69eqliIgInThxQkuXLjVPqrVs2TJ9/vnnioiI0Llz5zR79mwlJyebw7y/v7927Nihs2fP6sqVK0pOTlZgYKB2796tVatW6fjx4/roo4+0a9cuizpq1aql5cuXa/ny5frjjz/UvXt33bhx44n1BwYGKjIyUvPnz9epU6f0+eef65dffkn1+T+QUt0AAAAAkJ5eqEC8cuVK5cqVy+Lz8ssv/+t+AwIC9Prrr6t+/fqqV6+eSpYsqWnTpqWpj9y5cys8PFxJSUmqV6+egoKC1LdvX3l6esrGJm1fc69evXT06FH9/PPPKlmypDZt2qTjx4/rlVdeUZkyZTRs2DDzaLanp6cWL16sWrVqqWjRopo+fbp+/PFHFS9eXJI0YMAA2draqlixYvL29lZkZKS6deum119/XS1btlSlSpV09erVh2bV7tSpk9q3b6927dqpevXqKlCgwBNHh6X7E4L169dPvXr1UunSpbVt2zbz7NNpkVLdAAAAAJCeTMY/HxS1MiNGjNCSJUsUERGR2aXgX4qNjZWHh4fqluqmLLY8WwwAAAA8K8v3TMnsEiw8yAYxMTEPTfD7dy/UCDEAAAAAAOmFQAwAAAAAsEpWH4hHjBjB7dIAAAAAYIWsPhADAAAAAKwTgRgAAAAAYJUIxAAAAAAAq0QgBgAAAABYJQIxAAAAAMAqEYgBAAAAAFaJQAwAAAAAsEoEYgAAAACAVSIQAwAAAACsEoEYAAAAAGCVCMQAAAAAAKtEIAYAAAAAWCUCMQAAAADAKtlldgFAelu4ebzc3d0zuwwAAAAAzzlGiAEAAAAAVolADAAAAACwSgRiAAAAAIBVIhADAAAAAKwSgRgAAAAAYJUIxAAAAAAAq0QgBgAAAABYJQIxAAAAAMAqEYgBAAAAAFaJQAwAAAAAsEp2mV0AkN6atQ6VXRbHzC4DAAAA/xErfhme2SUggzBCDAAAAACwSgRiAAAAAIBVIhADAAAAAKwSgRgAAAAAYJUIxAAAAAAAq0QgBgAAAABYJQIxAAAAAMAqEYgBAAAAAFaJQAwAAAAAsEoEYgAAAACAVSIQAwAAAACsEoEYAAAAAGCVCMQAAAAAAKtEIAYAAAAAWCUCMQAAAADAKhGIAQAAAABWiUAMAAAAALBKBOJnKCwsTJ6enpldxnOlRo0a6tu3b2aXAQAAAMAKWW0g7tChg0wmk955552HtvXs2VMmk0kdOnR49oVlkrNnz8pkMj30adu2bWaXBgAAAAAZwi6zC8hMvr6+mj9/viZPniwnJydJ0t27dzVv3jzly5cvk6vLHGvXrlXx4sXNyw++FwAAAAD4r7HaEWJJKlu2rHx9fbV48WLzusWLFytfvnwqU6aMRdvk5GSFhoYqf/78cnJyUqlSpbRw4UKLNr/++qsCAwPl6OiomjVratasWTKZTLpx44ZFu1WrVqlo0aJydXVVSEiIoqKizNt27dqlunXrKnv27PLw8FD16tW1d+9ei/1NJpO+/fZbNW3aVM7OzgoMDNSvv/5q3p6UlKTOnTubay1cuLCmTJmSqu8kW7Zs8vHxMX88PDwkSfHx8erdu7dy5MghR0dHvfzyy9q1a5fFvps2bVLFihXl4OCgXLly6f3339e9e/fM22/duqV27drJ1dVVuXLl0sSJEx86/rRp08zfYc6cOdW8efNU1Q0AAAAAaWXVgViSOnXqpJkzZ5qXv//+e3Xs2PGhdqGhoZo9e7amT5+uw4cPq1+/fmrbtq02bdokSTpz5oyaN2+uJk2aaP/+/erWrZs+/PDDh/q5ffu2Pv30U82ZM0ebN29WZGSkBgwYYN5+8+ZNtW/fXlu3btXvv/+uwMBA1a9fXzdv3rToZ+TIkWrRooUOHDig+vXrq02bNrp27Zqk++E9b968+vnnn3XkyBENGzZMH3zwgX766aen/p4GDRqkRYsWadasWdq7d68CAgIUHBxsPuaFCxdUv359VahQQfv379dXX32l7777TqNHjzb3MXDgQG3atElLly7V6tWrtXHjRouwv3v3bvXu3VujRo3SsWPHtHLlSlWrVu2RNcXHxys2NtbiAwAAAACpZTIMw8jsIjJDhw4ddOPGDX3zzTfy9fXVsWPHJElFihTR+fPn9fbbb8vT01NhYWGKj4+Xl5eX1q5dq8qVK5v7ePvtt3X79m3NmzdP77//vpYvX66DBw+atw8dOlRjxozR9evXzX117NhRJ0+eVMGCBSXdHxEdNWqULl26lGKdycnJ8vT01Lx589SwYUNJ90eIhw4dqo8//ljS/ZFXV1dXrVixQiEhISn206tXL126dOmhUe0Hzp49ax5RtrH5v38n2bJliwoVKqSsWbMqLCxMrVu3liQlJibK399fffv21cCBA/Xhhx9q0aJFOnr0qEwmk/ncBg8erJiYGN2+fVvZsmXTDz/8oDfeeEOSdO3aNeXNm1ddu3bVZ599psWLF6tjx476888/5ebm9oRfUBoxYoRGjhz50Po6Dd6XXRbHJ+4PAAAApMaKX4ZndglIo9jYWHl4eCgmJkbu7u6PbGfVzxBLkre3txo0aKCwsDAZhqEGDRooe/bsFm1Onjyp27dvq27duhbrExISzLdWHzt2TBUqVLDYXrFixYeO5+zsbA7DkpQrVy5FR0ebl//66y8NHTpUGzduVHR0tJKSknT79m1FRkZa9FOyZEnz3y4uLnJ3d7fo58svv9T333+vyMhI3blzRwkJCSpduvQTv48FCxaoaNGi5uUH/1iQmJioqlWrmtdnyZJFFStW1NGjRyVJR48eVeXKlc1hWJKqVq2quLg4/fnnn7p+/boSEhJUqVIl83YvLy8VLlzYvFy3bl35+fmpQIECCgkJUUhIiPm28JQMGTJE7733nnk5NjZWvr6+TzxHAAAAAJAIxJLu3zbdq1cvSfeD5D/FxcVJkpYvX648efJYbHNwcEjTsbJkyWKxbDKZ9PdB+vbt2+vq1auaMmWK/Pz85ODgoMqVKyshIeGJ/SQnJ0uS5s+frwEDBmjixImqXLmy3NzcNGHCBO3YseOJ9fn6+iogICBN55Re3NzctHfvXm3cuFGrV6/WsGHDNGLECO3atSvF11U5ODik+fsHAAAAgAes/hliSQoJCVFCQoISExMVHBz80PZixYrJwcFBkZGRCggIsPg8GJEsXLiwdu/ebbHfPyedSo3w8HD17t1b9evXV/HixeXg4KArV66kuY8qVaqoR48eKlOmjAICAnTq1Kk01/JAwYIFZW9vr/DwcPO6xMRE7dq1S8WKFZMkFS1aVNu3b7cI9+Hh4XJzc1PevHlVsGBBZcmSxSKUX79+XcePH7c4lp2dnerUqaPx48frwIEDOnv2rNavX//UtQMAAADAozBCLMnW1tZ866+tre1D293c3DRgwAD169dPycnJevnllxUTE6Pw8HC5u7urffv26tatmyZNmqTBgwerc+fOioiIUFhYmCRZ3Eb8JIGBgZozZ47Kly+v2NhYDRw4MM2vPgoMDNTs2bO1atUq5c+fX3PmzNGuXbuUP3/+NPXzgIuLi7p3766BAwfKy8tL+fLl0/jx43X79m117txZktSjRw999tlnevfdd9WrVy8dO3ZMw4cP13vvvScbGxu5urqqc+fOGjhwoLJly6YcOXLoww8/tHheedmyZTp9+rSqVaumrFmz6rffflNycrLFbdUAAAAAkF4IxP/f4x60lqSPP/5Y3t7eCg0N1enTp+Xp6amyZcvqgw8+kCTlz59fCxcuVP/+/TVlyhRVrlxZH374obp3756m23q/++47de3a1fxKqLFjx1rMQp0a3bp10759+9SyZUuZTCa1atVKPXr00IoVK9LUz9998sknSk5O1ltvvaWbN2+qfPnyWrVqlbJmzSpJypMnj3777TcNHDhQpUqVkpeXlzp37qyhQ4ea+5gwYYLi4uLUqFEjubm5qX///oqJiTFv9/T01OLFizVixAjdvXtXgYGB+vHHHy3eiwwAAAAA6cVqZ5l+FsaMGaPp06fr/PnzmV2KVXgwkxyzTAMAACA9Mcv0i4dZpjPBtGnTVKFCBWXLlk3h4eGaMGGCebIuAAAAAMDzhUCcjk6cOKHRo0fr2rVrypcvn/r3768hQ4ZkdlkAAAAAgBQQiNPR5MmTNXny5MwuAwAAAACQCrx2CQAAAABglQjEAAAAAACrRCAGAAAAAFglAjEAAAAAwCoRiAEAAAAAVolADAAAAACwSgRiAAAAAIBVIhADAAAAAKwSgRgAAAAAYJUIxAAAAAAAq0QgBgAAAABYJQIxAAAAAMAqEYgBAAAAAFbJLrMLANLbonlD5O7untllAAAAAHjOMUIMAAAAALBKBGIAAAAAgFUiEAMAAAAArBKBGAAAAABglQjEAAAAAACrRCAGAAAAAFglAjEAAAAAwCoRiAEAAAAAVolADAAAAACwSgRiAAAAAIBVIhADAAAAAKySXWYXAKS34D7jZGfvmNllAAAywZYZH2V2CQCAFwgjxAAAAAAAq0QgBgAAAABYJQIxAAAAAMAqEYgBAAAAAFaJQAwAAAAAsEoEYgAAAACAVSIQAwAAAACsEoEYAAAAAGCVCMQAAAAAAKtEIAYAAAAAWCUCMQAAAADAKhGIAQAAAABWiUAMAAAAALBKBGIAAAAAgFUiEAMAAAAArBKBGAAAAABglQjEAAAAAACrRCAGAAAAAFglArGVOX/+vDp16qTcuXPL3t5efn5+6tOnj65evfrMahgxYoRKly79zI4HAAAAACkhEFuR06dPq3z58jpx4oR+/PFHnTx5UtOnT9e6detUuXJlXbt2LbNLBAAAAIBnhkBsRXr27Cl7e3utXr1a1atXV758+fTqq69q7dq1unDhgj788ENJkr+/v8aOHatOnTrJzc1N+fLl09dff23R1/nz59WiRQt5enrKy8tLjRs31tmzZ83bN27cqIoVK8rFxUWenp6qWrWqzp07p7CwMI0cOVL79++XyWSSyWRSWFiYJGnSpEkKCgqSi4uLfH191aNHD8XFxT2rrwcAAACAlSEQW4lr165p1apV6tGjh5ycnCy2+fj4qE2bNlqwYIEMw5AkTZw4UeXLl9e+ffvUo0cPde/eXceOHZMkJSYmKjg4WG5ubtqyZYvCw8Pl6uqqkJAQJSQk6N69e2rSpImqV6+uAwcOaPv27eratatMJpNatmyp/v37q3jx4oqKilJUVJRatmwpSbKxsdHnn3+uw4cPa9asWVq/fr0GDRr0yHOKj49XbGysxQcAAAAAUssuswvAs3HixAkZhqGiRYumuL1o0aK6fv26Ll++LEmqX7++evToIUkaPHiwJk+erA0bNqhw4cJasGCBkpOT9e2338pkMkmSZs6cKU9PT23cuFHly5dXTEyMGjZsqIIFC5r7f8DV1VV2dnby8fGxqKFv377mv/39/TV69Gi98847mjZtWoo1h4aGauTIkU/3hQAAAACweowQW5kHI8BPUrJkSfPfJpNJPj4+io6OliTt379fJ0+elJubm1xdXeXq6iovLy/dvXtXp06dkpeXlzp06KDg4GA1atRIU6ZMUVRU1BOPuXbtWtWuXVt58uSRm5ub3nrrLV29elW3b99Osf2QIUMUExNj/pw/fz5V5wYAAAAAEoHYagQEBMhkMuno0aMpbj969KiyZs0qb29vSVKWLFkstptMJiUnJ0uS4uLiVK5cOUVERFh8jh8/rtatW0u6P2K8fft2ValSRQsWLFChQoX0+++/P7K+s2fPqmHDhipZsqQWLVqkPXv26Msvv5QkJSQkpLiPg4OD3N3dLT4AAAAAkFoEYiuRLVs21a1bV9OmTdOdO3cstl26dElz585Vy5YtzbdAP07ZsmV14sQJ5ciRQwEBARYfDw8Pc7syZcpoyJAh2rZtm0qUKKF58+ZJkuzt7ZWUlGTR5549e5ScnKyJEyfqpZdeUqFChXTx4sV0OHMAAAAASBmB2Ip88cUXio+PV3BwsDZv3qzz589r5cqVqlu3rvLkyaMxY8akqp82bdooe/bsaty4sbZs2aIzZ85o48aN6t27t/7880+dOXNGQ4YM0fbt23Xu3DmtXr1aJ06cMD9H7O/vrzNnzigiIkJXrlxRfHy8AgIClJiYqKlTp+r06dOaM2eOpk+fnpFfBwAAAAArRyC2IoGBgdq9e7cKFCigFi1aqGDBguratatq1qyp7du3y8vLK1X9ODs7a/PmzcqXL59ef/11FS1aVJ07d9bdu3fl7u4uZ2dn/fHHH2rWrJkKFSqkrl27qmfPnurWrZskqVmzZgoJCVHNmjXl7e2tH3/8UaVKldKkSZM0btw4lShRQnPnzlVoaGhGfh0AAAAArJzJSO0sS8BzLjY2Vh4eHnqpwweys3fM7HIAAJlgy4yPMrsEAMBz4EE2iImJeexcQ4wQAwAAAACsEoEYAAAAAGCVCMQAAAAAAKtEIAYAAAAAWCUCMQAAAADAKhGIAQAAAABWiUAMAAAAALBKBGIAAAAAgFUiEAMAAAAArBKBGAAAAABglQjEAAAAAACrRCAGAAAAAFglAjEAAAAAwCoRiAEAAAAAVolADAAAAACwSgRiAAAAAIBVssvsAoD0tmrKYLm7u2d2GQAAAACec4wQAwAAAACsEoEYAAAAAGCVCMQAAAAAAKtEIAYAAAAAWKWnCsRbtmxR27ZtVblyZV24cEGSNGfOHG3dujVdiwMAAAAAIKOkORAvWrRIwcHBcnJy0r59+xQfHy9JiomJ0dixY9O9QAAAAAAAMkKaA/Ho0aM1ffp0ffPNN8qSJYt5fdWqVbV37950LQ4AAAAAgIyS5kB87NgxVatW7aH1Hh4eunHjRnrUBAAAAABAhktzIPbx8dHJkycfWr9161YVKFAgXYoCAAAAACCjpTkQd+nSRX369NGOHTtkMpl08eJFzZ07VwMGDFD37t0zokYAAAAAANKdXVp3eP/995WcnKzatWvr9u3bqlatmhwcHDRgwAC9++67GVEjAAAAAADpzmQYhvE0OyYkJOjkyZOKi4tTsWLF5Orqmt61AWkSGxsrDw8Ple43RLYOjpldDoBMtjt0WGaXAAAAMsmDbBATEyN3d/dHtkvzCPED9vb2Klas2NPuDgAAAABApkpzIL57966mTp2qDRs2KDo6WsnJyRbbefUSAAAAAOBFkOZA3LlzZ61evVrNmzdXxYoVZTKZMqIuAAAAAAAyVJoD8bJly/Tbb7+patWqGVEPAAAAAADPRJpfu5QnTx65ubllRC0AAAAAADwzaQ7EEydO1ODBg3Xu3LmMqAcAAAAAgGcizbdMly9fXnfv3lWBAgXk7OysLFmyWGy/du1auhUHAAAAAEBGSXMgbtWqlS5cuKCxY8cqZ86cTKoFAAAAAHghpTkQb9u2Tdu3b1epUqUyoh4AAAAAAJ6JND9DXKRIEd25cycjagEAAAAA4JlJcyD+5JNP1L9/f23cuFFXr15VbGysxQcAAAAAgBdBmm+ZDgkJkSTVrl3bYr1hGDKZTEpKSkqfygAAAAAAyEBpDsQbNmzIiDoAAAAAAHim0hyIq1evnhF1AAAAAADwTKU5ED9w+/ZtRUZGKiEhwWJ9yZIl/3VRAAAAAABktDQH4suXL6tjx45asWJFitt5hhgAAAAA8CJI8yzTffv21Y0bN7Rjxw45OTlp5cqVmjVrlgIDA/Xrr79mRI0AAAAAAKS7NAfi9evXa9KkSSpfvrxsbGzk5+entm3bavz48QoNDc2IGq1GWFiYPD09/3U//v7++uyzz/51Pxnt7NmzMplMioiIyOxSAAAAAFihNAfiW7duKUeOHJKkrFmz6vLly5KkoKAg7d27N32re4F06NBBTZo0sVi3cOFCOTo6auLEiZlTVBqMGDFCJpPJ/Fqtv5swYYJMJpNq1KiRrsf09fVVVFSUSpQoka79AgAAAEBqpDkQFy5cWMeOHZMklSpVSjNmzNCFCxc0ffp05cqVK90LfFF9++23atOmjb766iv1798/s8tJlVy5cmnDhg36888/LdZ///33ypcvX7ofz9bWVj4+PrKze+q53QAAAADgqaU5EPfp00dRUVGSpOHDh2vFihXKly+fPv/8c40dOzbdC3wRjR8/Xu+++67mz5+vjh07mtdPmjRJQUFBcnFxka+vr3r06KG4uLiH9l+yZIkCAwPl6Oio4OBgnT9/3rzt1KlTaty4sXLmzClXV1dVqFBBa9eufaiPmzdvqlWrVnJxcVGePHn05ZdfPrHuHDlyqF69epo1a5Z53bZt23TlyhU1aNDAou2uXbtUt25dZc+eXR4eHqpevfpDdwj88ccfevnll+Xo6KhixYpp7dq1MplMWrJkiaSUb5k+fPiwGjZsKHd3d7m5uemVV17RqVOnnlg7AAAAAKRVmgNx27Zt1aFDB0lSuXLldO7cOe3atUvnz59Xy5Yt07u+F87gwYP18ccfa9myZWratKnFNhsbG33++ec6fPiwZs2apfXr12vQoEEWbW7fvq0xY8Zo9uzZCg8P140bN/Tmm2+at8fFxal+/fpat26d9u3bp5CQEDVq1EiRkZEW/UyYMEGlSpXSvn379P7776tPnz5as2bNE+vv1KmTwsLCzMvff/+92rRpI3t7e4t2N2/eVPv27bV161b9/vvvCgwMVP369XXz5k1J92cbb9KkiZydnbVjxw59/fXX+vDDDx977AsXLqhatWpycHDQ+vXrtWfPHnXq1En37t1LsX18fLxiY2MtPgAAAACQWv/6XlVnZ2eVLVs2PWp54a1YsUJLly7VunXrVKtWrYe29+3b1/y3v7+/Ro8erXfeeUfTpk0zr09MTNQXX3yhSpUqSZJmzZqlokWLaufOnapYsaJKlSqlUqVKmdt//PHH+uWXX/Trr7+qV69e5vVVq1bV+++/L0kqVKiQwsPDNXnyZNWtW/ex59CwYUO988472rx5s8qVK6effvpJW7du1ffff2/R7p/n9/XXX8vT01ObNm1Sw4YNtWbNGp06dUobN26Uj4+PJGnMmDGPPf6XX34pDw8PzZ8/X1myZDHX/iihoaEaOXLkY88HAAAAAB4l1YF41KhRqWo3bNiwpy7mRVeyZElduXJFw4cPV8WKFeXq6mqxfe3atQoNDdUff/yh2NhY3bt3T3fv3tXt27fl7OwsSbKzs1OFChXM+xQpUkSenp46evSoKlasqLi4OI0YMULLly9XVFSU7t27pzt37jw0Qly5cuWHllMz83SWLFnUtm1bzZw5U6dPn1ahQoVUsmTJh9r99ddfGjp0qDZu3Kjo6GglJSXp9u3b5jqOHTsmX19fcxiWpIoVKz722BEREXrllVfMYfhJhgwZovfee8+8HBsbK19f31TtCwAAAACpDsS//PLLY7cfP35cd+/etepAnCdPHi1cuFA1a9ZUSEiIVqxYITc3N0n3n5dt2LChunfvrjFjxsjLy0tbt25V586dlZCQYA7ETzJgwACtWbNGn376qQICAuTk5KTmzZsrISEh3c6jU6dOqlSpkg4dOqROnTql2KZ9+/a6evWqpkyZIj8/Pzk4OKhy5cr/qg4nJ6c0tXdwcJCDg8NTHw8AAACAdUt1IN63b1+K6yMiIvT+++/r8OHD6tKlS7oV9qLy8/PTpk2bzKF45cqVcnNz0549e5ScnKyJEyfKxub+o9s//fTTQ/vfu3dPu3fvNo+mHjt2TDdu3FDRokUlSeHh4erQoYP5+eS4uDidPXv2oX5+//33h5Yf9PEkxYsXV/HixXXgwAG1bt06xTbh4eGaNm2a6tevL0k6f/68rly5Yt5euHBhnT9/Xn/99Zdy5swp6f5EXI9TsmRJzZo1S4mJiakeJQYAAACAp5XmSbUeOHPmjNq2basKFSrIw8NDhw8f1vTp09OztheWr6+v+Vbi4OBgxcbGKiAgQImJiZo6dapOnz6tOXPmpPh9ZcmSRe+++6527NihPXv2qEOHDnrppZfMATkwMFCLFy9WRESE9u/fr9atWys5OfmhfsLDwzV+/HgdP35cX375pX7++Wf16dMn1eewfv16RUVFydPTM8XtgYGBmjNnjo4ePaodO3aoTZs2FiO8devWVcGCBdW+fXsdOHBA4eHhGjp0qCTJZDKl2GevXr0UGxurN998U7t379aJEyc0Z84c82u+AAAAACA9pTkQX7lyRe+++66KFCmiqKgobdu2TQsWLFBgYGBG1PfCyps3rzZu3KgrV64oODhY+fPn16RJkzRu3DiVKFFCc+fOVWho6EP7OTs7a/DgwWrdurWqVq0qV1dXLViwwLx90qRJypo1q6pUqaJGjRopODg4xUnN+vfvr927d6tMmTIaPXq0Jk2apODg4FTX7+Li8sgwLEnfffedrl+/rrJly+qtt95S7969lSNHDvN2W1tbLVmyRHFxcapQoYLefvtt8yzTjo6OKfaZLVs2rV+/XnFxcapevbrKlSunb775htFiAAAAABnCZBiGkZqGt27d0qeffqpJkyYpICBAoaGhqlevXkbXh/+Q8PBwvfzyyzp58qQKFiyY7v3HxsbKw8NDpfsNka1DyqEbgPXYHWq9c1oAAGDtHmSDmJgYubu7P7Jdqp8hLliwoG7evKl3331XrVq1kslk0oEDBx5ql9KMxLBOv/zyi1xdXRUYGKiTJ0+qT58+qlq1aoaEYQAAAABIq1QH4ujoaEnS+PHjNWHCBP19YNlkMskwDJlMJiUlJaV/lXgh3bx5U4MHD1ZkZKSyZ8+uOnXqaOLEiZldFgAAAABISkMgPnPmTEbWgf+gdu3aqV27dpldBgAAAACkKNWB2M/PLyPrAAAAAADgmXrq1y4BAAAAAPAiIxADAAAAAKwSgRgAAAAAYJUIxAAAAAAAq5TmQFyrVi3duHHjofWxsbGqVatWetQEAAAAAECGS3Mg3rhxoxISEh5af/fuXW3ZsiVdigIAAAAAIKOl+rVLBw4cMP995MgRXbp0ybyclJSklStXKk+ePOlbHQAAAAAAGSTVgbh06dIymUwymUwp3hrt5OSkqVOnpmtxAAAAAABklFQH4jNnzsgwDBUoUEA7d+6Ut7e3eZu9vb1y5MghW1vbDCkSAAAAAID0lupA7OfnJ0lKTk7OsGIAAAAAAHhWUh2I/+7EiRPasGGDoqOjHwrIw4YNS5fCAAAAAADISGkOxN988426d++u7Nmzy8fHRyaTybzNZDIRiAEAAAAALwSTYRhGWnbw8/NTjx49NHjw4IyqCXgqsbGx8vDwUExMjNzd3TO7HAAAAACZJLXZIM3vIb5+/breeOONf1UcAAAAAACZLc2B+I033tDq1aszohYAAAAAAJ6ZND9DHBAQoI8++ki///67goKClCVLFovtvXv3TrfiAAAAAADIKGl+hjh//vyP7sxk0unTp/91UcDT4BliAAAAAFLqs0GaR4jPnDnzrwoDAAAAAOB5kOZniAEAAAAA+C9I8wixJP3555/69ddfFRkZqYSEBIttkyZNSpfCAAAAAADISGkOxOvWrdNrr72mAgUK6I8//lCJEiV09uxZGYahsmXLZkSNAAAAAACkuzTfMj1kyBANGDBABw8elKOjoxYtWqTz58+revXqvJ8YAAAAAPDCSHMgPnr0qNq1aydJsrOz0507d+Tq6qpRo0Zp3Lhx6V4gAAAAAAAZIc23TLu4uJifG86VK5dOnTql4sWLS5KuXLmSvtUBT6HKl2Nl6+iQ2WUAyAD7+43M7BIAAMB/SJoD8UsvvaStW7eqaNGiql+/vvr376+DBw9q8eLFeumllzKiRgAAAAAA0l2aA/GkSZMUFxcnSRo5cqTi4uK0YMECBQYGMsM0AAAAAOCFkaZAnJSUpD///FMlS5aUdP/26enTp2dIYQAAAAAAZKQ0Tapla2urevXq6fr16xlVDwAAAAAAz0SaZ5kuUaKETp8+nRG1AAAAAADwzKQ5EI8ePVoDBgzQsmXLFBUVpdjYWIsPAAAAAAAvgjRPqlW/fn1J0muvvSaTyWRebxiGTCaTkpKS0q86AAAAAAAySJoD8YYNGzKiDgAAAAAAnqk0B+Lq1atnRB0AAAAAADxTaQ7Emzdvfuz2atWqPXUxAAAAAAA8K2kOxDVq1Hho3d+fJeYZYgAAAADAiyDNs0xfv37d4hMdHa2VK1eqQoUKWr16dUbUCAAAAABAukvzCLGHh8dD6+rWrSt7e3u999572rNnT7oUBgAAAABARkrzCPGj5MyZU8eOHUuv7gAAAAAAyFBpHiE+cOCAxbJhGIqKitInn3yi0qVLp1ddAAAAAABkqDQH4tKlS8tkMskwDIv1L730kr7//vt0KwwAAAAAgIyU5kB85swZi2UbGxt5e3vL0dEx3YoCAAAAACCjpTkQ+/n5ZUQdAAAAAAA8U2kOxJJ069Ytbdq0SZGRkUpISLDY1rt373Qp7EUxYsQILVmyRBEREZldCgAAAAAgDdIciPft26f69evr9u3bunXrlry8vHTlyhU5OzsrR44czzwQX758WcOGDdPy5cv1119/KWvWrCpVqpSGDRumqlWrPtNanjdnz55V/vz5zcuurq7Kly+fatSoob59+yowMDATqwMAAACAzJXm1y7169dPjRo10vXr1+Xk5KTff/9d586dU7ly5fTpp59mRI2P1axZM+3bt0+zZs3S8ePH9euvv6pGjRq6evXqM6/lebV27VpFRUVp//79Gjt2rI4ePapSpUpp3bp1j9znnyP/AAAAAPBfk+ZAHBERof79+8vGxka2traKj4+Xr6+vxo8frw8++CAjanykGzduaMuWLRo3bpxq1qwpPz8/VaxYUUOGDNFrr70mSQoLC5PJZHroM2LECHM/3377rYoWLSpHR0cVKVJE06ZNszjOn3/+qVatWsnLy0suLi4qX768duzYYdFmzpw58vf3l4eHh958803dvHnTvM3f31+fffaZRfvSpUtb1DBp0iQFBQXJxcVFvr6+6tGjh+Li4szbw8LC5OnpqVWrVqlo0aJydXVVSEiIoqKinvg9ZcuWTT4+PipQoIAaN26stWvXqlKlSurcubOSkpIk3b/1u3Tp0vr222+VP39+8yRpK1eu1MsvvyxPT09ly5ZNDRs21KlTpyz637Ztm0qXLi1HR0eVL19eS5YskclksriNfNOmTapYsaIcHByUK1cuvf/++7p37555e40aNdS7d28NGjRIXl5e8vHxsfh+AAAAACC9pTkQZ8mSRTY293fLkSOHIiMjJUkeHh46f/58+lb3BK6urnJ1ddWSJUsUHx+fYpuWLVsqKirK/Pnxxx9lZ2dnvp167ty5GjZsmMaMGaOjR49q7Nix+uijjzRr1ixJUlxcnKpXr64LFy7o119/1f79+zVo0CAlJyebj3Hq1CktWbJEy5Yt07Jly7Rp0yZ98sknaToXGxsbff755zp8+LBmzZql9evXa9CgQRZtbt++rU8//VRz5szR5s2bFRkZqQEDBqTpOA+O1adPH507d0579uwxrz958qQWLVqkxYsXm8PsrVu39N5772n37t1at26dbGxs1LRpU/P5x8bGqlGjRgoKCtLevXv18ccfa/DgwRbHu3DhgurXr68KFSpo//79+uqrr/Tdd99p9OjRFu1mzZolFxcX7dixQ+PHj9eoUaO0Zs2aR55HfHy8YmNjLT4AAAAAkFppfoa4TJky2rVrlwIDA1W9enUNGzZMV65c0Zw5c1SiRImMqPGR7OzsFBYWpi5dumj69OkqW7asqlevrjfffFMlS5aUJDk5OcnJyUnS/eDas2dPjR07VnXr1pUkDR8+XBMnTtTrr78uScqfP7+OHDmiGTNmqH379po3b54uX76sXbt2ycvLS5IUEBBgUUdycrLCwsLk5uYmSXrrrbe0bt06jRkzJtXn0rdvX/Pf/v7+Gj16tN555x2L0erExERNnz5dBQsWlCT16tVLo0aNSstXZlakSBFJ958zrlixoqT7t0nPnj1b3t7e5nbNmjWz2O/777+Xt7e3jhw5ohIlSmjevHkymUz65ptv5OjoqGLFiunChQvq0qWLeZ9p06bJ19dXX3zxhUwmk4oUKaKLFy9q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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Minimum vote restaurant**"
      ],
      "metadata": {
        "id": "enmf5I3itOIF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# low Voted Restaurants\n",
        "low_voted = data.sort_values(by='votes').head(10)\n",
        "print('low rated restaurants are:')\n",
        "print(low_voted[['name', 'rate', 'votes']], \"\\n\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c1klFZnSstQR",
        "outputId": "841718cc-8468-423d-c2db-b62b8e218590"
      },
      "execution_count": 192,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "low rated restaurants are:\n",
            "                                 name  rate  votes\n",
            "110               Hari Super Sandwich   3.2      0\n",
            "107                     Coffee Shopee   3.4      0\n",
            "117                      Kulfi & More   3.4      0\n",
            "118               Kannadigas Karavali   3.4      0\n",
            "116                        Wood Stove   3.4      0\n",
            "115               Aarush's Food Plaza   3.4      0\n",
            "114                         Cake Bite   3.4      0\n",
            "113  Dharwad Line Bazaar Mishra Pedha   3.4      0\n",
            "126           Banashankari Nati Style   2.9      0\n",
            "125              Soms Kitchen & Bakes   2.9      0 \n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.barplot(data=low_voted,x='votes',y='name',palette='viridis')\n",
        "plt.title('TOp 10 low voted restaurants')\n",
        "plt.xlabel('votes')\n",
        "plt.ylabel('Restaurant')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 472
        },
        "id": "NrxnQCE9mYOR",
        "outputId": "17dffd97-b29c-493e-9def-4d946d137f28"
      },
      "execution_count": 193,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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3qFOnToYNWoUZsyYkW9/c+bMwciRI1GnTh08evQIf/zxhzQrUaNGDYSHh+P27dto3LgxateujZ9++gkVKlRQesw1a9bEokWLMHfuXFSrVg2bNm3C7NmzP/v6jB07Fj179kTv3r3RoEED6Onp5XlULPD+vovs7GxplsLIyAhOTk4wNTWFg4NDgf27u7tj+/bt2Lt3L2rVqgVPT888TwAjIiIiKohMfO6CbqJSICwsDB4eHnj+/Hme73GgkpWWlgYDAwOkpqZyiRQREVEpUdT3b85cEBERERGRUjC5ICIiIiIipeAN3fRVcnd3/+xHuBIRERHRl+HMBRERERERKQWTCyIiIiIiUgomF0REREREpBRMLoiIiIiISCmYXBARERERkVIwuSAiIiIiIqVgckFERERERErB5IKIiIiIiJSCyQURERERESkFkwsiIiIiIlIKJhdERERERKQUTC6IiIiIiEgpmFwQEREREZFSMLkgIiIiIiKlYHJBRERERERKweSCiIiIiIiUgskFEREREREpBZMLIiIiIiJSCiYXRERERESkFEwuiIiIiIhIKZhcEBERERGRUjC5ICIiIiIipWByQfR/1qxZA3Nzc6ioqGDJkiUFlpWE4OBgGBoaltj4REREREXB5IJKvUePHmH48OGwsbGBpqYmzM3N4ePjg+PHjxe5j7S0NAwbNgwTJkzAX3/9hYEDB+Zb9ncJDw+Hp6cnjIyMoKOjAzs7O/Tu3RuZmZl/25hEREREysbkgkq1+Ph41KlTBydOnMD8+fNx7do1HDp0CB4eHhg6dGiR+0lISEBWVhZat24NMzMz6Ojo5Fv2d7h58ya8vb3h4uKCkydP4tq1a1i2bBk0NDSQnZ39t4xJRERE9HdgckGl2pAhQyCTyXDhwgV06NAB9vb2qFq1KsaMGYNz585J7RISEuDr6wu5XA59fX107twZjx8/BvB+yVH16tUBADY2NpDJZPmWxcfHAwD27NkDZ2dnaGlpwcbGBtOmTcO7d++ksV68eIH+/fvDxMQE+vr68PT0RHR0dIHncOTIEZiammLevHmoVq0aKleuDG9vb6xduxba2toKbQ8fPgxHR0fI5XJ4e3sjKSlJqsvJycH06dNRqVIlaGpqolatWjh06JBUHx8fD5lMhi1btsDV1RVaWlqoVq0awsPDFca4fv06WrZsCblcjvLly6Nn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FcozMjJgbGyc7zEBAQEYM2aMtJ+WlgZzc/MijUdERESlC5MLIiWws7ODTCbDrVu3Cm0XHx+PNm3aYPDgwZg5cyaMjIxw+vRp9OvXD5mZmVJyoampiWbNmmHfvn0YN24cKlasCADSvRn79++XynJpamoWOraBgQFsbW0BALa2tli3bh3MzMywdetW9O/fv0jnmZ6eDlVVVVy6dAmqqqoKdXK5PN9jNDU1PxkbERERfR2YXBApgZGREby8vLB8+XKMGDEiz30XL168gKGhIS5duoScnBwsXLgQKirvb3natm1bnv5UVFSwceNGdOvWDR4eHggLC0OFChXg5OQETU1NJCQkFLoEqihyk4M3b97kW6+hoYHs7GyFstq1ayM7OxvJyclo3LjxF41PREREXx/e0E2kJMuXL0d2djbq1auHkJAQ3LlzBzExMfj555+l+yNsbW2RlZWFZcuW4d69e9i4cSNWrVqVb3+qqqrYtGkTatasCU9PTzx69Ah6enrw9/fH6NGjsX79esTFxeHy5ctYtmwZ1q9fX2h8r1+/xqNHj/Do0SNER0dj8ODB0NLSQosWLfJtb2VlhfT0dBw/fhxPnz6V7tPo3r07evXqhZ07d+L+/fu4cOECZs+ejf3793/ZBSQiIqJSj8kFkZLY2Njg8uXL8PDwwNixY1GtWjU0b94cx48fx8qVKwEANWvWxKJFizB37lxUq1YNmzZtwuzZswvsU01NDZs3b0bVqlXh6emJ5ORkBAYGYvLkyZg9ezYcHR3h7e2N/fv3w9rautD41q5dCzMzM5iZmcHDwwNPnz7FgQMH4ODgkG97V1dXfP/99+jSpQtMTEwwb948AEBQUBB69eqFsWPHwsHBAW3btkVkZCQsLCyKeeWIiIjoayETn3MnKhHRF0pLS4OBgQFSU1Ohr69f0uEQERFRERT1/ZszF0REREREpBRMLoiIiIiISCmYXBARERERkVIwuSAiIiIiIqVgckFERERERErB5IKIiIiIiJSCyQURERERESkFkwsiIiIiIlIKJhdERERERKQUTC6IiIiIiEgpmFwQEREREZFSMLkgIiIiIiKlYHJBRERERERKweSCiIiIiIiUgskFEREREREpBZMLIiIiIiJSCiYXRERERESkFEwuiIiIiIhIKZhcEBERERGRUjC5ICIiIiIipWByQURERERESsHkgoiI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vZhclGKHDh2CmZkZzMzMUL9+fURGRmL79u1wd3cHAHz77bcYPXo0hg0bhlq1auHMmTOYPHnyZ42hoqKCLVu24NKlS6hWrRpGjx6N+fPnK7TR09PDvHnz4OLigrp160ofbnP/Ov8pgwYNQvv27dGlSxfUr18fKSkpCrMYxdGoUSPs378fkyZNwrJly1CzZk0sWrQIc+fORbVq1bBp06Y8j8tVJk9PT3h6euLdu3dSWVFicHV1xffff48uXbrAxMQE8+bNK9J4Xl5eWL9+PVq0aAFHR0cMHz4cXl5eCjMj06dPR3x8PCpXrgwTExOF4/v164fMzEzp0bUFqVChAiIiIpCdnY0WLVqgevXqGDVqFAwNDYv8ehMREdHXSyaEECUdBBGVrI0bN2L06NF4+PAhNDQ0/tax0tLSYGBggNTUVN5/QUREVEoU9f2bi6aJ/sNev36NpKQkzJkzB4MGDfrbEwsiIiL6unEdA9F/2Lx581ClShWYmpoiICCgpMMhIiKiUo7LoojoH8VlUURERKVPUd+/OXNBRERERERKweSCiIiIiIiUgskFEREREREpBZMLIiIiIiJSCiYXRERERESkFEwuiIiIiIhIKZhcEBERERGRUjC5ICIiIiIipWByQURERERESsHkgoiIiIiIlILJBRERERERKQWTCyIiIiIiUgomF0REREREpBRMLoiIiIiISCmYXBARERERkVIwuSAiIiIiIqVgckFERERERErB5IKIiIiIiJSCyQURERERESkFkwsiIiIiIlIKJhdERERERKQUTC6IiIiIiEgpmFxQqTN16lTUqlWrxPsozdzd3TFq1KiSDoOIiIi+Mkwu/iOePHmCwYMHw8LCApqamjA1NYWXlxciIiJKOjQFwcHBMDQ0VCiLiYmBubk5OnXqhMzMTPj7++P48eNSvZ+fH9q2bfvPBvqFFi5cCCsrK2hra8PBwQFr1qwp0nFWVlaQyWSQyWRQVVVFhQoV0K9fPzx//vxvjpiIiIjo05hc/Ed06NABV65cwfr163H79m3s3bsX7u7uSElJKenQChUZGYnGjRvD29sbW7duhYaGBuRyOYyNjUs6tGI7efIk/P39MXbsWMTExGDdunUwMTEp8vHTp09HUlISEhISsGnTJpw8eRIjRoz4GyMmIiIiKhomF/8BL168wKlTpzB37lx4eHjA0tIS9erV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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#  Average Cost by restautant Type\n",
        "avg_cost_by_type = data.groupby('restaurant_type')['cost_for_two'].mean()\n",
        "print(\" Average Cost by restaurant Type:\")\n",
        "print(avg_cost_by_type, \"\\n\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HTuYOM8Dmjlw",
        "outputId": "cf3c9e55-0031-4b35-9cb0-384bba236b14"
      },
      "execution_count": 194,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " Average Cost by restaurant Type:\n",
            "restaurant_type\n",
            "Buffet    671.428571\n",
            "Cafes     545.652174\n",
            "Dining    357.272727\n",
            "other     668.750000\n",
            "Name: cost_for_two, dtype: float64 \n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Restaurants with both online order and table booking\n",
        "both_services = data[(data['online_order'] == 'Yes') & (data['book_table'] == 'Yes')].shape[0]\n",
        "print(f\" Number of Restaurants with Both Online Order & Table Booking: {both_services}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lL9TWsLtm8vU",
        "outputId": "52276ed5-75c2-4ee9-e729-35b5c3ba5709"
      },
      "execution_count": 195,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " Number of Restaurants with Both Online Order & Table Booking: 7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        " The .shape[0] counts how many rows match both conditions."
      ],
      "metadata": {
        "id": "l7s9StnMb0Zu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "both_services = data[(data['online_order'] == 'Yes') & (data['book_table'] == 'Yes')]\n",
        "both_services"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 269
        },
        "id": "lqMQe8SSbi6i",
        "outputId": "2d94c03a-3055-49dc-88dc-5fbfaf7bc08e"
      },
      "execution_count": 196,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                name online_order book_table  rate  votes  cost_for_two  \\\n",
              "0              Jalsa          Yes        Yes   4.1    775           800   \n",
              "7             Onesta          Yes        Yes   4.6   2556           600   \n",
              "11      Cafe Shuffle          Yes        Yes   4.2    150           600   \n",
              "12  The Coffee Shack          Yes        Yes   4.2    164           500   \n",
              "44            Onesta          Yes        Yes   4.6   2556           600   \n",
              "57            Wamama          Yes        Yes   4.2    354           800   \n",
              "61          Goa 0 Km          Yes        Yes   3.6    163           800   \n",
              "\n",
              "   restaurant_type  \n",
              "0           Buffet  \n",
              "7            Cafes  \n",
              "11           Cafes  \n",
              "12           Cafes  \n",
              "44           other  \n",
              "57           other  \n",
              "61          Dining  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-f4f3f195-5597-461b-b7c8-3e23f4ec3be5\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>name</th>\n",
              "      <th>online_order</th>\n",
              "      <th>book_table</th>\n",
              "      <th>rate</th>\n",
              "      <th>votes</th>\n",
              "      <th>cost_for_two</th>\n",
              "      <th>restaurant_type</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Jalsa</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>4.1</td>\n",
              "      <td>775</td>\n",
              "      <td>800</td>\n",
              "      <td>Buffet</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>Onesta</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>4.6</td>\n",
              "      <td>2556</td>\n",
              "      <td>600</td>\n",
              "      <td>Cafes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>Cafe Shuffle</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>4.2</td>\n",
              "      <td>150</td>\n",
              "      <td>600</td>\n",
              "      <td>Cafes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>The Coffee Shack</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>4.2</td>\n",
              "      <td>164</td>\n",
              "      <td>500</td>\n",
              "      <td>Cafes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>44</th>\n",
              "      <td>Onesta</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>4.6</td>\n",
              "      <td>2556</td>\n",
              "      <td>600</td>\n",
              "      <td>other</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>57</th>\n",
              "      <td>Wamama</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>4.2</td>\n",
              "      <td>354</td>\n",
              "      <td>800</td>\n",
              "      <td>other</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>61</th>\n",
              "      <td>Goa 0 Km</td>\n",
              "      <td>Yes</td>\n",
              "      <td>Yes</td>\n",
              "      <td>3.6</td>\n",
              "      <td>163</td>\n",
              "      <td>800</td>\n",
              "      <td>Dining</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-f4f3f195-5597-461b-b7c8-3e23f4ec3be5')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-f4f3f195-5597-461b-b7c8-3e23f4ec3be5 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-f4f3f195-5597-461b-b7c8-3e23f4ec3be5');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    <div id=\"df-3b6d4d01-2b87-4579-bfa3-314391ac14d7\">\n",
              "      <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-3b6d4d01-2b87-4579-bfa3-314391ac14d7')\"\n",
              "                title=\"Suggest charts\"\n",
              "                style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "      </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "      <script>\n",
              "        async function quickchart(key) {\n",
              "          const quickchartButtonEl =\n",
              "            document.querySelector('#' + key + ' button');\n",
              "          quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "          quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "          try {\n",
              "            const charts = await google.colab.kernel.invokeFunction(\n",
              "                'suggestCharts', [key], {});\n",
              "          } catch (error) {\n",
              "            console.error('Error during call to suggestCharts:', error);\n",
              "          }\n",
              "          quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "          quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "        }\n",
              "        (() => {\n",
              "          let quickchartButtonEl =\n",
              "            document.querySelector('#df-3b6d4d01-2b87-4579-bfa3-314391ac14d7 button');\n",
              "          quickchartButtonEl.style.display =\n",
              "            google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "        })();\n",
              "      </script>\n",
              "    </div>\n",
              "\n",
              "  <div id=\"id_324618f0-e5cb-4bd2-9a2d-ca1642acc9cc\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('both_services')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_324618f0-e5cb-4bd2-9a2d-ca1642acc9cc button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('both_services');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "both_services",
              "summary": "{\n  \"name\": \"both_services\",\n  \"rows\": 7,\n  \"fields\": [\n    {\n      \"column\": \"name\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 6,\n        \"samples\": [\n          \"Jalsa\",\n          \"Onesta\",\n          \"Goa 0 Km\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"online_order\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 1,\n        \"samples\": [\n          \"Yes\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"book_table\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 1,\n        \"samples\": [\n          \"Yes\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"rate\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.3387652649872839,\n        \"min\": 3.6,\n        \"max\": 4.6,\n        \"num_unique_values\": 4,\n        \"samples\": [\n          4.6\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"votes\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1112,\n        \"min\": 150,\n        \"max\": 2556,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          775\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"cost_for_two\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 125,\n        \"min\": 500,\n        \"max\": 800,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          800\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"restaurant_type\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 4,\n        \"samples\": [\n          \"Cafes\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 196
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Filter restaurants with both Online Order and Table Booking\n",
        "both_online_table = data[(data['online_order'] == 'Yes') & (data['book_table'] == 'Yes')]\n",
        "\n",
        "# Bar Plot\n",
        "sns.barplot(x=['Both Features', 'Other Restaurants'], y=[both_online_table.shape[0], data.shape[0] - both_online_table.shape[0]])\n",
        "plt.title(\"Restaurants Offering Both Online Order and Table Booking\")\n",
        "plt.ylabel(\"Number of Restaurants\")\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "7xSV8eC3vdxm",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 452
        },
        "outputId": "ba6e1993-07a5-4fad-b5b2-0f1ba8b02a06"
      },
      "execution_count": 197,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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o0fRsWNHAMDGjRsxYcIEdO7cGVpaWujXrx9Wrlz5j9RPREREVV+lhp2OHTtCCFHs9JKmKVhYWGDTpk3qLIuIiIg0SJUes0NERERUXgw7REREpNEYdoiIiEijMewQERGRRmPYISIiIo3GsENEREQajWGHiIiINBrDDhEREWk0hh0iIiLSaAw7REREpNEYdoiIiEijMewQERGRRmPYISIiIo3GsENEREQajWGHiIiINBrDDhEREWk0hh0iIiLSaAw7REREpNEYdoiIiEijMewQERGRRmPYISIiIo3GsENEREQajWGHiIiINBrDDhEREWk0hh0iIiLSaAw7REREpNEYdoiIiEijMewQERGRRmPYISIiIo2mcti5d+8e7t+/L90/e/YspkyZgjVr1qi1MCIiIiJ1UDnsDBkyBEePHgUAJCcnw8fHB2fPnsW///1vLFiwQO0FEhEREZWHymHn8uXLaNGiBQDg999/h7u7O/7++29s3LgR69evV3d9REREROWictjJy8uDXC4HABw6dAg9e/YEALi6uuLRo0fqrY6IiIionFQOOw0aNEBYWBiOHz+OgwcPws/PDwDw8OFDWFpaqr1AIiIiovJQOewsXrwYq1evRseOHTF48GA0btwYALB7927p8BYRERFRVaGj6gM6duyIp0+fIiMjA9WqVZPaR48eDSMjI7UWR0RERFReKu/Z6dSpE168eKEUdADAwsICn3zyidoKIyIiIlIHlcPOsWPH8OrVq0LtOTk5OH78uFqKIiIiIlKXUh/GunjxovT31atXkZycLN3Pz89HZGQkatasqd7qiIiIiMqp1Ht2mjRpgqZNm0Imk6FTp05o0qSJdPPw8MDChQsxZ84clZ48KioKPXr0gJ2dHWQyGXbu3Kk0XQiBOXPmwNbWFgYGBvD29saNGzeU+jx79gz+/v4wNTWFubk5RowYgczMTJXqICIiIs1V6rCTlJSEmzdvQgiBs2fPIikpSbo9ePAAGRkZ+Oyzz1R68qysLDRu3BihoaFFTl+yZAlWrlyJsLAwnDlzBkZGRvD19UVOTo7Ux9/fH1euXMHBgwexd+9eREVFYfTo0SrVQURERJpLJoQQlV0EAMhkMuzYsQO9e/cG8Gavjp2dHaZNm4bp06cDANLT02FtbY3169dj0KBBiI+Ph5ubG6Kjo+Hp6QkAiIyMRNeuXXH//n3Y2dmV6rkzMjJgZmaG9PR0mJqaVsjrIyLN5TFjQ2WXQFQlxSwdVqHzL+33t8qnngPAjRs3cPToUaSkpKCgoEBpmqqHsoqTlJSE5ORkeHt7S21mZmZo2bIlTp06hUGDBuHUqVMwNzeXgg4AeHt7Q0tLC2fOnEGfPn2KnHdubi5yc3Ol+xkZGWqpmYiIiKoelcPO2rVrMW7cOFSvXh02NjaQyWTSNJlMprawoxgAbW1trdRubW0tTUtOToaVlZXSdB0dHVhYWCgNoH5XSEgI5s+fr5Y6iYiIqGpTOewsXLgQX3/9NWbOnFkR9fwjgoODMXXqVOl+RkYG7O3tK7EiIiIiqigqX2cnLS0NAwYMqIhalNjY2AAAHj9+rNT++PFjaZqNjQ1SUlKUpr9+/RrPnj2T+hRFLpfD1NRU6UZERESaSeWwM2DAABw4cKAialHi5OQEGxsbHD58WGrLyMjAmTNn4OXlBQDw8vLC8+fPERMTI/U5cuQICgoK0LJlywqvkYiIiKo+lQ9jubi4YPbs2Th9+jQaNmwIXV1dpemTJk0q9bwyMzORmJgo3U9KSkJcXBwsLCzw0UcfYcqUKVi4cCHq1KkDJycnzJ49G3Z2dtIZW/Xr14efnx9GjRqFsLAw5OXlYcKECRg0aFCpz8QiIiIizabyqedOTk7Fz0wmw61bt0o9r2PHjuHjjz8u1B4QEID169dDCIG5c+dizZo1eP78Odq2bYsff/wRdevWlfo+e/YMEyZMwJ49e6ClpYV+/fph5cqVMDY2LnUdPPWciMqDp54TFa2qnHpeZa6zU5kYdoioPBh2iIpWVcKOymN2iIiIiD4kZbqo4P3797F7927cvXu30H9AX758uVoKIyIiIlIHlcPO4cOH0bNnT9SuXRvXrl2Du7s7bt++DSEEmjVrVhE1EhEREZWZyoexgoODMX36dFy6dAn6+vrYtm0b7t27hw4dOvwj198hIiIiUoXKYSc+Ph7Dhr0ZcKSjo4OXL1/C2NgYCxYswOLFi9VeIBEREVF5qBx2jIyMpHE6tra2uHnzpjTt6dOn6quMiIiISA1UHrPTqlUrnDhxAvXr10fXrl0xbdo0XLp0Cdu3b0erVq0qokYiIiKiMlM57CxfvhyZmZkAgPnz5yMzMxP//e9/UadOHZ6JRURERFWOSmEnPz8f9+/fR6NGjQC8OaQVFhZWIYURERERqYNKY3a0tbXxr3/9C2lpaRVVDxEREZFaqTxA2d3dXaX/f0VERERUmVQOOwsXLsT06dOxd+9ePHr0CBkZGUo3IiIioqpE5QHKXbt2BQD07NkTMplMahdCQCaTIT8/X33VEREREZWTymHn6NGjFVEHERERUYVQOex06NChIuogIiIiqhAqh52oqKgSp7dv377MxRARERGpm8php2PHjoXa3h67wzE7REREVJWofDZWWlqa0i0lJQWRkZFo3rw5Dhw4UBE1EhEREZWZynt2zMzMCrX5+PhAT08PU6dORUxMjFoKIyIiIlIHlffsFMfa2hoJCQnqmh0RERGRWqi8Z+fixYtK94UQePToEb755hs0adJEXXURERERqYXKYadJkyaQyWQQQii1t2rVCr/88ovaCiMiIiJSB5XDTlJSktJ9LS0t1KhRA/r6+morioiIiEhdVA47Dg4OFVEHERERUYVQOewAQFZWFv766y/cvXsXr169Upo2adIktRRGREREpA4qh53z58+ja9euyM7ORlZWFiwsLPD06VMYGhrCysqKYYeIiIiqFJVPPQ8KCkKPHj2QlpYGAwMDnD59Gnfu3IGHhwe+/fbbiqiRiIiIqMxUDjtxcXGYNm0atLS0oK2tjdzcXNjb22PJkiX4v//7v4qokYiIiKjMVA47urq60NJ68zArKyvcvXsXwJsrK9+7d0+91RERERGVk8pjdpo2bYro6GjUqVMHHTp0wJw5c/D06VP8+uuvcHd3r4gaiYiIiMpM5T07ixYtgq2tLQDg66+/RrVq1TBu3Dg8efIEq1evVnuBREREROWh8p4dT09P6W8rKytERkaqtSAiIiIidVJ5z06nTp3w/PnzQu0ZGRno1KmTOmoiIiIiUhuVw86xY8cKXUgQAHJycnD8+HG1FEVERESkLqU+jPX2fzu/evUqkpOTpfv5+fmIjIxEzZo11VsdERERUTmVOuwo/tu5TCYr8nCVgYEBVq1apdbiiIiIiMqr1GEnKSkJQgjUrl0bZ8+eRY0aNaRpenp6sLKygra2doUUSURERFRWpQ47iv92XlBQUGHFEBEREambygOUIyIisG/fPun+F198AXNzc7Ru3Rp37txRa3FERERE5VWmiwoaGBgAAE6dOoUffvgBS5YsQfXq1REUFKTW4vLz8zF79mw4OTnBwMAAzs7O+OqrryCE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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.pie(sizes,labels=labels,autopct='%1.1f%%')\n",
        "plt.title(\"Restaurant offering both online order and booking table\")\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "cGVRrHi2fccs",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 428
        },
        "outputId": "d546bcdd-76ef-44fc-95e5-35afe85252e2"
      },
      "execution_count": 198,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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AObNm2d/3MOGDQOgSpUquWZKSUmhXbt27Nu3j1GjRlGpUiUWLFjAoEGDiI+P59FHH6VmzZrMmzePxx57jHLlyvHEE08A0KBBA/u+NZ06deK+++6zTzc5OZm2bdty7Ngxhg8fToUKFfj999955plnOHHiRLZ9S2bPns3FixcZNmwYvr6+hIWF5frhnJmZSefOnWnatClTp05l5cqVvPHGG1SpUoURI0YAtj+iPXr04K+//mLEiBHUqFGDb7/9loEDB17DMwajRo0iNDSUcePGsWfPHt577z0OHTpkL3pge72NHz+ejh07MmLECPt469evZ+3atXh7e/Pcc8+RkJDA0aNHeeuttwCy7UT46quv4uHhwZgxY0hISGDKlCkMGDCAdevWXTHjjh07aN26NSEhITz55JN4e3vzwQcf0K5dO3799VeaNm3qMP7DDz9M8eLFeemll4iJiWHatGmMGjWKL7/88pqWDeTtuQAYPnw4c+bMYfDgwTzyyCMcPHiQ6dOn8/fff9uXUW5WrlxJ165dqVy5MuPGjSMlJYV33nmHli1bsmnTpmzlMKf32YsvvsikSZO47bbbuO2229i0aRO33noraWlpDvfNj9dtbt577z1q165Nz5498fLy4rvvvuOhhx7CarUycuRIh3H37dtH3759GTJkCAMHDuTjjz9m0KBBNGzYkNq1awNw8uRJ2rdvT0ZGhv3zcObMmfj7++ea4XKZmZl06dKFZs2aMWXKFJYtW8ZLL71ERkYGEyZMAGyFsGfPnvz8888MGTKE+vXrs3z5csaOHcuxY8fsr2ewrWWfO3cuffv25YknnmDdunVMnjyZXbt28fXXX+eaY+bMmTz44IM8++yzTJo06aq5r/Y5CLbS/d///pd7772XZs2a8euvv+bp87tmzZpMmDCBF198kWHDhtm/YLdo0QKABQsWkJyczIgRIwgPD+evv/7inXfe4ejRoyxYsOCal29OTp06RbNmzbBYLIwaNYrIyEiWLl3KkCFDOH/+vOttwjbEbvbs2QZgrFy50jh9+rRx5MgRY+HChUZkZKTh6+trHDlyxD5uhw4djDp16hgXL160D7NarUaLFi2MqlWr2ofVq1fP6Nat2xXnO3LkSCO3pyI5Odnh97S0NOOmm24ybrnlFvuwgwcPGoAxe/bsbPcHjJdeesn++0svvWQAxt13333VeRmG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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**For Business Expansion**\n",
        "\n",
        "- Expand Online Ordering: It's clearly linked to better ratings.\n",
        "\n",
        "- Promote Table Booking: Slightly improves customer perception.\n",
        "\n",
        "- Support Low-Visibility Restaurants: Use engagement campaigns like instagram influencers,food blogers, ads  etc\n",
        "\n",
        "- Focus on Value + Quality: More impactful than pricing alone.\n",
        "\n",
        "- Data-backed Partner Selection: Prioritize cafes & quick bites for high conversion areas.\n",
        "\n",
        "- Underperforming Restaurants have to do promotions, work on quality,must have online booking.\n",
        "\n",
        "-  Restaurants that offer online ordering are rated better, possibly because of convenience, faster service, or customer expectations being met."
      ],
      "metadata": {
        "id": "_M8-4q-vuu1k"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "QsOM7_FcdA2D"
      },
      "execution_count": 198,
      "outputs": []
    }
  ]
}
