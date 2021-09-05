# python-networking

In my Operating Systems & Architecture class at Camosun College, I completed a series of assignments that involved installing and configuring Cent OS 7 (Linux Distribution) on a PC, and Rasbpian on a Raspberry Pi 3B+. 

Configuration of SSH, public key authentication and firewalls was completed to provide remote access to the system when required. The assignment being described is a networking project where dynamic data from a Pi Hat temperature sensor was retrieved and made available over the network.

Two Python files were provided in the assignment, temperature.py and web_temperature.py. Temperature.py extracted temperature data from the sensor. Web_temperature.py was provided as a program to read temperature data from the device file and display it in HTML. After installing pip and updating several python packages I started the web server using the command mod_wsgi-express start-server web_temperature.py. I had webserver log and general logs (journalctl) open in separate terminal windows to check for errors. 

The assignment provided read_temp and write_temp functions and instructed to modify the web_temperature program to turn on a red LED if the temperature rises,  a green LED if the temperature falls, and a yellow LED if the temperature stays the same.

To track temperature changes I had to write the current temperature to a file, so that the next time the page was loaded, the current temperature was read and compared to the new current temperature. From a web browser on the CentOS machine I visited http:____.____.____.____:8000/web_temperature.py (the Pi’s IP address was used in place of the blank lines) and was able to see the temperature being updated every 5 seconds.
