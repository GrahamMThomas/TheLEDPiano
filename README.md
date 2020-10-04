<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** GrahamMThomas, TheLEDPiano, CwakrJax, grahamthethomas@gmail.com
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/GrahamMThomas/TheLEDPiano">
    <img src="assets/images/square_logo.png" alt="Logo" width="128" height="128">
  </a>

  <h3 align="center">The LED Piano</h3>

  <p align="center">
    Raspberry Pi zero and Light strips are used to achieve an awesome light up effect on your piano. Connect with <a href="https://synthesiagame.com/">Synthesia</a> to help you learn new songs by lighting up the correct notes to play.
    <br />
    <a href="https://github.com/GrahamMThomas/TheLEDPiano"><strong>Explore the docs (Github)»</strong></a>
    <br />
    <br />
    <a href="https://github.com/GrahamMThomas/TheLEDPiano">View Demo</a>
    ·
    <a href="https://github.com/GrahamMThomas/TheLEDPiano/issues">Report Bug</a>
    ·
    <a href="https://github.com/GrahamMThomas/TheLEDPiano/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About the Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->

## About The Project

Inspired by: [Onlaj's Piano LED Visualizer](https://github.com/onlaj/Piano-LED-Visualizer).

Main reason I chose to rewrite it from scratch was:

- Move to Python3
- Make the codebase useable (Onlaj's has 1 file with ~ 3000 lines)
- Maintain two connections (piano/synthesia) instead of 1 (synthesia)
  - This allows us to do cool things like mark notes red/white depending on if you play them correctly
- Make it more hands off. Plug it in and connect. The project handles reconnections of devices seemlessly so no more sshing to get things to work.
- Overall productionalizing that I felt the original repo was missing

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

- npm

```sh
npm install npm@latest -g
```

### Installation

1. Clone the repo

```sh
git clone https://github.com/GrahamMThomas/TheLEDPiano.git
```

2. Install NPM packages

```sh
npm install
```

<!-- USAGE EXAMPLES -->

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

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

Your Name - [@CwakrJax](https://twitter.com/CwakrJax) - grahamthethomas@gmail.com

Project Link: [https://github.com/GrahamMThomas/TheLEDPiano](https://github.com/GrahamMThomas/TheLEDPiano)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [Onlaj's Piano LED Visualizer](https://github.com/onlaj/Piano-LED-Visualizer)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/GrahamMThomas/repo.svg?style=flat-square
[contributors-url]: https://github.com/GrahamMThomas/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/GrahamMThomas/repo.svg?style=flat-square
[forks-url]: https://github.com/GrahamMThomas/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/GrahamMThomas/repo.svg?style=flat-square
[stars-url]: https://github.com/GrahamMThomas/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/GrahamMThomas/repo.svg?style=flat-square
[issues-url]: https://github.com/GrahamMThomas/repo/issues
[license-shield]: https://img.shields.io/github/license/GrahamMThomas/repo.svg?style=flat-square
[license-url]: https://github.com/GrahamMThomas/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/GrahamMThomas
[product-screenshot]: images/screenshot.png
