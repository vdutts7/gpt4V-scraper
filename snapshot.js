const puppeteer   = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
puppeteer.use(StealthPlugin());


const url = process.argv[2];
// const url = "https://en.wikipedia.org/wiki/Devious_lick#:~:text=A%20devious%20lick%20(also%20known,their%20school%2C%20typically%20from%20a";
const timeout = 6000; //adjust to liking

(async () => {

    // See README for Windows/Linux instructions
    const browser = await puppeteer.launch( {
        headless: "false",
        executablePath: '/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary',
        userDataDir: '/Users/vdutts7/Library/Application\ Support/Google/Chrome\ Canary/Default',
    } );

    const page = await browser.newPage();


    await page.setViewport( {
        width: 1200,
        height: 1200,
        deviceScaleFactor: 1,
    } );
    await page.goto( url, {
        waitUntil: "domcontentloaded",
        timeout: timeout,
    } );



    await page.waitForTimeout(timeout);

    await page.screenshot({
        path: "snapshot.jpg",
        fullPage: true,
    });

    await browser.close();
})();