# 用法：python3 build.py [game.js] [輸出.html]
# 以 shell.html 為外殼（CSS、HUD 容器），把 game.js（已排版的完整打包程式）與 extra.css 塞回去。
# 另外加上「載入中」畫面與錯誤顯示，手機上載入失敗時看得到原因。
# game.js 末端有 window.__game 測試掛鉤，發佈前可留可拿掉，不影響遊戲。
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
SHELL = os.path.join(here, 'shell.html')
OUT = os.path.join(here, '..', 'index.html')
s = open(SHELL, encoding='utf-8').read()
a = s.index('<script>') + 8; b = s.rindex('</script>')
js = open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, 'game.js'), encoding='utf-8').read()
out = sys.argv[2] if len(sys.argv) > 2 else OUT
css = open(os.path.join(here, 'extra.css'), encoding='utf-8').read()
boot = '''<div id="boot"><b>載入中…</b><span>第一次開啟需要下載約 4 MB</span></div>
    <script>
      (function () {
        function show(m) {
          var el = document.getElementById("boot");
          if (!el) { el = document.createElement("div"); el.id = "boot"; document.body.appendChild(el); }
          el.className = "is-error";
          el.innerHTML = "<b>遊戲載入失敗</b><span></span>";
          el.lastChild.textContent = String(m).slice(0, 300);
        }
        window.addEventListener("error", function (e) { show(e.message || e.error); });
        window.addEventListener("unhandledrejection", function (e) { show((e.reason && (e.reason.message || e.reason)) || "未知錯誤"); });
      })();
    </script>
    '''
head = s[:a].replace('</style>', css + '\n</style>', 1)
i = head.rindex('<script>')
head = head[:i] + boot + head[i:]
open(out, 'w', encoding='utf-8').write(head + '\n' + js + '\n' + s[b:])
