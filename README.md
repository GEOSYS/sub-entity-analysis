<div id="top"></div>
<!-- PROJECT SHIELDS -->
<!--
*** See the bottom of this document for the declaration of the reference variables
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/GEOSYS">
    <img src="https://earthdailyagro.com/wp-content/uploads/2022/01/Logo.svg" alt="Logo" width="400" height="200">
  </a>

  <h1 align="center">Sub-Entity Analysis Processor</h1>

  <p align="center">
    Learn how to use &ltgeosys/&gt platform capabilities in your own business workflow! Build your processor and learn how to run them on your platform.
    <br />
    <a href="https://earthdailyagro.com/"><strong>Who we are</strong></a>
    <br />
    <br />
    <a href="https://github.com/GEOSYS/sub-entity-analysis-processor/issues">Report Bug</a>
    ·
    <a href="https://github.com/GEOSYS/sub-entity-analysis-processor/issues">Request Feature</a>
  </p>
</p>

<div align="center">
</div>

<div align="center">
  
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Twitter][twitter-shield]][twitter-url]
[![Youtube][youtube-shield]][youtube-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

</div>


<!-- TABLE OF CONTENTS -->
<details open>
  <summary>Table of Contents</summary>

- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  * [Prerequisite](#prerequisite)
  * [Installation](#installation)
- [Usage](#usage)
  * [Run the example inside a Docker container](#run-the-example-inside-a-docker-container)
  * [Usage with Jupyter Notebook](#usage-with-jupyter-notebook)
- [Project Organization](#project-organization)
- [Resources](#resources)
- [Support development](#support-development)
- [License](#license)
- [Contact](#contact)
- [Copyrights](#copyrights)

</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<p> The aim of this project is to help our customers valuing &ltgeosys/&gt platform capabilities to build their own analytic of interest. </p>

This directory exposes an example of code that will enable you to generate MR times series with GeosysPy for a given geometry and a sub-entity of this geometry and compare them between each other. It highlights the ability to retrieve a product time series in [xarray](https://docs.xarray.dev/en/stable/) format. 

This directory allows you to run this example both through a notebook and as a local application on your machine. 
 

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisite
 <p align="left">
Use of this project requires valids credentials from the &ltgeosys/&gt platform . If you need to get trial access, please register <a href=https://earthdailyagro.com/geosys-registration/>here</a>.
</p>

To be able to run this example, you will need to have following tools installed:

1. Install Conda: please install Conda on your computer. You can download and install it by following the instructions provided on the [official Conda website](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

2. Install Docker Desktop: please install Docker Desktop on your computer. You can download and install it by following the instructions provided on the [official Docker Desktop website](https://docs.docker.com/desktop/)

3. Install Jupyter Notebook: please install jupyter Notebook on your computer following the instructions provided on the [official Jupyter website](https://jupyter.org/install)

4. Install Git: please install Github on your computer. You can download and install it by visiting <a href=https://desktop.github.com/>here</a> and following the provided instructions


This package has been tested on Python 3.11.4

<p align="right">(<a href="#top">back to top</a>)</p>


### Installation

To set up the project, follow these steps:

1. Clone the project repository:

    ```
    git clone https://github.com/GEOSYS/sub-entity-analysis
    ```


2. Change the directory:

    ```
    cd sub-entity-analysis
    ```


3. Fill the environment variable (.env)

Ensure that you populate the .env file with your Geosys APIs credentials. If you haven't acquired the credentials yet, please click [here](https://earthdailyagro.com/geosys-registration/) to obtain them.
   
   ```
   API_CLIENT_ID = <your client id>
   API_CLIENT_SECRET = <your client id>
   API_USERNAME = <your username>
   API_PASSWORD = <your password>
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE -->
## Usage


### Usage with Jupyter Notebook

To use the project with Jupyter Notebook, follow these steps:


1. Create a Conda environment:

    To create a Conda environment, ensure first you have installed Conda on your computer. You can download and install it by following the instructions provided on the official Conda website. 

    
    ```
    conda create -y --name demo_example3
    ```


2. Activate the Conda environment:
    
    ```
    conda activate demo_example3

    ```
   
3. Install the project dependencies. You can do this by running the following command in your terminal:

    ```
    conda install -y pip
    pip install -r requirements.txt
    pip install ipykernel
    ```
4. Set up the Jupyter Notebook kernel for the project:

    ```
    python -m ipykernel install --user --name demo_example3 --display-name example3
    ```
5. Open the example notebook (sub_entity_analysis.ipynb) by clicking on it.



6. Select the "Kernel" menu and choose "Change Kernel". Then, select "example3" from the list of available kernels.


7. Run the notebook cells to execute the code example.

<p align="right">(<a href="#top">back to top</a>)</p>

### Run the example inside a Docker container

To set up and run the project using Docker, follow these steps:

1. Build the Docker image locally:
    
    ```
    docker build --tag demo_example3 .
    ```

2. Run the Docker container:

    ```
    docker run -d --name example3_container -p 8082:80 demo_example3
    ```

3. Access the API by opening a web browser and navigating to the following URL:
    
    ```
    http://127.0.0.1:8082/docs
    ```


This URL will open the Swagger UI documentation, click on the "Try it out" button for the POST endpoint, choose an indicator value and  enter the request body

Body Example for sub-entity-analysis/percentage-deviation endpoint:


```json
{
  "polygon": "POLYGON((-90.41169914 41.66631642, -90.41178502 41.6545818, -90.37753855 41.65413284, -90.37788188 41.666059940000004, -90.41169914 41.66631642))",
  "subPolygon":  "POLYGON((-90.39620670000001 41.66067377, -90.39623734 41.661004840000004, -90.39632852 41.66132771, -90.396478 41.661634480000004, -90.39668209 41.66191756, -90.39693578 41.6621701, -90.39723276000001 41.662385730000004, -90.39756577 41.66255921, -90.39792662 41.66268625, -90.39830643 41.662763760000004, -90.39869585 41.66278987, -90.39908518 41.662763760000004, -90.39946498 41.66268625, -90.39982584 41.66255921, -90.40015884 41.662385730000004, -90.40045592 41.6621701, -90.40070951 41.66191756, -90.40091361 41.661634480000004, -90.40106309000001 41.66132771, -90.40115427 41.661004840000004, -90.4011849 41.66067377, -90.40115427 41.66034277, -90.40106309000001 41.66001989, -90.40091361 41.65971311, -90.40070951 41.659429960000004, -90.40045592 41.659177480000004, -90.40015884 41.65896184, -90.39982584 41.65878835, -90.39946498 41.65866123, -90.39908518 41.65858372, -90.39869585 41.65855767, -90.39830643 41.65858372, -90.39792662 41.65866123, -90.39756577 41.65878835, -90.39723276000001 41.65896184, -90.39693578 41.659177480000004, -90.39668209 41.659429960000004, -90.396478 41.65971311, -90.39632852 41.66001989, -90.39623734 41.66034277, -90.39620670000001 41.66067377))",
  "startDate": "2022-05-26",
  "endDate": "2023-05-26"
}
```


Body Example for sub-entity-analysis/cumulative-index-values endpoint:


```json
{
  "polygon": "POLYGON((-90.41169914 41.66631642, -90.41178502 41.6545818, -90.37753855 41.65413284, -90.37788188 41.666059940000004, -90.41169914 41.66631642))",
  "startDate": "2022-05-26",
  "endDate": "2023-05-26"
}
```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- PROJECT ORGANIZATION -->
## Project Organization


    ├── README.md         
    ├── notebooks          
    ├── requirements.txt    
    ├── environment.yml   
    │
    ├── setup.py           
    ├───src                
    │   ├───main.py 
    │   ├───api
    │   │   ├── files
    │   │   │   └── favicon.svg
    │   │   ├── __init__.py
    │   │   └── api.py
    │   └───sub_entity_analysis
    │       ├── __init__.py
    │       ├── utils.py
    │       └── sub_entity_analysis.py      
    └── tests  

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- RESOURCES -->
## Resources 
The following links will provide access to more information:
- [EarthDaily agro developer portal  ](https://developer.geosys.com/)
- [Pypi package](https://pypi.org/project/geosyspy/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Support development

If this project has been useful, that it helped you or your business to save precious time, don't hesitate to give it a star.

<p align="right">(<a href="#top">back to top</a>)</p>

## License

Distributed under the [GPL 3.0 License](https://www.gnu.org/licenses/gpl-3.0.en.html). 

<p align="right">(<a href="#top">back to top</a>)</p>

## Contact

For any additonal information, please [email us](mailto:sales@earthdailyagro.com).

<p align="right">(<a href="#top">back to top</a>)</p>

## Copyrights

© 2023 Geosys Holdings ULC, an Antarctica Capital portfolio company | All Rights Reserved.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- List of available shields https://shields.io/category/license -->
<!-- List of available shields https://simpleicons.org/ -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=social
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=plastic&logo=appveyor
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/qgis-plugin/repo.svg?style=plastic&logo=appveyor
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/GEOSYS/sub-entity-analysis-processor/repo.svg?style=social
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/GEOSYS/qgis-plugin
[license-url]: https://www.gnu.org/licenses/gpl-3.0.en.html
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=social&logo=linkedin
[linkedin-url]: https://www.linkedin.com/company/earthdailyagro/mycompany/
[twitter-shield]: https://img.shields.io/twitter/follow/EarthDailyAgro?style=social
[twitter-url]: https://img.shields.io/twitter/follow/EarthDailyAgro?style=social
[youtube-shield]: https://img.shields.io/youtube/channel/views/UCy4X-hM2xRK3oyC_xYKSG_g?style=social
[youtube-url]: https://img.shields.io/youtube/channel/views/UCy4X-hM2xRK3oyC_xYKSG_g?style=social
[language-python-shiedl]: https://img.shields.io/badge/python-3.9-green?logo=python
[language-python-url]: https://pypi.org/ 
[GitStars-shield]: https://img.shields.io/github/stars/GEOSYS?style=social
[GitStars-url]: https://img.shields.io/github/stars/GEOSYS?style=social
[CITest-shield]: https://img.shields.io/github/workflow/status/GEOSYS/sub-entity-analysis-processor/Continous%20Integration
[CITest-url]: https://img.shields.io/github/workflow/status/GEOSYS/sub-entity-analysis-processor/Continous%20Integration
