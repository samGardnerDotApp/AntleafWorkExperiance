**Overview**

This is a simple web app project which visualizes moisture data from an ada fruit moisture sensor hooked up to a raspberry pi by showing it in a graph.
****

**How to build with docker**

To build a docker image with this project you go to your working directory and run ```docker image build -t webapp .``` and to run the image run ```docker run -p 5000:5000 webapp```. This will start the server on [localhost:5000](http://localhost:5000).

****

**Changing range of data shown in graph**

To change the range of data shown in the graph you can pass a URL query by putting a ``?`` followed by the template ``start=YYYY-MM-DD&end=YYYY-MM-DD``. For example ``localhost:5000/?start=2025-12-20&end=2026-01-10`` would show the data between the 20th of December 2025 and the 10th of January 2026.