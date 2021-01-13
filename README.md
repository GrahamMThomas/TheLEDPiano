<img src="assets/images/square_logo.png" align="right" height="144px" />

# The LED Piano &nbsp; 

> "I Shorten Things" is a bit.ly clone I used to practice building a full stack application from the ground up.

To access the app, go to https://app.ishortenthings.com:

## About The Project

Inspired by: [Onlaj's Piano LED Visualizer](https://github.com/onlaj/Piano-LED-Visualizer).

Main reason I chose to rewrite it from scratch was:

- Move to Python3
- Make the codebase useable (Onlaj's has 1 file with ~ 3000 lines)
- Maintain two connections (piano/synthesia) instead of 1 (synthesia)
  - This allows us to do cool things like mark notes red/white depending on if you play them correctly
- Make it more hands off. Plug it in and connect. The project handles reconnections of devices seemlessly so no more sshing to get things to work.
- Overall productionalizing that I felt the original repo was missing

### Installation

1. Clone the repo

```sh
git clone https://github.com/GrahamMThomas/TheLEDPiano.git
```

2. Install required packages

```sh
pip install -r requirements.txt
```

3. Add midiusb.rules file

```sh
cp 33-midiusb.rules /etc/udev/rules.d/33-midiusb.rules
sudo udevadm control --reload
sudo service udev restart
```

4. Install [rtpmidi](https://www.tobias-erichsen.de/software/rtpmidi.html)
- Run and create a session. Name it whatever you want. Enable it. Ignore Bonjour errors
- Create a new Remote Peer (+ sign under directory). Chuck your PI address and use 5004 as the port
- Click connect and then turn on your piano (You have to reconnect rtpmidi everytime the piano turns off)

5. Open synthesia and make sure they are connected
- Set Key light to "Finger-Based" channel


<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/GrahamMThomas/TheLEDPiano/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Graham Thomas - [@CwakrJax](https://twitter.com/CwakrJax) - grahamthethomas@gmail.com

Project Link: [https://github.com/GrahamMThomas/TheLEDPiano](https://github.com/GrahamMThomas/TheLEDPiano)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [Onlaj's Piano LED Visualizer](https://github.com/onlaj/Piano-LED-Visualizer)

