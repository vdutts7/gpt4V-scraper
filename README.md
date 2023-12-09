<div align="center">


  <img src="https://res.cloudinary.com/dnz16usmk/image/upload/f_auto,q_auto/v1/vd7-website/gpt4v-logo" alt="Logo" width="80" height="80" />
  <img src="https://res.cloudinary.com/dnz16usmk/image/upload/f_auto,q_auto/v1/vd7-website/wikipedia-logo" alt="Logo" width="67" height="67"/>
   <img src="https://res.cloudinary.com/dnz16usmk/image/upload/f_auto,q_auto/v1/vd7-website/linkedin-logo" alt="Logo" width="67" height="67"/>

  <h1 align="center">
        GPT-4V Web Agent
    </h1>
    <p align="center"> 
        <i><b>AI agent that can SEE 👁️, control, navigate, & do stuff for you on your browser.</b></i>
        <br /> 
    </p>

[![Github][github]][github-url]

<img src="https://res.cloudinary.com/dnz16usmk/image/upload/f_auto,q_auto/v1/vd7-website/gpt4v-scraper"   />

 </div>

<br/>


## Table of Contents

  <ol>
    <a href="#about">📝 About</a><br/>
    <a href="#how-to-build">💻 How to build</a><br/>
    <a href="#tools-used">🔧 Tools used</a>
        <ul>
        </ul>
    <a href="#contact">👤 Contact</a>
  </ol>

<br/>

## 📝About

- Automated web scraping tool for capturing full-page screenshots.
- Utilizes Puppeteer with a stealth plugin to avoid detection by anti-bot mechanisms.
- Designed for efficiency with customizable timeout settings.


## 💻 How to build

### Part 1: Screenshot + Scrape
- Run `npm i` to install dependencies (Puppetteer libraries, see `package.json` for details).
- Copy `.env.template` and rename this new file `.env` . Then add your `OPENAI_API_KEY`and save the file. Run `source .env` properly mount this into the environment.
- Set up browser confguration to allow for websites with paywalls. Chrome Canary can be installed and then referenced in `snapshot.js`:
```
executablePath: '/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary',
userDataDir: '/Users/vdutts7/Library/Application\ Support/Google/Chrome\ Canary/Default',
``` 
Replace paths with respective locations specific to your device.

- Run `node snapshot.js "<URL>"` . Insert any URL in place of `<URL>`. 

Ex:
```
node snapshot.js "https://en.wikipedia.org/wiki/Devious_lick"
```
Wait for few seconds (adjust `const timeout = 6000;`  if too slow), and  `snapshot.jpg` will magically appear in root directory of project:

<div align="center">
    <i>snapshot.jpg</i>
    <img src="https://res.cloudinary.com/dnz16usmk/image/upload/f_auto,q_auto/v1/vd7-website/snapshot-deviouslick"   />
</div>


### Part 2: Image to Text Conversion 

This next part is better than a lot of OCR software on the market right now, in my opinion.

### Part 3: Image to Text Conversion


## 🔧Tools Used

[![GPT4Vision][GPT4Vision]][GPT4Vision-url]
[![Puppeteer][puppeteer]][puppeteer-url]

## 👤Contact

<!-- Replace placeholders with your actual contact information -->
[![Email][email]][email-url]
[![Twitter][twitter]][twitter-url]

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[GPT4Vision]: https://img.shields.io/badge/OpenAI_GPT--4V-0058A0?style=for-the-badge&logo=openai&logoColor=white&color=4aa481
[GPT4Vision-url]: https://openai.com/research/gpt-4v-system-card
[puppeteer]: https://img.shields.io/badge/Puppeteer-40B5A4?style=for-the-badge&logo=Puppeteer&logoColor=white
[puppeteer-url]: https://pptr.dev/
[email]: https://img.shields.io/badge/me@vd7.io-FFCA28?style=for-the-badge&logo=Gmail&logoColor=00bbff&color=black
[email-url]: #
[github]: https://img.shields.io/badge/💻Github-000000?style=for-the-badge
[github-url]: https://github.com/vdutts7/gpt4v-scraper
[twitter]: https://img.shields.io/badge/Twitter-FFCA28?style=for-the-badge&logo=Twitter&logoColor=00bbff&color=black
[twitter-url]: https://twitter.com/vdutts7/