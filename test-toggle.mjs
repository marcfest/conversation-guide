import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();
await page.setViewportSize({ width: 414, height: 896 });
await page.goto('http://localhost:5678');
await page.waitForSelector('.lens-btn');

// Screenshot 1: Listen should be active on load
await page.screenshot({ path: '/tmp/listen-active.png' });
console.log('✓ Screenshot 1: Listen active on load');

// Get initial state
let listenPressed = await page.getAttribute('[data-lens="listen"]', 'aria-pressed');
let respondPressed = await page.getAttribute('[data-lens="respond"]', 'aria-pressed');
let guidance = await page.textContent('#guidance');
console.log('Initial state: Listen aria-pressed=' + listenPressed + ', Respond aria-pressed=' + respondPressed);
console.log('Guidance visible:', guidance?.substring(0, 60) + '...');

// Click Respond
await page.click('[data-lens="respond"]');
await page.waitForTimeout(200);
await page.screenshot({ path: '/tmp/respond-active.png' });
console.log('✓ Screenshot 2: Respond active after click');

listenPressed = await page.getAttribute('[data-lens="listen"]', 'aria-pressed');
respondPressed = await page.getAttribute('[data-lens="respond"]', 'aria-pressed');
guidance = await page.textContent('#guidance');
console.log('After clicking Respond: Listen aria-pressed=' + listenPressed + ', Respond aria-pressed=' + respondPressed);
console.log('Guidance text:', guidance?.substring(0, 60) + '...');

// Click Listen again
await page.click('[data-lens="listen"]');
await page.waitForTimeout(200);
await page.screenshot({ path: '/tmp/listen-final.png' });

listenPressed = await page.getAttribute('[data-lens="listen"]', 'aria-pressed');
respondPressed = await page.getAttribute('[data-lens="respond"]', 'aria-pressed');
console.log('After clicking Listen: Listen aria-pressed=' + listenPressed + ', Respond aria-pressed=' + respondPressed);

await browser.close();
console.log('✓ All tests completed');
