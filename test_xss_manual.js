const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  await page.route("https://image.pollinations.ai/**", route => {
    // Return a dummy image
    route.fulfill({
      status: 200,
      contentType: 'image/png',
      body: Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=', 'base64')
    });
  });

  let xssDetected = false;
  page.on('dialog', async dialog => {
    console.log(`Dialog opened: ${dialog.message()}`);
    if (dialog.message().includes('XSS')) {
      xssDetected = true;
    }
    await dialog.accept();
  });

  await page.goto('file:///app/index.html');

  // Inject payload
  const payload = "')-alert('XSS')-('";
  await page.fill('#prompt', payload);
  await page.click('.gen-btn');

  // Wait for it to finish generating
  await page.waitForSelector('#dlBtn', { state: 'visible' });

  // Go to gallery
  await page.evaluate(() => switchTab('gallery'));

  // Click the image
  await page.click('.gallery-item img');

  await page.waitForTimeout(500);

  if (xssDetected) {
    console.log("XSS VULNERABILITY DETECTED!");
  } else {
    console.log("No XSS detected.");
  }

  await browser.close();
})();
