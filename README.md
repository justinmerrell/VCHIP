# VCHIP.APP

A prank website intended to "scan" the chip that has been embeded when someone recives the vaccine. The web app makes use of a phones embeded hardware to communicate a false perception that a scan is indeed happening, because of this it is intended to only work on mobile devices.

*If the web app is opened on a non-mobile device the user is told the app will not work.*

## View Flow

1) To start the user is instructed to place their phone over the "injection" site and then hit the button to find the chip.
2) A screen indicating the chip has been found and if the users moves the chip is lost.

<img src="docs/images/mobile.PNG?raw=true" width="200"> <img src="docs/images/find_chip.jpg?raw=true" width="200"> <img src="docs/images/scanning.jpg?raw=true" width="200"> <img src="docs/images/found.jpg?raw=true" width="200"> <img src="docs/images/chip.jpg?raw=true" width="200"> <img src="docs/images/results.jpg?raw=true" width="200">

## Getting Started

``` BASH
sudo apt-get install python3-pip
sudo git clone git@github.com:justinmerrell/VCHIP.git
cd VCHIP
sudo source env/bin/activate
sudo pip install -r requirements.txt
```
