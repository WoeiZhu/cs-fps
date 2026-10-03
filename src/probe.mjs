import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'] });
const p = await b.newPage({ viewport:{width:1280,height:720}});
p.on('console', m=>{ if(m.type()==='error'||m.type()==='warning') console.log('[console]',m.type(),m.text().slice(0,300)); });
p.on('pageerror', e=>console.log('[pageerror]',e.message));
await p.goto('file://'+process.cwd()+'/'+(process.argv[2]||'test.html'));
await p.waitForFunction(()=>window.__game, null, {timeout:60000});
const script = process.argv[3];
if (script) { const fs = await import('fs'); const code = fs.readFileSync(script,'utf8'); const r = await p.evaluate(code); console.log(typeof r==='string'?r:JSON.stringify(r,null,1)); }
if (process.argv[4]) await p.screenshot({path: process.argv[4]});
await b.close();
