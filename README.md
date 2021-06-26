<p align="center">
<img  src="https://drive.google.com/uc?export=view&id=1nZjIq1AbpMKXBDop7CEkvJNa6Tr2awQy" width="250" height="250">
</p>

# WebApp
<table>
<tr>
<td>
A web app using FastAPI to help to diagnose the mental health of a person. It helps to quantify the mental health among three parameters: stress, anxiety and depression, with the help of a specially designed questionnaire containing questions related to the defined parameters. Emotion detection is implemented to get an overview of the person's emotions in real time.  <br><br> A user will first have to register on the website after which they will be eligible for taking the questionnaire and emotional detection functionalities. A vent out wall is implemented on the website on which any person can share their thoughts and experiences with the community, anonymously.  On the basis of the scores taken from the questionnaire the mental state of the person will be approximated. The results do not guarantee anything, and it is easy to generate fake report, therefore we are relying on the user to answer the questionnaire punctually.<br><br>
</td>
</tr>
</table>

# Installation Guide:
1. python3 -m venv venv . Then activate your virtual environment(OS specific). (If you don't have venv, install it) [optional]
2. python3 -m pip install -r requirements.txt
3. uvicorn main:app --reload

# Built With
- [FastAPI](https://fastapi.tiangolo.com/) - _FastAPI_ is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- [jQuery - Ajax](http://www.w3schools.com/jquery/jquery_ref_ajax.asp) - _jQuery_ simplifies HTML document traversing, event handling, animating, and Ajax interactions for rapid web development.
- [Tensorflow](https://www.tensorflow.org/) - _TensorFlow_ is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML powered applications.
- [OpenCV](https://opencv.org/) - _OpenCV_ provides a real-time optimized Computer Vision library, tools, and hardware.
- [Uvicorn](https://www.uvicorn.org/) - _Uvicorn_ is a lightning-fast ASGI server implementation, using [uvloop](https://github.com/MagicStack/uvloop) and [httptools](https://github.com/MagicStack/httptools).
- [Bootstrap](http://getbootstrap.com/) - Extensive list of components and  Bundled Javascript plugins.
